from django.http import HttpResponse


def DashboadView(request):
    return HttpResponse("<h1>Welcome to swifthub Dashboard.</h1>")