from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = 'id','name',
    ordering = '-id',


@admin.register(models.Contact)
class AdminContact(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id','first_name','last_name','phone',
    list_per_page = 10
    list_max_show_all = 200
    # list_editable = 'first_name',
    list_display_links = 'id','first_name','phone',