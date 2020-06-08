from django.contrib import admin
from . models import contactdetails,email_contact

# Register your models here.
admin.site.register(contactdetails)
admin.site.register(email_contact)
