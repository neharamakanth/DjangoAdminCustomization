from django.contrib import admin
from .models import Customer,Movies

class MoviesAdmin(admin.ModelAdmin):
#for changing the display order
    fields=['release_year','title','length']

# for searching based on specific fields
    search_fields=['title']

#for adding filters based on which u can sort items in the model
    list_filter=['length','release_year']

#for displaying movies in the form of list
    list_display=['title','length']

#for making fields ediatble in list first they should be in above list_display attribute and then
    list_editable=['length']




class CustomerAdmin(admin.ModelAdmin):
#for changing the display order
    fields=['phone_number','first_name','last_name']

# for searching based on specific fields
    search_fields=['phone_number']

    list_filter=['phone_number']

    list_display=['first_name','last_name','phone_number']

    list_editable=['phone_number']



# Register your models here.
admin.site.register(Movies,MoviesAdmin)
admin.site.register(Customer,CustomerAdmin)
