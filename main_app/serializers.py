from rest_framework import serializers 
from .models import Manager, Task, TeamMember, Project


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        # table name
        model= Manager
        fields = '__all__'

    