from django.forms import ModelForm
from django import forms
from django.db import models
from models import Grid, Mineral, MineralDistribution, rover, subgrid, roversensor

class GridForm(ModelForm):
	class Meta:
		model = Grid
		field = '__all__'

class RoverForm(ModelForm):
	class Meta:
		model = rover
		field = '__all__'

class RoverSensor(ModelForm):
	class Meta:
		model = roversensor
		field = '__all__'

class mineral(ModelForm):
	class Meta:
		model = Mineral
		field = '__all__'

class rovermovement(forms.Form):
	MovementString = forms.CharField(label = 'MovementString', max_length = 200)
	#class Meta:
		#model = rover
		#fields = ['MovementString','rover_id']
	rover_id = forms.IntegerField(label = 'rover_id')

class roverupdate(forms.Form):
	Grid_id = forms.IntegerField(label = 'Grid_id')
	rover_id = forms.IntegerField(label = 'rover_id')
	rover_x = forms.IntegerField(label = 'rover_x')
	rover_y = forms.IntegerField(label = 'rover_y')
	rover_direction = forms.CharField(label = 'rover_direction')