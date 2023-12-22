from django.contrib import admin
from .models import Ref, resume
# Register your models here.

class imageAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "image"] 

admin.site.register(Ref, imageAdmin)
admin.site.register(resume)