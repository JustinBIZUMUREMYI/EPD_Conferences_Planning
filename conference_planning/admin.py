from django.contrib import admin
from .models import Attendees
from django.contrib.auth.models import Group

admin.site.register([Attendees])
admin.site.unregister(Group)

