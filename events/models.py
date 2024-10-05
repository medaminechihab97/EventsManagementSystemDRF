from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.




class Role(models.TextChoices):
    ADMIN = 'ROLE_ADMIN'
    USER = 'ROLE_USER'
    
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    role = models.CharField(choices=Role.choices, max_length=20, default=Role.USER)

    def has_role(self, role_name):
        return self.role == role_name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField(max_length=100)
    capacity = models.PositiveIntegerField()
    attendees = models.ManyToManyField(User, related_name='events', blank=True)
    waitlist = models.ManyToManyField(User, related_name='waitlisted_events', blank=True)
    actual_attendees = models.IntegerField(default=0)
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date cannot be after end date.')

        current_datetime = datetime.now()
        if self.start_date < current_datetime or self.end_date < current_datetime:
            raise ValidationError('Event cannot be scheduled in the past.')

        return super().clean()

    @property
    def is_full(self):
        return self.actual_attendees >= self.capacity

    def add_attendee(self, user):
        if not self.is_full:
            self.attendees.add(user)
            self.actual_attendees += 1
            self.save()
            return True, "Attendee added successfully"
        else:
            self.waitlist.add(user)
            return False, "Event is full. You've been added to the waitlist."