from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

# Create your views here.
 
def register(request):
    user1 = User()
    user1.username = 'pranshu'
    user1.password = 'pranshu'

    user2 = User()
    user2.username = 'x'
    user2.password = 'x'

    users = [user1,user2]

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user3 = User()
        user3.username = username
        user3.password = password
        users.append(user3)
        print(users)
        messages.info(request,username)
        return redirect('/')
    else:
        return render(request,'index.html')


