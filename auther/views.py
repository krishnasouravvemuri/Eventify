from django.shortcuts import render , redirect
from .forms import LoginForm , SignpForm
from django.contrib import messages
from django.contrib.auth import logout , authenticate, login
from .models import UserData
from hosts.models import EventDetails

def home(request):
    events = EventDetails.objects.all().order_by('-id')
    for event in events:
        event.remaining_seats = max(0, event.seats - event.registrations.count())
    return render(request, 'home.html', {'events': events})

def signup_user(request):
    if request.method == "POST":
        role = request.POST.get('role', '')
        signup_form = SignpForm(request.POST)

        if signup_form.is_valid():
            user = signup_form.save() 
            role = request.POST.get('role', '')
            company_name = request.POST.get('company_name', '')
            UserData.objects.create(user=user, company_name = company_name, role = role)            
            messages.success(request, "Success! Your account has been created.")
            if role == 'host':
                return redirect('hosts_home')
            elif role == 'member':
                return redirect('members_home')
            else:
                return redirect('home')
        else:
            messages.error(request , signup_form.errors)
    else:
        signup_form = SignpForm()
    
    return render(request, 'signup_user.html', {'form': signup_form})

def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            c =  request.POST.get('role').lower()
            user = authenticate(request, username=u, password=p)

            if user is not None:
                login(request, user)

                try:
                    userdata = UserData.objects.get(user=user)
                    user_role = userdata.role.lower()
                except UserData.DoesNotExist:
                    user_role = None

                if user_role == 'host' and c == 'host':
                    return redirect('hosts_home')
                elif user_role == 'member' and c == 'member':
                    return redirect('members_home')
                else:
                    messages.error(request, "Please Choose Correct Role")
                    return redirect('login_user')
            else:
                messages.error(request, "Invalid Credentials!")
        else:
            messages.error(request, "Please fill all required fields correctly.")
    else:
        login_form = LoginForm()

    return render(request, 'login_user.html', {'form': login_form})

def logout_user(request):    
    logout(request)
    messages.success(request , "Logged out Successfully !")
    return redirect('home') 


