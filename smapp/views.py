from django.shortcuts import render,get_object_or_404
from .models import Lot
from ipware import get_client_ip

# Create your views here.
def home_page(request):

    ip, is_routable = get_client_ip(request)

    if ip is None:
        ip='0.0.0.0'
    else:
        if is_routable:
            ipv='Public'
        else:
            ipv='Private'
    print(ip,ipv)

    return render(request,'smapp/home_page.html')

def lot_details(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tracks=Lot.objects.filter(tracking_code__contains=searched)
        return render(request, 'smapp/lot_details.html', {'searched': searched,'tracks':tracks})
    else:
        return render(request, 'smapp/lot_details.html', {})