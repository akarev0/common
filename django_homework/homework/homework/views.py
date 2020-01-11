from django.http import HttpResponse


def health_check(request):
    return HttpResponse("OK")


def some_another_url():
    return 1
