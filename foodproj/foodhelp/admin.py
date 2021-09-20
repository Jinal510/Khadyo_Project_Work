from django.contrib import admin
from .models import*
# Register your models here.

class foodhelperAdmin(admin.ModelAdmin):
    list_display=('name','lastname','contact','city','area')
    list_display_links=("name",)
    list_editable=('city','area')
    list_per_page=5
    search_fields=('name',)
    list_filter=('city','area')

class NgoAdmin(admin.ModelAdmin):
    list_display=('name','contact','area','address')
    list_display_links=("name",'address')
    list_editable=('area',)
    list_per_page=5
    search_fields=('name',)
    list_filter=('area',)

admin.site.register(User)
admin.site.register(foodhelper,foodhelperAdmin)
admin.site.register(UserRole)
admin.site.register(AddFood)
admin.site.register(NGO,NgoAdmin)
admin.site.register(Feedback)
admin.site.register(Transaction)