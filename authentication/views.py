from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.core.mail import send_mail


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            getmail = User.objects.get(username=username)
            mail1 = getmail.email
            print(type(mail1))

            # Corrected order and removal of trailing commas
            subject = 'Notification'
            message = 'You are logged in'
            email_from = 'mohan638010@gmail.com'
            recipient_list = [mail1]

            send_mail(subject, message, email_from, recipient_list)  # Correct order

            return redirect('index')


           

            
            # mail = getmail.email
            
            # print(getmail.id)
            # print(getmail.username)
            # print(getmail.email)
           


            

            # return redirect('index')
        
        else:
            context = {
                'error' : '* Invalid username or password'
            }

            return render(request,'login.html',context)



    return render(request,'login.html')

def logoutpage(request):

    del_user = request.user

    logout(request)

    del_user.delete()

def sigpage(request):

    if request.method == 'POST':

        user_check = User.objects.filter(username = request.POST['name'])

        if len(user_check) > 0 :

            context = {
                'error' : "* username already exist"
            }

            return render(request,'signup.html',context)
        
        else:

            username = request.POST['name']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            mail = request.POST['mail']
            

            new_user = User(username = username, first_name = firstname, last_name = lastname, email = mail)

            new_user.set_password(request.POST['pass'])

            new_user.save()

            return redirect('/')

    return render(request,'signup.html')



   

    
