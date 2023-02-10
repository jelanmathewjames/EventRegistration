from django.shortcuts import render, redirect
from django.http import JsonResponse
from home.models import RegistrationForm, EventScheduler

# Create your views here.
def home(request):
    schedule = EventScheduler.objects.filter(event_name='online_coding_event').first() 
    data = schedule.event_data_time
    return render(request,'home.html',{'data':data})

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        education_status = request.POST['education_status']
        institution = request.POST['institution']
        check_email = RegistrationForm.objects.filter(email=email).exists()
        check_phone_number = RegistrationForm.objects.filter(phone_number=phone_number).exist()
        if check_email:
            return JsonResponse(
                {'success':'email_exist'},
                safe = False
            )
        elif check_phone_number:
            return JsonResponse(
                {'success':'phone_number_exist'},
                safe = False
            )
        else:
            register = RegistrationForm.objects.create(name=name,email=email,phone_number=phone_number,
                                                        current_education=education_status,institution=institution)
            register.save()
            return JsonResponse(
                {'success':'true'},
                safe = False
            )                      
    elif request.method == 'GET':
        return render(request,'registration.html')
