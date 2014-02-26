from django.contrib import admin

from campaign.models import Prospectus, Campaign, Vote


admin.site.register(Prospectus)
admin.site.register(Campaign)
admin.site.register(Vote)