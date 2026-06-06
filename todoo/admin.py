from django.contrib import admin

from todoo.models import task

class taskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at', 'updated_at')
    search_fields = ('title',)

admin.site.register(task, taskAdmin)
