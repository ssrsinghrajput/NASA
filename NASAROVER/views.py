'''DocString for views'''
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from NASAROVER.forms import GridForm, RoverForm
from NASAROVER.forms import RoverSensor, mineral, rovermovement, roverupdate
from NASAROVER.models import Grid, Rover, Roversensor, Mineral, Roverposition
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from forms import UserForm
from models import Rover
from serializers import RoverSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
#from snippets.permissions import IsOwnerOrReadOnly

class Allrovers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rover.objects.all()
    serializer_class = RoverSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class Allrovers1(generics.ListCreateAPIView):
    queryset = Rover.objects.all()
    serializer_class = RoverSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class Listallrovers(generics.ListCreateAPIView):
    #if (not request.user.is_authenticated()):
     #   return redirect('/login/')
    #queryset = Rover.objects.all()
    serializer_class = RoverSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #print Rover.objects.all()
    def get_queryset(self):
        if self.request.user.is_anonymous():
            print '1'
            return Rover.objects.all()
        else:
            return Rover.objects.filter(rover_ownedby=self.request.user)
def register(request):
    '''DocString for register'''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
           # print request.POST
            my_model = form.save(commit=False)
            my_model.set_password(request.POST['password'])
            my_model.save()
            return redirect('/login')
    else:
        form = UserForm()
    c_form = {'form': form}
    return render(request, 'register.html', c_form)

next = ''
def user_login(request):
    '''DocString for login'''
#    next = ""
    global next
    #print request
    if request.GET:
        next = request.GET['next']
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
     #   print next, 'Hello'
        if user is not None:
            login(request, user)
            print next
            if not next == '':
                return HttpResponseRedirect(next)
            else:
                return redirect('/')
        else:
            return HttpResponse('Invalid user name or password')
    else:
        return render(request, 'login.html')


def logout_view(request):
    '''DocString for logout'''
    logout(request)
    return redirect('/login/')


def Grid_form(request):
    '''docstring for Grid_form'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = GridForm(request.POST)
        if form.is_valid():
            model1 = Grid()
            model1.grid_id = form.cleaned_data.get('grid_id')
            model1.length = form.cleaned_data.get('length')
            model1.breadth = form.cleaned_data.get('breadth')
            model1.save()
    form = GridForm()
    c_form = {'form': form}
    return render(request, 'templates.html', c_form)


def Rover_form(request):
    '''docstring for Rover_form'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = RoverForm(request.POST)
        if form.is_valid():
            model1 = Rover()
            model1.rover_name = form.cleaned_data.get('rover_name')
            #model1.Grid_id = form.cleaned_data.get('Grid_id')
            # if model1.Grid_id > len(Grid.objects.all()):
            #   return HttpResponse("Not any Grid with this id is created yet")
            #model1.x = form.cleaned_data.get('x')
            #model1.y = form.cleaned_data.get('y')
            #model1.direct = form.cleaned_data.get('direct')
            model1.rover_ownedby = form.cleaned_data.get('rover_ownedby')
            model1.save()
    form = RoverForm()
    c_form = {'form': form}
    return render(request, 'RoverForm.html', c_form)


def Rover_Sensor(request):
    '''docstring for Rover_Sensor'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = RoverSensor(request.POST)
        if form.is_valid():
            model1 = Roversensor()
            model1.rover_id = form.cleaned_data.get('rover_id')
            model1.m_id = form.cleaned_data.get('m_id')
            model1.save()
        #   return render()
    form = RoverSensor()
    c_form = {'form': form}
    return render(request, 'RoverSensor.html', c_form)


def Mineral1(request):
    '''docstring for Mineral1'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = mineral(request.POST)
        if form.is_valid():
            model1 = Mineral()
            model1.name = form.cleaned_data.get('name')
            model1.save()
    form = mineral()
    c_form = {'form': form}
    return render(request, 'Mineral.html', c_form)


def menu(request):
    '''docstring for menu'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    return render(request, 'MenuForm.html')


def movementstring(request):
    '''DocString for movementstring'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = rovermovement(request.POST)
        if True:
            # print '111'
            # print request
            rover_id = request.POST['rover_id']
            mid = Rover.objects.get(rover_id=rover_id)

            model1 = Roverposition.objects.get(rover_id=mid)
            x_coord = model1.rover_x
            y_coord = model1.rover_y
            direct = model1.rover_direction
            string = request.POST['MovementString']
            for i in range(0, len(string)):
                # print rover.x, rover.y, rover.d
                if string[i] == 'M':
                    if direct == 'E':
                        x_coord = x_coord + 1
                    elif direct == 'W':
                        x_coord = x_coord - 1
                    elif direct == 'N':
                        y_coord = y_coord + 1
                    elif direct == 'S':
                        y_coord = y_coord - 1
                    #self.printwhatfound(rover, obj)
                    '''if x == 0 or x > obj.len_x:
                        if rover.y == 0 or rover.y == obj.len_y:
                            return'''
                elif string[i] == 'L':
                    if direct == 'E':
                        direct = 'N'
                    elif direct == 'W':
                        direct = 'S'
                    elif direct == 'N':
                        direct = 'W'
                    elif direct == 'S':
                        direct = 'E'
                elif string[i] == 'R':
                    if direct == 'E':
                        direct = 'S'
                    elif direct == 'N':
                        direct = 'E'
                    elif direct == 'W':
                        direct = 'N'
                    elif direct == 'S':
                        direct = 'W'
            model1.rover_x = x_coord
            model1.rover_y = y_coord
            model1.rover_direction = direct
            model1.save()
            string1 = "Final Grid points are "
            string1 += str(x_coord) + " and "
            string1 += str(y_coord) + " with direction " + direct
            return HttpResponse(string1)
    form = rovermovement()
    k = Rover.objects.all()
    c_form = {'form': form, 'k': k}
    return render(request, 'Movement.html', c_form)

# def allrovers(request):


def roverupdate1(request):
    '''docstring for roverupdate1'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = roverupdate(request.POST)
        if form.is_valid():
            rover_id = form.cleaned_data.get('rover_id')
            length = form.cleaned_data.get('grid_id')
           # print len(rover.objects.all()),
           # Id,len(roverposition.objects.all())
            # if Id > len(rover.objects.all()):
            #   return HttpResponse("Not any
            # rover with this id is created yet")
            if length > len(Grid.objects.all()):
                return HttpResponse("Not any Grid with this id is created yet")
            model1 = Roverposition.objects.get(rover_id=rover_id)
            model1.grid_id = length
            model1.rover_x = form.cleaned_data.get('rover_x')
            model1.rover_direction = form.cleaned_data.get('rover_direction')
            model1.rover_y = form.cleaned_data.get('rover_y')
            model1.save()
    form = roverupdate()
    c_form = {'form': form}
    return render(request, 'roverupdate.html', c_form)
