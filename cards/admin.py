from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'email',
        'uid',
        'created_at',
    )
    search_fields = ('name', 'phone_number', 'email')
