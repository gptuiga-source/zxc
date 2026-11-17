from django.shortcuts import render, redirect
from .models import Count
from .password import check_password

def index(request):
    if request.method == "GET":
        Count.objects.create()
    else:
        return redirect("password")
    count = len(Count.objects.all())
    return render(request, "index.html", {"count": count})




def clear_date(request):
    verify_password = check_password()
    if request.method == "POST":
        input_password = request.POST.get("input-password", "")
        if verify_password == input_password:
            Count.objects.all().delete()
            return redirect("index")
        else:
            error = "Неверный пароль"
    else:
        error = ""
    return render(request, "password.html", {"error": error})
