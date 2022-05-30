from django.contrib import admin

from listings.models import User
from listings.models import Project
admin.site.register(User)
admin.site.register(Project)
