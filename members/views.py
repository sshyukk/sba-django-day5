from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.

def index(req):
    print(dir(req))
    return HttpResponse("hello")

def test(req):
    return HttpResponse("Test")

def test2(req):
    return HttpResponse("Test2")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']

        # if username == 'exit' :
        #     return HttpResponse("<h2> 나가기 </h2>")
        # elif username == 'codingon' :
        #     return render(req, 'login.html')
        
        member = Members(
            username = username,
            useremail = email
        )

        member.save()
        res_data = {}
        res_data['res'] = '등록성공'
        return render(req, 'index.html', res_data)

    return render(req, 'index.html')


