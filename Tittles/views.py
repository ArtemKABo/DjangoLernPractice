from django.template.response import TemplateResponse
from .models import User

def index(request):
    
    if request.method == "POST":
        n = request.POST.get("name")
        if n=="":
            data ={"error": "Не указано имя пользователя", "person": ""}
        else:
            user, created = User.objects.get_or_create(name = n)
            data = {"person": user.name}
        return TemplateResponse(request, "index.html",data)
    else: 
        data = {"person": ""}
        return TemplateResponse(request, "index.html")
