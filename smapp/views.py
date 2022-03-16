from django.shortcuts import render,redirect,get_object_or_404
from .models import Lot
from .models import ip
from .forms import LotForm


# Create your views here.
def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    get_ip=ip()
    get_ip.ip_address=ipaddress
    get_ip.save()
    return get_ip.ip_address

def home_page(request):
    current_ip=client_ip(request)
    old_ip=ip.objects.all()
    penultimate_index=len(old_ip)-2
    old_ip=old_ip[penultimate_index].ip_address
    return render(request, 'smapp/home_page.html', {'ip1':current_ip,'ip2':old_ip})

def lot_details(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tracks=Lot.objects.filter(tracking_code__contains=searched)
        return render(request, 'smapp/lot_details.html', {'searched': searched,'tracks':tracks})
    else:
        return render(request, 'smapp/lot_details.html', {})

def lots_list(request):
    lots=Lot.objects.all()
    return render(request, 'smapp/lots_list.html',{'lots':lots})

def single_lot(request,pk):
    lot=get_object_or_404(Lot,pk=pk)
    return render(request, 'smapp/single_lot.html',{'lot':lot})

def new_lot(request):
    if request.method=="POST":
        form=LotForm(request.POST)
        if form.is_valid():
            lot=form.save(commit=False)
            lot.author=request.user
            if not lot.hash:
                lot.writeOnChain()
            lot.save()
            return redirect('lots_list')
    else:
        form=LotForm()
    return render(request, 'smapp/new_lot.html',{'form':form})

def lot_edit(request,pk):
    lot=get_object_or_404(Lot,pk=pk)
    if request.method == "POST":
        form = LotForm(request.POST,instance=lot)
        if form.is_valid():
            lot = form.save(commit=False)
            lot.author = request.user
            lot.save()
            return redirect('lots_list')
    else:
        form = LotForm(instance=lot)
    return render(request, 'smapp/lot_edit.html', {'form': form})

