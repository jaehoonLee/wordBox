# Create your views here.
from django.http import *
from django.shortcuts import * 
from main.forms import *

def main_page(request):
    return render_to_response('main_page.html', {'form' : LoginForm});
















