from django.contrib import admin
from .models import Contact_us
from .models import ServiceBooking, ProductInquiry

# Register your models here.
admin.site.register(Contact_us)
admin.site.register(ServiceBooking)
admin.site.register(ProductInquiry)