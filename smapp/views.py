from django.shortcuts import render,HttpResponse
from .models import Lot
from .models import ip
import datetime

# Create your views here.
def home_page(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    get_ip= ip() #imported class from model
    get_ip.ip_address= ipaddress
    get_ip.pub_date = datetime.date.today() #import datetime
    get_ip.save()
    return render(request, 'smapp/home_page.html', {'ipsave': ipaddress,'ipnow':get_ip.ip_address })

def lot_details(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tracks=Lot.objects.filter(tracking_code__contains=searched)
        return render(request, 'smapp/lot_details.html', {'searched': searched,'tracks':tracks})
    else:
        return render(request, 'smapp/lot_details.html', {})
