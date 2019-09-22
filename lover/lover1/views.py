from django.shortcuts import render
from .models import LoverData
from .forms import LovesForm
from django.http.response import HttpResponse

def love_view(request):
    return render(request,'love.html')
def lover_view(request):
    if request.method=="POST":
        lform=LovesForm(request.POST)
        if lform.is_valid():
            boyfrnd_name=request.POST.get('boyfrnd_name','')
            girlfrnd_name=request.POST.get('girlfrnd_name','')
            data=LoverData(
                boyfrnd_name=boyfrnd_name,
                girlfrnd_name=girlfrnd_name,
            )
            data.save()
            return HttpResponse('Data is Inserted')
        else:
            return HttpResponse('Data is not inserted')
    else:
        lform=LovesForm()
        return render(request,'lover.html',{'lform':lform})
