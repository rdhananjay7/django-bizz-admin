from django.shortcuts import render  # render a template
from django.http import HttpResponse

from listings.models import Listing
from teammembers.models import Team

# Create your views here.


def index(request):

    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    members = Team.objects.filter(is_employed=True)
    context = {
        'team': members,
    }
    return render(request, 'pages/about.html', context)
