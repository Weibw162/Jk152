import json

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import Img, Per, PerLike


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    username = ''
    password = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    per = Per.objects.filter(username=username, password=password)

    if per.exists():
        request.session["username"] = username
        return HttpResponseRedirect('/show/1')
    else:
        return HttpResponse("傻逼！这都能写错？退回去重新登录！！！！")


def show(request, Img_id):
    per = Per.objects.filter(username=request.session["username"])
    img = Img.objects.filter(sn=Img_id)
    like = 0
    like_list = []
    if per.exists() | img.exists():
        per = per[0]
        img = img[0]
    perlike = PerLike.objects.filter(per=per, img=img)
    if perlike.exists():
        like = 1
    else:
        like = 0
    perlike_list = PerLike.objects.filter(per=per)
    if perlike_list.exists():
        for item in perlike_list:
            like_list.append(item.img.sn)

    context = {
        "img_id": Img_id,
        "img_count": [i + 1 for i in range(428)],
        "like": like,
        "like_list": like_list,
        "like_count":len(like_list),
    }

    return render(request, 'show.html', context)


@csrf_exempt
def like(request, Img_id):
    per_username = request.session["username"]

    img = Img.objects.filter(sn=Img_id)
    per = Per.objects.filter(username=per_username)
    if img.exists() | per.exists():
        img = img[0]
        per = per[0]

    perlike = PerLike.objects.filter(img=img, per=per)
    if perlike.exists():
        perlike.delete()
        img.like_num -= 1
        img.save()
        return HttpResponse("0")

    else:
        perlike_list = PerLike.objects.filter(per=per)
        if len(perlike_list) >= 5:
            return HttpResponse("3")
        perlike = PerLike()
        perlike.img = img
        perlike.per = per
        perlike.save()
        img.like_num += 1
        img.save()
        return HttpResponse("1")
