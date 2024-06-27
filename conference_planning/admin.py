from django.contrib import admin
from .models import Attendees, Testimonial, Panalist, Sponsorships, booth, Document, BookSponsorship, Sponsor,Countdown, Speaker,PreviousPhotos,PreviousVideos,Amount, FloorPlan, Booth_space, BookBooth, accessory, BookAccessory
from django.contrib.auth.models import Group

admin.site.register([Attendees, FloorPlan,Booth_space, BookBooth])
admin.site.register([Sponsorships, Amount, accessory, BookAccessory])
admin.site.register([Testimonial, PreviousPhotos,PreviousVideos])
admin.site.register([Sponsor]) 
admin.site.register([Panalist])
admin.site.register([booth])
admin.site.register([BookSponsorship])
admin.site.register([Document])
admin.site.register([Countdown, Speaker])
admin.site.unregister(Group)

