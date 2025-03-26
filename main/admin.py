from django.contrib import admin

# Register your models here.
from .models import FeedBackModel

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'message')

admin.site.register(FeedBackModel, FeedbackAdmin)