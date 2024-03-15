from django.contrib import admin
from .models import message_table , registration_table

class admin_site(admin.ModelAdmin):
    list_display=['id', 'name', 'email' , 'subject' , 'phone_n' , 'message']


admin.site.register(message_table , admin_site)

class admin_registration(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'fname' , 'dob' , 'email' , 'address' , 'phone_n' , 'exp_skills' , 'information']


admin.site.register(registration_table , admin_registration)

# Register your models here.
