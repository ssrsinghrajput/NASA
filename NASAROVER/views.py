'''DocString for views'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from NASAROVER.forms import GridForm, RoverForm
from NASAROVER.forms import RoverSensor, mineral, rovermovement, roverupdate
from NASAROVER.models import Grid, Rover, Roversensor, Mineral, Rover_position
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from forms import UserForm
#from userauth.models import UserProfile


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
    c = {'form': form}
    return render(request, 'register.html', c)


def user_login(request):
    '''DocString for login'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
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
            model1.Grid_id = form.cleaned_data.get('Grid_id')
            model1.length = form.cleaned_data.get('length')
            model1.breadth = form.cleaned_data.get('breadth')
            model1.save()
    form = GridForm()
    c = {'form': form}
    return render(request, 'templates.html', c)


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
    c = {'form': form}
    return render(request, 'RoverForm.html', c)


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
    c = {'form': form}
    return render(request, 'RoverSensor.html', c)


def Mineral1(request):
    '''docstring for Mineral1'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = mineral(request.POST)
        if form.is_valid():
            model1 = Mineral()
            model1.Name = form.cleaned_data.get('Name')
            model1.save()
    form = mineral()
    c = {'form': form}
    return render(request, 'Mineral.html', c)


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
        print '111'
        form = rovermovement(request.POST)
        if True:
            # print '111'
            # print request
            Id = request.POST['rover_id']
            id = Rover.objects.get(rover_id=Id)

            model1 = Rover_position.objects.get(rover_id=id)
            x = model1.rover_x
            y = model1.rover_y
            d = model1.rover_direction
            string = request.POST['MovementString']
            for i in range(0, len(string)):
                # print rover.x, rover.y, rover.d
                if string[i] == 'M':
                    if d == 'E':
                        x = x + 1
                    elif d == 'W':
                        x = x - 1
                    elif d == 'N':
                        y = y + 1
                    elif d == 'S':
                        y = y - 1
                    #self.printwhatfound(rover, obj)
                    '''if x == 0 or x > obj.len_x:
                        if rover.y == 0 or rover.y == obj.len_y:
                            return'''
                elif string[i] == 'L':
                    if d == 'E':
                        d = 'N'
                    elif d == 'W':
                        d = 'S'
                    elif d == 'N':
                        d = 'W'
                    elif d == 'S':
                        d = 'E'
                elif string[i] == 'R':
                    if d == 'E':
                        d = 'S'
                    elif d == 'N':
                        d = 'E'
                    elif d == 'W':
                        d = 'N'
                    elif d == 'S':
                        d = 'W'
            model1.rover_x = x
            model1.rover_y = y
            model1.rover_direction = d
            model1.save()
            string1 = "Final Grid points are " + \
                str(x) + " and " + str(y) + " with direction " + d
            return HttpResponse(string1)
    form = rovermovement()
    k = Rover.objects.all()
    c = {'form': form, 'k': k}
    return render(request, 'Movement.html', c)

# def allrovers(request):


def roverupdate1(request):
    '''docstring for roverupdate1'''
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = roverupdate(request.POST)
        if form.is_valid():
            Id = form.cleaned_data.get('rover_id')
            l = form.cleaned_data.get('Grid_id')
           # print len(rover.objects.all()),
           # Id,len(rover_position.objects.all())
            # if Id > len(rover.objects.all()):
            #   return HttpResponse("Not any
            # rover with this id is created yet")
            if l > len(Grid.objects.all()):
                return HttpResponse("Not any Grid with this id is created yet")
            model1 = Rover_position.objects.get(rover_id=Id)
            model1.Grid_id = l
            model1.rover_x = form.cleaned_data.get('rover_x')
            model1.rover_direction = form.cleaned_data.get('rover_direction')
            model1.rover_y = form.cleaned_data.get('rover_y')
            model1.save()
    form = roverupdate()
    c = {'form': form}
    return render(request, 'roverupdate.html', c)
