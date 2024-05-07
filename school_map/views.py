from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, LoginForm  # Import your custom signup and login forms
from django.contrib import messages
from django.shortcuts import render
from .models import RoomInput



def authentication(request):
    if request.user.is_authenticated:
        return redirect('school_map:room_input')
    else:
        return redirect('school_map:login')

def index(request):
    return render(request, 'school_map/floor1.html')

def user_signup(request):
  if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
          user = form.save()  
          login(request, user)  
          return redirect('school_map:room_input') 
      else:
          error_message = "There was an error with your signup. Please correct the errors below."
          return render(request, 'school_map/SSignUp.html', {'form': form, 'error_message': error_message})
  else:
      form = SignupForm()
  return render(request, 'school_map/SSignUp.html', {'form': form})

def user_login(request):
  if request.user.is_authenticated:
    
    return redirect('school_map:room_input')

  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
      
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)    
            return redirect('school_map:room_input') 
        else:
            error_message = "Invalid username or password. Please try again."
            messages.error(request, error_message)
            return render(request, 'school_map/SLogin.html', {'form': form, 'error_message': error_message})
  else:
    form = LoginForm()
  return render(request, 'school_map/SLogin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('school_map:login')

def room_input(request):
  if request.method == 'POST':
     
      room_input, created = RoomInput.objects.get_or_create(user=request.user)
      room_input.day_a_period_1 = request.POST.get('day_a_period_1', 1000)
      room_input.day_a_period_2 = request.POST.get('day_a_period_2', 1000)
      room_input.day_a_period_3 = request.POST.get('day_a_period_3', 1000)
      room_input.day_a_period_4 = request.POST.get('day_a_period_4', 1000)
      room_input.day_b_period_1 = request.POST.get('day_b_period_1', 1000)
      room_input.day_b_period_2 = request.POST.get('day_b_period_2', 1000)
      room_input.day_b_period_3 = request.POST.get('day_b_period_3', 1000)
      room_input.day_b_period_4 = request.POST.get('day_b_period_4', 1000)

     
      room_input.save()

     
      return redirect('school_map:floor1')

  else:
    
      try:
          room_input = RoomInput.objects.get(user=request.user)
      except RoomInput.DoesNotExist:
        
          room_input = RoomInput.objects.create(user=request.user)

    
      default_values = {
          'day_a_period_1': room_input.day_a_period_1,
          'day_a_period_2': room_input.day_a_period_2,
          'day_a_period_3': room_input.day_a_period_3,
          'day_a_period_4': room_input.day_a_period_4,
          'day_b_period_1': room_input.day_b_period_1,
          'day_b_period_2': room_input.day_b_period_2,
          'day_b_period_3': room_input.day_b_period_3,
          'day_b_period_4': room_input.day_b_period_4,
      }

      
      return render(request, 'school_map/RoomInput.html', default_values)


def floor1(request):
  
  try:
      room_input = RoomInput.objects.get(user=request.user)
  except RoomInput.DoesNotExist:
   
      room_input = RoomInput.objects.create(user=request.user)

 
  context = {
      'day_a_period_1': room_input.day_a_period_1,
      'day_a_period_2': room_input.day_a_period_2,
      'day_a_period_3': room_input.day_a_period_3,
      'day_a_period_4': room_input.day_a_period_4,
      'day_b_period_1': room_input.day_b_period_1,
      'day_b_period_2': room_input.day_b_period_2,
      'day_b_period_3': room_input.day_b_period_3,
      'day_b_period_4': room_input.day_b_period_4,
  }

 
  return render(request, 'school_map/floor1.html', context)

def floor2(request):
 
  try:
      room_input = RoomInput.objects.get(user=request.user)
  except RoomInput.DoesNotExist:

      room_input = RoomInput.objects.create(user=request.user)


  context = {
      'day_a_period_1': room_input.day_a_period_1,
      'day_a_period_2': room_input.day_a_period_2,
      'day_a_period_3': room_input.day_a_period_3,
      'day_a_period_4': room_input.day_a_period_4,
      'day_b_period_1': room_input.day_b_period_1,
      'day_b_period_2': room_input.day_b_period_2,
      'day_b_period_3': room_input.day_b_period_3,
      'day_b_period_4': room_input.day_b_period_4,
  }


  return render(request, 'school_map/floor2.html', context)

def floor3(request):

  try:
      room_input = RoomInput.objects.get(user=request.user)
  except RoomInput.DoesNotExist:

      room_input = RoomInput.objects.create(user=request.user)

 
  context = {
      'day_a_period_1': room_input.day_a_period_1,
      'day_a_period_2': room_input.day_a_period_2,
      'day_a_period_3': room_input.day_a_period_3,
      'day_a_period_4': room_input.day_a_period_4,
      'day_b_period_1': room_input.day_b_period_1,
      'day_b_period_2': room_input.day_b_period_2,
      'day_b_period_3': room_input.day_b_period_3,
      'day_b_period_4': room_input.day_b_period_4,
  }


  return render(request, 'school_map/floor3.html', context)

def floor4(request):
 
  try:
      room_input = RoomInput.objects.get(user=request.user)
  except RoomInput.DoesNotExist:
  
      room_input = RoomInput.objects.create(user=request.user)

 
  context = {
      'day_a_period_1': room_input.day_a_period_1,
      'day_a_period_2': room_input.day_a_period_2,
      'day_a_period_3': room_input.day_a_period_3,
      'day_a_period_4': room_input.day_a_period_4,
      'day_b_period_1': room_input.day_b_period_1,
      'day_b_period_2': room_input.day_b_period_2,
      'day_b_period_3': room_input.day_b_period_3,
      'day_b_period_4': room_input.day_b_period_4,
  }


  return render(request, 'school_map/floor4.html', context)

def floor5(request):
 
  try:
      room_input = RoomInput.objects.get(user=request.user)
  except RoomInput.DoesNotExist:
 
      room_input = RoomInput.objects.create(user=request.user)


  context = {
      'day_a_period_1': room_input.day_a_period_1,
      'day_a_period_2': room_input.day_a_period_2,
      'day_a_period_3': room_input.day_a_period_3,
      'day_a_period_4': room_input.day_a_period_4,
      'day_b_period_1': room_input.day_b_period_1,
      'day_b_period_2': room_input.day_b_period_2,
      'day_b_period_3': room_input.day_b_period_3,
      'day_b_period_4': room_input.day_b_period_4,
  }


  return render(request, 'school_map/floor5.html', context)
