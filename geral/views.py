from django.contrib.auth.decorators import login_required
import requests

@login_required
def TestAuth(request):
    return "Entrou"