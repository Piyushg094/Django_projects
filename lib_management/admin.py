from django.contrib import admin
# Register your models here.
from .models import *

# @admin.register(Author)

    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','email',"phone","roles"]

@admin.register(BookDetail)
class BookDetailAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(BookRecord)
class BoolRecordAdmin(admin.ModelAdmin):
    list_display=['book',"edition","count","price","available","category"]

@admin.register(IssueRecord)
class IssueRecordAdmin(admin.ModelAdmin):
    list_display=['user','book','status','issue_date',"return_date","fine"]

