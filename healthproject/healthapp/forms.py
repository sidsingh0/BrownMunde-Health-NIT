from .models import UserInfo, Exercise, Appointment
from django import forms

class UserInfoModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = 'all'


class ExerciseModelForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = 'all'


class AppointmentModelForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = 'all'