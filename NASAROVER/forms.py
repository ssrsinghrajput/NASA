'''DocString for forms'''
from django.forms import ModelForm
from django import forms
from django.db import models
from NASAROVER.models import Grid, Mineral, Roverposition
from NASAROVER.models import Rover, Roversensor
#from userauth.models import UserProfile
from django.contrib.auth.models import User


class UserForm(ModelForm):

    '''DocString for UserForm'''
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():

        '''DocString for Meta'''
        model = User
        fields = ('username', 'email', 'password')


class GridForm(ModelForm):

    '''DocString for GridForm'''
    class Meta():

        '''DocString for Meta'''
        model = Grid
        field = '__all__'


class RoverForm(ModelForm):

    '''DocString for RoverForm'''
    class Meta():

        '''DocString for Meta'''
        model = Rover
        field = '__all__'


class RoverSensor(ModelForm):

    '''DocString for GridForm'''
    class Meta():

        '''DocString for Meta'''
        model = Roversensor
        field = '__all__'


class mineral(ModelForm):

    '''docstring for mineral'''
    class Meta():

        '''DocString for Meta'''
        model = Mineral
        field = '__all__'


class rovermovement(forms.Form):

    '''docstring for rovermovement'''
    MovementString = forms.CharField(label='MovementString', max_length=200)
    # class Meta:
    #model = rover
    #fields = ['MovementString','rover_id']
    rover_id = forms.IntegerField(label='rover_id')


class roverupdate(ModelForm):

    '''DocString for roverupdate'''
    class Meta():

        '''DocString for Meta'''
        model = Roverposition
        field = '__all__'
