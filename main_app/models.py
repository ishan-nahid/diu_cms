from django.utils import timezone
import bcrypt
from django.db import models
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    depertment = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, default='')
    registration_time = models.DateTimeField(default=timezone.now)

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='student',
    )

    class Meta:
        db_table = "User_infoo"

    def save(self, *args, **kwargs):
        password_bytes = self.password.encode('utf-8')
        passwordd = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        self.password = passwordd.decode('utf-8')
        super().save(*args, **kwargs)
  
class Booking(models.Model):
    massage_id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=100)
    faculty_id = models.ForeignKey(User, verbose_name="", on_delete=models.CASCADE, related_name='faculty_id')
    massage = models.CharField(max_length=100)

    weekdays = [
        ('saturday' , 'Saturday'),
        ('sunday'   , 'Sunday'), 
        ('monday'   , 'Monday'),
        ('tuesday'  , 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday' , 'Thursday'),
    ]
    
    weekday = models.CharField(
        max_length=10,
        choices=weekdays, 
        default='saturday',
    )
    slot_options = [
        ('08:30 AM', '08:30 AM'),
        ('09:45 AM', '09:45 AM'),
        ('11:00 AM', '11:00 AM'),
        ('12:15 PM', '12:15 PM'),
        ('01:30 PM', '01:30 PM'),
        ('02:45 PM', '02:45 PM'),
        ('04:00 PM', '04:00 PM'),
        ('05:15 PM', '05:15 PM'),
    ]

    slot = models.CharField(
        max_length=10,
        choices=slot_options,
        default='08:30 AM',
    )

    approve = models.BooleanField(default=False)
    approve_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
        ('Pending', 'Pending'),
    )

    approve = models.CharField(max_length=10, choices=approve_CHOICES, default='Pending')

    booking_time = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super(Booking, self).save(*args, **kwargs)

class Counselling_Hour(models.Model):
    slot_id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(User, verbose_name="", on_delete=models.CASCADE, related_name='faculty')

    weekdays = [
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
    ]

    weekday = models.CharField(
        max_length=10,
        choices=weekdays,
        default='saturday',
    )

    slot1 = models.BooleanField(default=False)
    slot2 = models.BooleanField(default=False)
    slot3 = models.BooleanField(default=False)
    slot4 = models.BooleanField(default=False)
    slot5 = models.BooleanField(default=False)
    slot6 = models.BooleanField(default=False)
    slot7 = models.BooleanField(default=False)
    slot8 = models.BooleanField(default=False)

    on = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(Counselling_Hour, self).save(*args, **kwargs)

    slot_id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(User, verbose_name="", on_delete=models.CASCADE, related_name='faculty')

    weekdays = [
        ('saturday' , 'Saturday'),
        ('sunday'   , 'Sunday'), 
        ('monday'   , 'Monday'),
        ('tuesday'  , 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday' , 'Thursday'),
    ]

    weekday = models.CharField(
        max_length=10,
        choices=weekdays, 
        default='saturday',
    )


    slot1 = models.BooleanField(default=False)
    slot2 = models.BooleanField(default=False)
    slot3 = models.BooleanField(default=False)
    slot4 = models.BooleanField(default=False)
    slot5 = models.BooleanField(default=False)
    slot6 = models.BooleanField(default=False)
    slot7 = models.BooleanField(default=False)
    slot8 = models.BooleanField(default=False)

    on = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(Counselling_Hour, self).save(*args, **kwargs)