from django.shortcuts import render
from companyapp.models import companydb
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def Company(request):
    return render(request,'companydetails.html')
def getdata(request):
    if request.method == 'POST':
        img_a = request.FILES['abc']
        name_a = request.POST.get('name')
        location_a = request.POST.get('location')
        number_a = request.POST.get('number')
        data = companydb(name=name_a,location=location_a,number=number_a,abc=img_a)
        data.save()
    return redirect('Company')
def viewcompany(request):
    obj = companydb.objects.all()
    return render(request,'viewcompanydetails.html',{'obj':obj})
def edit(request,id):
    obj = companydb.objects.filter(id=id)
    return render(request, 'edit.html',{'obj':obj})

def update(request,id):
    if request.method == 'POST':
        name_c = request.POST.get('name')
        location_c = request.POST.get('location')
        number_c = request.POST.get('number')
        try:
            image_c=request.FILES['abc']
            fs = FileSystemStorage() 
            file = fs.save(image_c.name, image_c)
        except MultiValueDictKeyError:
            file=companydb.objects.get(id=id).abc  
    companydb.objects.filter(id=id).update(name=name_c,location=location_c,number=number_c,abc=file)
    return redirect('Company')
def delete(request,id):
    companydb.objects.get(id=id).delete()
    return redirect('Company')