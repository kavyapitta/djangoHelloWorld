from django.http import HttpResponse

def helloWorldView(request):
    return HttpResponse('Hello World!')
