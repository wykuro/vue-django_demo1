from django.shortcuts import render, redirect
from myblog.models import SiteInfo, Classes, Userinfo
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def index(request):
    siteinfo = SiteInfo.objects.all()[0]
    classes = Classes.objects.all()
    userlist = Userinfo.objects.all()
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist
    }
    return render(request, 'index.html', data)


def classes(request):
    siteinfo = SiteInfo.objects.all()[0]
    classes = Classes.objects.all()
    try:
        choosed_id = request.GET['id']
        print(choosed_id)
        choosed = Classes.objects.filter(id=choosed_id).first()
    except:
        return redirect("/")
    if choosed:
        userlist = Userinfo.objects.filter(belong=choosed)
    else:
        userlist = []
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist
    }
    return render(request, 'classes.html', data)
