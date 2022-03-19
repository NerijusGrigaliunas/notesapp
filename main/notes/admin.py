
from django.contrib import admin
from.models import Note, Category, Profile
admin.site.register(Note)
admin.site.register(Category)
admin.site.register(Profile)


admin.site.site_header = 'Admin Panel'

