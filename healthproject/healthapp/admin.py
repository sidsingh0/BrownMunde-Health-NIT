from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Appointment)
admin.site.register(Calorie)
