from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(donor_table)
admin.site.register(volunteer_table)
admin.site.register(donate_items_details)