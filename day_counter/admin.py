from django.contrib import admin

from day_counter.models import Counter


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    readonly_fields = ['guid']
    list_display = ('id', 'title', 'user')
