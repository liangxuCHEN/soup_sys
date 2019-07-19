from django.contrib import admin

# Register your models here.
from today_soup.models import SoupModel

class SoupAdmin(admin.ModelAdmin):
    list_display = ('id','title','created')


admin.site.register(SoupModel, SoupAdmin)