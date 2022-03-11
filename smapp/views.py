from django.shortcuts import render,HttpResponse
from .models import Lot
from .models import ip


# Create your views here.


def home_page(request):
    first_ip=request.META.get('REMOTE_ADDR')
    return render(request, 'smapp/home_page.html', {'ip1':first_ip})

def lot_details(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tracks=Lot.objects.filter(tracking_code__contains=searched)
        return render(request, 'smapp/lot_details.html', {'searched': searched,'tracks':tracks})
    else:
        return render(request, 'smapp/lot_details.html', {})
