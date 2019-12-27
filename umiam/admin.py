from django.contrib import admin
from .models import HMCMember, Gallery, Achievement, QuickLinks

# Register your models here.
admin.site.register(HMCMember)
admin.site.register(Gallery)
admin.site.register(Achievement)
admin.site.register(QuickLinks)
