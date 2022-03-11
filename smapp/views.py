from django.shortcuts import render,HttpResponse
from .models import Lot
from .models import ip


# Create your views here.
def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    get_ip= ip()
    get_ip.ip_address= ipaddress
    get_ip.save()
    return ipaddress

def home_page(request):
    first_ip=client_ip(request)
    second_ip=request.META.get('REMOTE_ADDR')
    return render(request, 'smapp/home_page.html', {'ip1':first_ip,'ip2':second_ip})

def lot_details(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tracks=Lot.objects.filter(tracking_code__contains=searched)
        return render(request, 'smapp/lot_details.html', {'searched': searched,'tracks':tracks})
    else:
        return render(request, 'smapp/lot_details.html', {})
