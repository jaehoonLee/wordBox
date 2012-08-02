# Create your views here.
from django.http import *
from django.shortcuts import * 
from account.forms import *

def main_page(request):
    return render_to_response('login_page.html', {'form' : LoginForm});













