from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm, ChalanForm
from .models import Vehicle, Chalan

def homePage(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vehicle_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user
            vehicle.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'register_vehicle.html', {'form': form})

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

@login_required
def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'edit_vehicle.html', {'form': form})

@login_required
def add_chalan(request):
    if request.method == 'POST':
        form = ChalanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chalan_list')
    else:
        form = ChalanForm()
    return render(request, 'add_chalan.html', {'form': form})

@login_required
def chalan_list(request):
    chalans = Chalan.objects.filter(vehicle__owner=request.user)
    return render(request, 'chalan_list.html', {'chalans': chalans})

@login_required
def edit_chalan(request, pk):
    chalan = get_object_or_404(Chalan, pk=pk, vehicle__owner=request.user)
    if request.method == 'POST':
        form = ChalanForm(request.POST, instance=chalan)
        if form.is_valid():
            form.save()
            return redirect('chalan_list')
    else:
        form = ChalanForm(instance=chalan)
    return render(request, 'edit_chalan.html', {'form': form})
