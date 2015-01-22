'''DocString for Serializers'''
from models import Rover
from rest_framework import serializers
class RoverSerializer(serializers.ModelSerializer):
    '''DocString for RoverSerializer'''
    Rover = serializers.PrimaryKeyRelatedField(many=True, queryset=Rover.objects.all())
    class Meta:
        '''DocString for Meta'''
        model = Rover
        fields = ('rover_id', 'rover_name', 'rover_ownedby')
