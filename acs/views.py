from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from acs.backend import OfferingAH


def index(request):
    context = {}
    return render(request, 'acs/index.html', context)


def results(request):
    offerings = []
    object1 = OfferingAH()
    if request.GET['availability'] == '1':
        offerings = object1.get_all_offerings()

    if not offerings:
        return render(request, 'acs/results.html', {})

    return render(request, 'acs/results.html', {'offerings': offerings})


def offeringdetail(request):
    raise Http404("detail does not exist")

    return render(request, 'polls/detail.html', {'question': question})

