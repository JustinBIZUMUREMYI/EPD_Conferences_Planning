from django.contrib import admin
from .models import Attendees, Testimonial, Panalist, Sponsorships, booth, Document, BookSponsorship, Sponsor,Countdown, Speaker
from django.contrib.auth.models import Group

admin.site.register([Attendees])
admin.site.register([Sponsorships])
admin.site.register([Testimonial])
admin.site.register([Sponsor])
admin.site.register([Panalist])
admin.site.register([booth])
admin.site.register([BookSponsorship])
admin.site.register([Document])

admin.site.register([Countdown, Speaker])
admin.site.unregister(Group)

