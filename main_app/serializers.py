from rest_framework import serializers 
from .models import Manager, Task, TeamMember, Project


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        # table name
        model= Manager
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        # table name
        model= TeamMember
        fields = '__all__' 
        extra_kwargs = {
            'tasks': {'required': False}
        }
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # table name
        model= Task
        fields = '__all__'    
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        # table name
        model= Project
        fields = '__all__' 
        
        extra_kwargs = {
            'manager_id': {'required': False}
        }