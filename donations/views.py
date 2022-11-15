from django.shortcuts import render

# Create your views here.
def donate(request):
    return render(request,'donate.html')

def receive(request):
    return render(request,'receive.html')