from django.contrib import admin
from .models import Tasks

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("task", "desc", "status", )


admin.site.register(Tasks, MemberAdmin)