from django.http import HttpResponse


def index(request):
    return HttpResponse("datos_integrados")