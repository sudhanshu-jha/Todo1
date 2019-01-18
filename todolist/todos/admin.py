from django.contrib import admin

# Register your models here.

from .models import Todo

# from .models import Test


class TodoAdmin(admin.ModelAdmin):

    search_fields = ["Title"]

    fieldsets = [
        ("user", {"fields": ["user"]}),
        ("Title", {"fields": ["Title"]}),
        ("Description", {"fields": ["Description"]}),
    ]
    list_filter = ["user"]


admin.site.register(Todo, TodoAdmin)
