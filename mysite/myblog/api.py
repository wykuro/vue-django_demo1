from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from myblog.models import Classes, Userinfo, SiteInfo
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from myblog.tojosn import Classes_data, Userinfo_data
import json


@api_view(['GET', 'POST'])
def api_test(request):
    classes = Classes.objects.all()
    # print(classes)
    # classes_data = Classes_data(classes, many=True)
    # userlist = Userinfo.objects.all()
    # userlist_data = Userinfo_data(userlist, many=True)
    # data = {
    #     'classes': classes_data.data,
    #     'userinfo': userlist_data.data
    # }
    data = {
        'classes': []
    }
    for c in classes:
        data_item = {
            'id': c.id,
            'text': c.text,
            'userlist': []
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                'id': user.id,
                'nickName': user.nickName,
                'headImg': str(user.headImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
        # data = json.dump(data)
    return Response(data)


@api_view(['GET', 'POST'])
def getmenulist(request):
    allClasses = Classes.objects.all()
    siteinfo = SiteInfo.objects.get(id=1)
    siteinfo_data = {
        'sitename': siteinfo.title,
        'logo': "http://127.0.0.1:9000/upload/"+str(siteinfo.logo)
    }
    menu_data = []
    for c in allClasses:
        data_item = {
            'id': c.id,
            'text': c.text
        }
        menu_data.append(data_item)
    data = {
        'menu_data': menu_data,
        'siteinfo': siteinfo_data
    }
    return Response(data)


@api_view(['GET', 'POST', 'DELETE'])
def getuserlist(request):
    if(request.method == 'DELETE'):
        user_id = request.POST['id']
        deleteuser = Userinfo.objects.get(id=user_id)
        deleteuser.delete()
        return Response("ok")
    menuId = request.GET['id']
    menu = Classes.objects.get(id=menuId)
    userlist = Userinfo.objects.filter(belong=menu)
    data = []
    for user in userlist:
        data_item = {
            'id': user.id,
            'headimg': str(user.headImg),
            'nickname': user.nickName
        }
        data.append(data_item)
    return Response(data)


@api_view(['POST'])
def tologin(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)
    user = User.objects.filter(username=username)
    if len(user) > 0:
        user_pwd = user[0].password
        auth_pwd = check_password(password, user_pwd)
        if auth_pwd:
            token = Token.objects.update_or_create(user=user[0])
            token = Token.objects.get(user=user[0])
            print(token.key)
            userinfo = Userinfo.objects.get(belong_user=user[0])
            print(userinfo)
            data = {
                'token': token.key,
                'userinfo': {
                    'id': userinfo.id,
                    'nickname': userinfo.nickName,
                    'headimg': str(userinfo.headImg)
                }
            }
            return Response(data)
        else:
            return Response("err")
    else:
        return Response("none")
    return Response("ok")


@api_view(['POST'])
def toregister(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    user = User.objects.filter(username=username)
    if user:
        return Response("same")
    else:
        newpwd = make_password(password, username)
        newUser = User(username=username, password=newpwd)
        newUser.save()
    return Response('ok')


@api_view(['POST', 'PUT'])
def uploadlogo(request):
    if(request.method == 'PUT'):
        sitename = request.POST['sitename']
        old_info = SiteInfo.objects.get(id=1)
        old_info.title = sitename
        new_info = SiteInfo.objects.get(id=2)
        old_info.logo = new_info.logo
        old_info.save()
        return Response('ok')
    img = request.FILES['logo']
    print(img)
    test_sitelogo = SiteInfo.objects.get(id=2)
    print(test_sitelogo)
    test_sitelogo.logo = img
    test_sitelogo.save()
    data = {
        'img': str(test_sitelogo.logo)
    }
    return Response(data)
