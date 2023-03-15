from django.shortcuts import render

# Create your views here.
def csk(request):
    return render(request,'csk.html')



def rcb(request):
    return render(request,'rcb.html')