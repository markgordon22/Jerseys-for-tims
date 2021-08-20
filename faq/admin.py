from django.contrib import admin
from .models import Faq

# Register your models here.


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'date',
    )


admin.site.register(Faq, FaqAdmin)
