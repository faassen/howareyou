from django.http import HttpResponse


def welcome(request, name):
    return HttpResponse("User: %s" % name)
