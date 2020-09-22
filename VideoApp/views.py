from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={'text':'capitalize me','number':150}
    return render(request,'VideoApp/index.html',context=my_dict)

def other(request):
    return render(request,'VideoApp/other.html')

def relative_urls(request):
    return render(request,'VideoApp/relative_urls.html')
