from django.template.response import TemplateResponse
from .models import User

def index(request):
    
    if request.method == "POST":
        user, created = User.objects.get_or_create(name = request.POST.get("name"))
        data = {"person": user.name}
        return TemplateResponse(request, "index.html",data)
    else: 
        data = {"person": ""}
        return TemplateResponse(request, "index.html")
