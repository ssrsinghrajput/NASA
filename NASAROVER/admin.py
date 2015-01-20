'''DocString for admin'''
from django.contrib import admin
from NASAROVER.models import Grid, Mineral, Subgrid
from NASAROVER.models import MineralDistribution, Rover, Roversensor, Rover_position
# Register your models here.
admin.site.register(Grid)
admin.site.register(Subgrid)
admin.site.register(Mineral)
admin.site.register(MineralDistribution)
admin.site.register(Rover)
admin.site.register(Roversensor)
admin.site.register(Rover_position)
