from django.shortcuts import render,redirect
from .models import Contact_us
from .models import ServiceBooking
from .models import ProductInquiry


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('mobile')
        message = request.POST.get('message')

        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()
        return redirect('home')
    return render(request,'contact.html')


def service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        service_choice = request.POST.get('service')

        print(name, mobile)

        service_booking = ServiceBooking(
            name=name,
            mobile=mobile,
            service=service_choice,
        )

        service_booking.save()
        return redirect('booking_success')

    return render(request, 'services.html')

def booking_success(request):
    return render(request, 'booking_success.html')

def products(request):
    return render(request,'products.html')

def inquiry_success(request):
    return render(request, 'inquiry_success.html')


def inquery(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        product = request.POST.get('Product')

        # Create a new ProductInquiry object and save it to the database
        inquiry = ProductInquiry(name=name, mobile=mobile, product=product)
        inquiry.save()

        return redirect('inquiry_success')  # Redirect to a success page

    return render(request,'inquery.html')


