'''DocString for forms'''
from django.forms import ModelForm
from django import forms
from django.db import models
from NASAROVER.models import Grid, Mineral
from NASAROVER.models import MineralDistribution, rover, subgrid, roversensor


class GridForm(ModelForm):
    '''DocString for GridForm'''
    class Meta:
        model = Grid
        field = '__all__'


class RoverForm(ModelForm):
    '''DocString for RoverForm'''
    class Meta:
        model = rover
        field = '__all__'


class RoverSensor(ModelForm):
    '''DocString for GridForm'''
    class Meta:
        model = roversensor
        field = '__all__'


class mineral(ModelForm):
    '''docstring for mineral'''
    class Meta:
        model = Mineral
        field = '__all__'


class rovermovement(forms.Form):
    '''docstring for rovermovement'''
    MovementString = forms.CharField(label='MovementString', max_length=200)
    # class Meta:
    #model = rover
    #fields = ['MovementString','rover_id']
    rover_id = forms.IntegerField(label='rover_id')


class roverupdate(forms.Form):
    Grid_id = forms.IntegerField(label='Grid_id')
    rover_id = forms.IntegerField(label='rover_id')
    rover_x = forms.IntegerField(label='rover_x')
    rover_y = forms.IntegerField(label='rover_y')
    rover_direction = forms.CharField(label='rover_direction')
