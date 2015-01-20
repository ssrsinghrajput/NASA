from django.shortcuts import render
from django.http import HttpResponse
from forms import GridForm, RoverForm 
from forms import RoverSensor, mineral, rovermovement, roverupdate
from models import Grid, rover, roversensor, Mineral
from django.http import HttpResponse
# Create your views here.


def Grid_form(request):
    '''docstring for Grid_form'''
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
    if request.method == 'POST':
        form = RoverForm(request.POST)
        if form.is_valid():
            model1 = rover()
            model1.Grid_id = form.cleaned_data.get('Grid_id')
            if model1.Grid_id > len(Grid.objects.all()):
                return HttpResponse("Not any Grid with this id is created yet")
            model1.x = form.cleaned_data.get('x')
            model1.y = form.cleaned_data.get('y')
            model1.direct = form.cleaned_data.get('direct')
            model1.save()
    form = RoverForm()
    c = {'form': form}
    return render(request, 'RoverForm.html', c)


def Rover_Sensor(request):
    '''docstring for Rover_Sensor'''
    if request.method == 'POST':
        form = RoverSensor(request.POST)
        if form.is_valid():
            model1 = roversensor()
            model1.rover_id = form.cleaned_data.get('rover_id')
            model1.m_id = form.cleaned_data.get('m_id')
            model1.save()
        #   return render()
    form = RoverSensor()
    c = {'form': form}
    return render(request, 'RoverSensor.html', c)


def Mineral1(request):
    '''docstring for Mineral1'''
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
    return render(request, 'MenuForm.html')


def movementstring(request):
    '''DocString for movementstring'''
    if request.method == 'POST':
        form = rovermovement(request.POST)
        if form.is_valid():
            Id = form.cleaned_data.get('rover_id')
            #model1 = rover()
            if Id > len(rover.objects.all()):
                return HttpResponse("Not any rover with this id is created yet")
            model1 = rover.objects.get(rover_id=Id)
            x = model1.x
            y = model1.y
            d = model1.direct
            string = form.cleaned_data.get('MovementString')
            for i in range(0, len(string)):
                # print rover.x, rover.y, rover.d
                if (string[i] == 'M'):
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
            model1.x = x
            model1.y = y
            model1.direct = d
            model1.save()
            string1 = "Final Grid points are " + \
                str(x) + " and " + str(y) + " with direction " + d
            return HttpResponse(string1)
    form = rovermovement()
    c = {'form': form}
    return render(request, 'Movement.html', c)


def roverupdate1(request):
    '''docstring for roverupdate1'''
    if request.method == 'POST':
        form = roverupdate(request.POST)
        if form.is_valid():
            Id = form.cleaned_data.get('rover_id')
            l = form.cleaned_data.get('Grid_id')
            if Id > len(rover.objects.all()):
                return HttpResponse("Not any rover with this id is created yet")
            if l > len(Grid.objects.all()):
                return HttpResponse("Not any Grid with this id is created yet")
            model1 = rover.objects.get(rover_id=Id)
            model1.Grid_id = l
            model1.x = form.cleaned_data.get('rover_x')
            model1.direct = form.cleaned_data.get('rover_direction')
            model1.y = form.cleaned_data.get('rover_y')
            model1.save()
    form = roverupdate()
    c = {'form': form}
    return render(request, 'roverupdate.html', c)
