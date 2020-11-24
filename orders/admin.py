from django.contrib import admin
from .models import Hire, HireElement


class HireAdmin(admin.ModelAdmin):
    list_display = ['hirer', 'taking_date', 'return_date', 'cost', 'paid']
    prepopulated_fields = {'slug': ('hirer', 'cost',)}
admin.site.register(Hire, HireAdmin)


class HireElementAdmin(admin.ModelAdmin):
    list_display = ['product', 'number', 'hire']
    list_filter = ['hire']
    prepopulated_fields = {'slug': ('product', 'number')}
admin.site.register(HireElement, HireElementAdmin)