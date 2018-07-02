from django.contrib import admin

from . import models

admin.site.register(models.AppUsers)
admin.site.register(models.Applications)
admin.site.register(models.Files)
admin.site.register(models.Periods)
