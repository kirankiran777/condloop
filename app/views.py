from django.shortcuts import render

# Create your views here.
def cond(request):
    d={'a':3000,'b':2000,'c':300}
    return render(request,'cond.html',d)


def loop(request):
    d={'name':'THOR'}
    return render(request,'loop.html',d)
