from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import EmailStore

# Create your views here.


def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        record = EmailStore()
        record.email = request.POST.get('email')
        record.name = request.POST.get('name')
        record.save()
        return HttpResponseRedirect('/list')
    return render(request, 'add.html')

def edit(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            record = EmailStore.objects.get(email=email)
            record.name = request.POST.get('name')
            record.is_edited = True
            record.save()
            return HttpResponseRedirect('/list')
    except:
        pass
    return render(request, 'edit.html', {})

def list_all(request):
    all_records = EmailStore.objects.all()
    return render(request, 'list.html', {'all_records':all_records})
    
def audit(request):
    all_records = EmailStore.objects.all()
    return render(request, 'audit.html', {'all_records':all_records})