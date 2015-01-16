from django.db import models
from django.db.models.signals import post_save
from random import randint
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your models here.
class Grid(models.Model):
	Grid_id = models.AutoField(primary_key = True)
	length = models.IntegerField()
	breadth = models.IntegerField()
	def __unicode__(self):
		return str(self.Grid_id)
class rover(models.Model):
	Grid_id = models.IntegerField()
	x = models.IntegerField()
	y = models.IntegerField()
	direct = models.CharField(max_length = 10)
	rover_id = models.AutoField(primary_key = True)
	def __unicode__(self):
		return str(self.rover_id)
class subgrid(models.Model):
	Grid = models.ForeignKey(Grid)
	grid_x  = models.IntegerField()
	grid_y  = models.IntegerField()
	subgrid_id = models.AutoField(primary_key = True)
	def __unicode__(self):
		return "Grid "+ str(self.Grid)+" Subgrid "+str(self.subgrid_id)

class Mineral(models.Model):
	Name = models.CharField(max_length = 50,unique = True)
	M_id = models.AutoField(primary_key = True)
	def __unicode__(self):
		return str(self.Name)
class MineralDistribution(models.Model):
	Grid_id = models.ForeignKey(Grid)
	subgrid_id = models.ForeignKey(subgrid)
	m_id = models.ForeignKey(Mineral)
	quanity = models.IntegerField()
	def __unicode__(self):
		return "Grid "+str(self.Grid_id)+" subgrid "+str(self.subgrid_id.subgrid_id)+" mineral "+str(self.m_id.Name)

class roversensor(models.Model):
	rover_id = models.ForeignKey(rover)
	m_id = models.ForeignKey(Mineral)
	class Meta:
		unique_together = ('rover_id','m_id')
	def __unicode__(self):
		return "Rover "+str(self.rover_id.rover_id)+" mineral "+str(self.m_id.Name)
def subgrid_maker(sender,instance,**kwargs):
	for i in range(instance.length):
		for j in range(instance.breadth):
			subgr = subgrid()
			subgr.Grid = instance
			subgr.grid_x = i
			subgr.grid_y = j
			#p+=1
			subgr.save()

def distribution(sender,instance,**kwargs):
	mine = Mineral.objects.all()
	for k in mine:
		distri = MineralDistribution()
		distri.Grid_id = instance.Grid
		distri.subgrid_id = instance
		distri.m_id = k
		k = randint(0,2)
		if k == 0:
			distri.quanity = 0
		else:
			distri.quanity = randint(3,11)
		distri.save()

post_save.connect(subgrid_maker,sender=Grid)
post_save.connect(distribution,sender=subgrid)