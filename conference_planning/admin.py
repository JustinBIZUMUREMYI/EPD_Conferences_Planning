from django.contrib import admin
from .models import Attendees, Testimonial
from django.contrib.auth.models import Group

admin.site.register([Attendees])
admin.site.register([Testimonial])
admin.site.unregister(Group)

