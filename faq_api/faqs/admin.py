from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',) # Only display the 'question' field
    search_fields = ('question', 'answer')
