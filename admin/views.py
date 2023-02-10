from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.http import JsonResponse
from home.models import RegistrationForm
# Create your views here.
def admin_login(request):
    if 'admin_login' not in request.session:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            check_user = User.objects.filter(username=username).exists()
            if check_user:
                user = auth.authenticate(username=username,password=password)
                if user:
                    request.session['admin_login'] = username
                    return JsonResponse(
                        {'success':'true'},
                        safe=False
                    )   
                else:
                    return JsonResponse(
                        {'success':'incorrect_password'},
                        safe=False
                    )
            else:
                return JsonResponse(
                    {'success':'incorrect_username'},
                    safe=False
                )
        elif request.method == 'GET':
            return render(request,'admin_login.html')
    else:
        return redirect('/admin/admin_home')

def admin_home(request):
    if 'admin_login' in request.session:
        data = RegistrationForm.objects.all()
        return render(request,'admin_home.html',{'data':data})
    else:
        return redirect('/admin/')

def admin_logout(request):
    try:
        del request.session['admin_login']
        return redirect('/admin/')
    except KeyError:
        return redirect('/admin/')