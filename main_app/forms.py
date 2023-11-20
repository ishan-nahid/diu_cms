from django import forms 
from .models import Booking, User, Counselling_Hour

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'depertment', 'user_id', 'email', 'password', 'role']

class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['faculty_id' ,'massage', 'weekday', 'slot']

class counsellingHourForm(forms.ModelForm):
    class Meta:
        model = Counselling_Hour
        fields = ['weekday', 'slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7', 'slot8']

class checkScheduleForm(forms.Form):
    faculty_id = forms.CharField(label='faculty_id')
    
class deleteSlot(forms.Form):
    pass