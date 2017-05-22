from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from models import User
from django.shortcuts import redirect


# Create your views here.
def login(request):
    # context = {}
    # return render(request, 'login.html', context)
    return render_to_response("login.html")
    # return HttpResponse(json.dumps(result))


def logout(request):
    is_login = request.session.get('ex_user', None)
    if is_login:
        del request.session['ex_user']
        return redirect('login')
    return HttpResponse('404')


@csrf_exempt
def checkuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                op = "0"  # stand for "success
                request.session['ex_user'] = username
            elif user.password != password:
                op = "1"  # stand for "password not correct"

        except User.DoesNotExist:
            op = "-1"  # stand for "user not existed"
        result = {
            "msg": op
        }
        return HttpResponse(json.dumps(result))


def registration(request):
    return render_to_response("registration.html")


@csrf_exempt
def register(request):
    fullname = request.POST["fullname"]
    address = request.POST["address"]
    email = request.POST["email"]
    city = request.POST["city"]
    sexradio = request.POST["sexradio"]
    username = request.POST["username"]
    password = request.POST["password"]
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
            msg = "-1"  # stand for username existed...
        except User.DoesNotExist:
            user = User()
            user.fullname = fullname
            user.address = address
            user.email = email
            user.city = city
            user.sex = sexradio
            user.username = username
            user.password = password
            try:
                user.save()
                msg = "1"  # stand for register successed...
            except Exception as e:
                msg = "2"  # stand for insert failed
                print e.message

        result = {
            "msg": msg
        }
    return HttpResponse(json.dumps(result))
