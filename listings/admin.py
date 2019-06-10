from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'is_published',
                    'city', 'category', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'city')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', )
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
