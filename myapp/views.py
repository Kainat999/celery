from django.shortcuts import render
from celery_project.celery import add



# Enqueue Task using delay()
def index(request):
    print("Results: ")
    add.delay()
    return render(request, "myapp/index.html")


def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")