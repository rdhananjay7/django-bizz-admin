from django.shortcuts import render  # render a template
from django.http import HttpResponse
from listings.choices import category_choices, city_choices

from listings.models import Listing
from teammembers.models import Team

# Create your views here.


def index(request):

    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'category_choices': category_choices,
        'city_choices' : city_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    members = Team.objects.filter(is_employed=True)
    context = {
        'team': members,
    }
    return render(request, 'pages/about.html', context)
