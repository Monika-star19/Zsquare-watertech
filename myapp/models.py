from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class ServiceBooking(models.Model):
    SERVICE_CHOICES = [
        ('ro', 'Domestic RO Service'),
        ('industrial', 'Industrial Ro Service'),
        ('commercial', 'Commercial Ro Service'),
        ('conditioner', 'Water Conditioner Service'),
        ('softner', 'Water Softener Service'),
        ('presure', 'Pressure Pump Service'),
        ('heat', 'Heat Pump Service'),
        ('pool', 'Swimming Pool Filtration Service'),
        ('ionizer', 'Water Ionizer Service'),
        ('rain', 'Rain Water Harvesting Service'),
        ('etp/stp', 'ETP/STP Service'),
        ('amc', 'AMC Service'),
    ]

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.get_service_display()}"


class ProductInquiry(models.Model):
    PRODUCT_CHOICES = [
        ('domestic', 'Domestic RO'),
        ('commercial', 'Commercial RO'),
        ('commercial1', 'Commercial RO Plant Capacity 100 LPH'),
        ('commercial2', 'Commercial RO Plant Capacity 200 LPH'),
        ('commercial3', 'Commercial RO Plant Capacity 250 LPH'),
        ('industrial', 'Industrial RO'),
        ('industrial1', 'Industrial RO Plant Capacity upto 500 LPH'),
        ('industrial2', 'Industrial RO Plant Capacity upto 1000 LPH'),
        ('industrial3', 'Industrial RO Plant Capacity upto 6000 LPH'),
        ('watersoft', 'Water Softner'),
        ('waterconditioner', 'Water Conditioner'),
        ('pressure', 'Pressure Pump'),
        ('pool', 'Swimming Pool Filtration Equipments'),
        ('sewage', 'Sewage Treatment'),
        ('rainwater', 'Rain Water Harvesting'),
        ('heatpump', 'Heat Pump'),
    ]

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    product = models.CharField(max_length=50, choices=PRODUCT_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.product}"
