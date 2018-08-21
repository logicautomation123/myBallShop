from django.shortcuts import render
# Create your views here.
def hello_view(request):
    from django.http import HttpResponse
    return HttpResponse("Hello,Django!")