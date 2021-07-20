from get_print.models import Consumer, Part
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

# Register your models here.
admin.site.register(Part)
admin.site.register(Consumer)