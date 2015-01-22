'''DocString for models'''
from django.db import models
from django.db.models.signals import post_save
from random import randint
from django.contrib.auth.models import User
# Create your models here.


class Grid(models.Model):
    '''DocString for Grid'''
    grid_id = models.AutoField(primary_key=True)
    length = models.IntegerField()
    breadth = models.IntegerField()

    def __unicode__(self):
        return str(self.grid_id)


class Rover(models.Model):
    '''DocString for rover'''
  #  Grid_id = models.IntegerField()
    rover_id = models.AutoField(primary_key=True)
    rover_name = models.CharField(max_length=50)
    rover_ownedby = models.ForeignKey(User)
    def __unicode__(self):
        return str(self.rover_id)


class Subgrid(models.Model):
    '''DocString for subgrid'''
    grid = models.ForeignKey(Grid)
    grid_x = models.IntegerField()
    grid_y = models.IntegerField()
    subgrid_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "Grid " + str(self.grid) + " Subgrid " + str(self.subgrid_id)


class Mineral(models.Model):
    '''DocString for Minerals'''
    name = models.CharField(max_length=50, unique=True)
    m_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return str(self.name)


class MineralDistribution(models.Model):
    '''DocString for MineralDistribution'''
    grid_id = models.ForeignKey(Grid)
    subgrid_id = models.ForeignKey(Subgrid)
    m_id = models.ForeignKey(Mineral)
    quanity = models.IntegerField()

    def __unicode__(self):
        st1 = "Grid " + str(self.grid_id)
        st1 += " subgrid "+ str(self.subgrid_id.subgrid_id)
        st1 += " mineral "+ str(self.m_id.name)
        return st1
class Roversensor(models.Model):
    '''DocString for roversensro'''
    rover_id = models.ForeignKey(Rover)
    m_id = models.ForeignKey(Mineral)

    class Meta:
        '''DocString for Meta'''
        unique_together = ('rover_id', 'm_id')

    def __unicode__(self):
        st1 = "Rover " + str(self.rover_id.rover_id)
        st1 += " mineral " + str(self.m_id.name)
        return st1

class Roverposition(models.Model):
    '''DocString for roverposition'''
    grid_id = models.IntegerField()
    rover_id = models.ForeignKey(Rover)
    rover_x = models.IntegerField()
    rover_y = models.IntegerField()
    rover_direction = models.CharField(max_length=5)
    def __unicode__(self):
        return str(self.rover_id.rover_id)

def subgrid_maker(sender, instance, **kwargs):
    '''DocString for subgrid_maker'''
    for i in range(instance.length):
        for j in range(instance.breadth):
            subgr = Subgrid()
            subgr.grid = instance
            subgr.grid_x = i
            subgr.grid_y = j
            # p+=1
            subgr.save()


def distribution(sender, instance, **kwargs):
    '''DocString for distribution'''
    mine = Mineral.objects.all()
    for k in mine:
        distri = MineralDistribution()
        distri.grid_id = instance.grid
        distri.subgrid_id = instance
        distri.m_id = k
        k = randint(0, 2)
        if k == 0:
            distri.quanity = 0
        else:
            distri.quanity = randint(3, 11)
        distri.save()

def roverposition(sender, instance, **kwargs):
    '''DocString for roverposition'''
    obj = Roverposition()
    obj.rover_x = 0
    obj.rover_y = 0
    obj.rover_direction = ''
    obj.grid_id = 0
    obj.rover_id = instance
    obj.save()
post_save.connect(subgrid_maker, sender=Grid)
post_save.connect(distribution, sender=Subgrid)
post_save.connect(roverposition, sender=Rover)
