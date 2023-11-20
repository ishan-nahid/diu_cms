import bcrypt
from django.shortcuts import render, redirect
from .forms import User_form, LoginForm, BookingForm, counsellingHourForm, checkScheduleForm
from main_app.models import User, Booking, Counselling_Hour
from django.core.mail import send_mail
from django.conf import settings

def welcome(request):
    return render(request, 'welcome.html')

def register_user(request):
    if request.method == "POST":
        form = User_form(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            
            
            new_user.save()

            try:
                return redirect('login')
            except Exception as e:
                print("Redirect Exception:", str(e))
        else:
            print("Form errors:", form.errors) 
    else:
        form = User_form()

    return render(request, 'sign_up.html')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                print('not email here')
                user = None

            def check_password(plain_text_password, hashed_password):
                return bcrypt.checkpw(plain_text_password, hashed_password)

            if user and check_password(password.encode('utf-8'), user.password.encode('utf-8')) == True:
                request.session['authenticated'] = True
                request.session['user_id'] = user.user_id
                request.session['role'] = user.role
                return redirect(profile)
            
            else:
                print('pass not match')
                form.add_error(None, 'Invalid email or password')
            
    else:
        form = LoginForm()

    return render(request, 'login.html')

def profile(request):
    if request.session.get('authenticated'):
        user_id = request.session.get('user_id') 
        user_role = request.session.get('role')
        if user_id and user_role:
            user_identity = User.objects.get(user_id=user_id)
            if user_role == "faculty":
                messages_for_faculty = Booking.objects.filter(faculty_id_id=user_identity)
                schedule = Counselling_Hour.objects.filter(faculty_id=user_identity)
                
                latest_schedule = {}
                for entry in schedule:
                    latest_schedule[entry.weekday] = entry
                    
                order_of_days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday']

                filtered_schedule = {k: v for k, v in latest_schedule.items() if k.lower() in order_of_days}
                
                latest_schedule = {k: v for k, v in filtered_schedule.items() if v.on}
                
                sorted_schedule = sorted(latest_schedule.items(), key=lambda x: order_of_days.index(x[0]))

                updated_schedule = dict(sorted_schedule)
                
                return render(request, 'faculty_profile.html', {'user': user_identity, 'messages': messages_for_faculty, 'schedule': updated_schedule.values()})
            else:
                messages_of_students = Booking.objects.filter(student_id=user_id)
                return render(request, 'student_profile.html', {'user': user_identity, 'massage': messages_of_students})
        else:
            return render(request, 'welcome.html')
    else:
        return render(request, 'welcome.html')

def find_schedule(request):
    if request.session.get('authenticated'):
        if request.method == 'POST':
            form = checkScheduleForm(request.POST)

        
            user_id = request.session.get('user_id')
            user = User.objects.get(user_id=user_id)

            if form.is_valid():
                faculty_id = form.cleaned_data['faculty_id']
                info = User.objects.get(user_id=faculty_id)
                messages_of_students = Booking.objects.filter(student_id=user_id)
                
                schedule = Counselling_Hour.objects.filter(faculty_id=faculty_id)

                latest_schedule = {}
                for entry in schedule:
                    latest_schedule[entry.weekday] = entry

                order_of_days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday']

                filtered_schedule = {k: v for k, v in latest_schedule.items() if k.lower() in order_of_days}
                latest_schedule = {k: v for k, v in filtered_schedule.items() if v.on}
                
                sorted_schedule = sorted(latest_schedule.items(), key=lambda x: order_of_days.index(x[0].lower()))

                updated_schedule = dict(sorted_schedule)

                return render(request, 'student_profile.html', {'form': form, 'user': user, 'schedule': updated_schedule.values(), 'info': info, 'massage': messages_of_students})
        else:
            print("not ")
            return redirect('profile')
            # form = checkScheduleForm()
            # return render(request, 'profile.html', {'form': form})
    else:
        print("not authen")
        return render(request, 'welcome.html')
    
def request_slot(request):
    if request.session.get('authenticated'):
        if request.method == "POST":
            form = BookingForm(request.POST)

        
            user_id = request.session.get('user_id')
            user_role = request.session.get('role')
            
            if user_id and user_role:
                user = User.objects.get(user_id=user_id)

                if user_role == "student":
                    if form.is_valid():

                        faculty_id = form.cleaned_data['faculty_id']
                        f_mail = faculty_id.email

                        student_massange = form.cleaned_data['massage']

                        send_mail("Counselling Request", student_massange, settings.EMAIL_HOST_USER, [f_mail] )

                        new_booking = form.save(commit=False)
                        new_booking.student_id = user.user_id
                        new_booking.save()
                        return redirect('profile')
                    else:
                        print("Form errors:", form.errors)
                else:
                    print("Only students can request slots.")
                
            else:
                print("User not authenticated.")
                return redirect('user_login')
        else:
            form = BookingForm()
            return render(request, 'profile.html', {'form': form})
            
    else:
        return render(request, 'welcome.html')

def update_approve(request):
    if request.session.get('authenticated'):
        if request.method == "POST":
            booking_id = request.POST.get('booking_id')
            try:
                booking = Booking.objects.get(massage_id=booking_id)
                if booking.approve == 'Pending':
                    booking.approve = 'True'
                elif booking.approve == 'True':
                    booking.approve = 'False'
                else:
                    booking.approve = 'Pending'
                booking.save()
            except Booking.DoesNotExist:
                return redirect('student_profile')
        return redirect('profile')
    else:
        return render(request, 'welcome.html')

def edit_counselling_hour(request):
    if request.session.get('authenticated'):
        if request.method == 'POST':
            form = counsellingHourForm(request.POST)

        
            user_id = request.session.get('user_id')
            user = User.objects.get(user_id=user_id)

            if form.is_valid():
                
                booking = form.save(commit=False)
                booking.faculty = user
                
                booking.save()
                return redirect('profile')
            else:
                return redirect('profile')

        else:
            form = counsellingHourForm()
            return render(request, 'profile.html', {'form': form})
    else:
        return render(request, 'welcome.html')

def delete_slot(request):
    if request.session.get('authenticated'):
        if request.method == 'POST':
            slot_id = request.POST.get('slot_id')

            slot = Counselling_Hour.objects.get(slot_id=slot_id)
            print(slot)
            slot.on = not slot.on
            slot.save()
            return redirect('profile')
        else:
            return render(request, 'welcome.html')
    else:
        return render(request, 'welcome.html')
    

