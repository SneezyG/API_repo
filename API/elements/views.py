from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from elements.models import Elements, AllElements, constants, users
from werkzeug.security import check_password_hash, generate_password_hash
import secrets, string
from elements.Mail import send, validate
import uuid


# import sentry_sdk





# home view
def index(request):
  return render(request, 'elements/index.html')

    

def verifyMail(request):
  if request.method == 'POST':
    mail = request.POST['mail']
    res = validate(mail)
    if res.status_code == 200:
      res = res.json()
      if res["score"] > 0.4:
        user = users.objects.create(mail=mail)
        user.save()
        obj = {
          "valid": True,
          "free": res["free"],
          "mail": mail,
        }
        return JsonResponse(obj)
      else:
       return HttpResponse("mail invalid", status=404)
    else:   
      return HttpResponse("can't validate mail, try again", status=400)
  return HttpResponse('request method not allow', status=405)
  

def create(request):
  if request.method == 'POST':
    mail = request.POST['mail']
    username = request.POST['username']
    password = generate_password_hash(request.POST['password'], "sha256")
    try:
      user = users.objects.get(mail=mail)
    except:
      return HttpResponse('mail invalid', status=404)
    if user:
      user.user = username
      user.password = password
      user.save()
      obj = {
        "username": username,
        "password": password,
        "mail": mail,
        "mugshot": "",
        "secretKey": "",
        "projectKey": "",
        "accAge": user.user_age,
        "projectName": "",
      }
      return JsonResponse(obj)
   
  return HttpResponse('request method not allow', status=405)


def createProject(request):
  if request.method == 'POST':
    mail = request.POST['mail'] 
    projectName = request.POST['projectName']
    try:
      user = users.objects.get(mail=mail)
    except:
      return HttpResponse('mail invalid', status=404)
    if user:
      obj = {
          "username": "",
          "password": "",
          "mail": mail,
          "mugshot": "",
          "secretKey": str(uuid.uuid4()),
          "projectKey": str(uuid.uuid4()),
          "accAge": "",
          "projectName": projectName,
        }
      user.secret_key = obj["secretKey"]
      user.project_key = obj["projectKey"]
      user.project_name = obj["projectName"]
      user.save()
      return JsonResponse(obj)
   
  return HttpResponse('request method not allow', status=405)
  

def shot(user):
  if user.mug_shot:
    return user.mug_shot.url
  else:
    return ""
    
    
def login(request):
  if request.method == 'POST':
    mail = request.POST['mail']
    password = request.POST['password']
    try:
      user = users.objects.get(mail=mail)
    except:
      return HttpResponse('mail invalid', status=404)
    if user:
      auth= check_password_hash(user.password, password)
      if auth:
          obj = {
            "username": user.user,
            "password": password,
            "mail": mail,
            "mugshot": shot(user),
            "secretKey": user.secret_key,
            "projectKey": user.project_key,
            "accAge": user.user_age,
            "projectName": user.project_name,
          }
          return JsonResponse(obj)
      else:
        return HttpResponse("invalid password", status=400)
  
  return HttpResponse('request method not allow', status=405)


def forgetPass(request):
  if request.method == 'POST':
    mail = request.POST['mail']
    try:
      user = users.objects.get(mail=mail)
    except:
      return HttpResponse('mail invalid', status=404)
    if user:
      newPass = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10)))
      res = send(user.user, newPass, mail)
      if res.status_code == 200:
        user.password = generate_password_hash(newPass, "sha256")
        user.save()
        #return HttpResponse("success")
        obj = {
          "status": "success",
          "newPass": newPass
        }
        return JsonResponse(obj)
      else:
        return HttpResponse("can't send mail, try again", status=400)
       
  return HttpResponse('request method not allow', status=405)
  

def changePass(request):
  if request.method == 'POST':
    mail = request.POST['mail']
    oldPass = request.POST['oldPass']
    newPass = generate_password_hash(request.POST['newPass'], "sha256")
    try:
      user = users.objects.get(mail=mail)
    except:
      return HttpResponse('mail invalid', status=404)
    if user:
      auth = check_password_hash(user.password, oldPass)
      if auth:
        user.password = newPass
        user.save()
        return HttpResponse("success")
      else:
        return HttpResponse("invalid password", status=400)
        
  return HttpResponse('request method not allow', status=405)

  

def upload(request):
  if request.method == 'POST':
    mail = request.POST['mail']
    mugshot = request.FILES['mugshot']
    try:
      user = users.objects.get(mail=mail)
    except:
      return HttpResponse('mail invalid', status=404)
    if user:
      user.mug_shot = mugshot
      user.save()
      return HttpResponse("success")

  return HttpResponse('request method not allow', status=405)
  
  
