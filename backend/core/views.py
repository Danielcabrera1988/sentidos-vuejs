from django.shortcuts import render
from django.views.generic import TemplateView

class HomeRest(TemplateView):
    template_name = "home-Rest.html"
