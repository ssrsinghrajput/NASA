from django.contrib import admin
from models import Grid, subgrid, Mineral, MineralDistribution, rover, roversensor
# Register your models here.
admin.site.register(Grid)
admin.site.register(subgrid)
admin.site.register(Mineral)
admin.site.register(MineralDistribution)
admin.site.register(rover)
admin.site.register(roversensor)
