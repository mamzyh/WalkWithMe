from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from app1.models import LogMessage
from app1.forms import LogForm

def home(request):
    return render(request, "home.html")

def hello1(request, name):
    return HttpResponse(f"Hello there, {name}")

def hello2(request, name):
    return render(request, "hello.html", {
        'name': name,
        'date': datetime.now()
    })

def addMessage(request):
    form = LogForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.save()
        return redirect("show")
    return render(request, "logMessage.html", {"form": form})

def showMessages(request):
    messages = LogMessage.objects.order_by("-log_date")
    return render(request, "showMessages.html", {
        "message_list": messages
    })
