from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ManagerSerializer, TaskSerializer, TeamMemberSerializer, ProjectSerializer
from .models import Manager, Task, TeamMember, Project


# Create your views here.
class ManagerIndex(APIView):
    
    def get(self,request):
        queryset = Manager.objects.all()
        serializer = ManagerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        try:
            serializer = ManagerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class ManagerDetails(APIView):
    
    #  get specific manager by id 
    def get(self, request, manager_id):
        queryset = Manager.objects.get(id=manager_id)
        serializer = ManagerSerializer(queryset)
        return Response(serializer.data)
    
    
    # Update manager info
    def put(self,request, manager_id):
        try:
            queryset = get_object_or_404(Manager, id=manager_id)
            serializer = ManagerSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # delete manager 
    def delete(self, request, manager_id):
        try:
            queryset = get_object_or_404(Manager, id=manager_id)
            queryset.delete()
            return Response({'message': f' Mnanger {manager_id} has been deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'ERROR': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
    
#  ############################# Team member CRUD ##############################


class TeamMemberIndex(APIView):
    
    def get(self,request):
        queryset = TeamMember.objects.all()
        serializer = TeamMemberSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        try:
            serializer = TeamMemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class TeamMemberDetails(APIView):
    
    #  get specific Team member by id 
    def get(self, request, teamMember_id):
        queryset = get_object_or_404(TeamMember, id=teamMember_id)
        serializer = TeamMemberSerializer(queryset)
        return Response(serializer.data)
    
    
    # Update Team member info
    def put(self,request, teamMember_id):
        try:
            queryset = get_object_or_404(TeamMember, id=teamMember_id)
            serializer = TeamMemberSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # delete Team member 
    def delete(self, request, teamMember_id):
        try:
            queryset = get_object_or_404(TeamMember, id=teamMember_id)
            queryset.delete()
            return Response({'message': f' Team member {teamMember_id} has been deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'ERROR': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

#  ############################# Project  CRUD ##############################

class ProjectIndex(APIView):
    
    def get(self,request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class ProjectDetails(APIView):
    
    #  get specific Teproject  by id 
    def get(self, request, project_id):
        queryset = get_object_or_404(Project, id=project_id)
        serializer = ProjectSerializer(queryset)
        return Response(serializer.data)
    
    
    # Update project info
    def put(self,request, project_id):
        try:
            queryset = get_object_or_404(Project, id=project_id)
            serializer = ProjectSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # delete project
    def delete(self, request, project_id):
        try:
            queryset = get_object_or_404(Project, id=project_id)
            queryset.delete()
            return Response({'message': f' Project {project_id} has been deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'ERROR': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  



#  ############################# Task  CRUD ##############################

class TaskIndex(APIView):
    
    def get(self,request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskDetails(APIView):
    
    #  get specific task  by id 
    def get(self, request, task_id):
        queryset = get_object_or_404(Task, id=task_id)
        serializer = TaskSerializer(queryset)
        return Response(serializer.data)
    
    
    # Update task info
    def put(self,request, task_id):
        try:
            queryset = get_object_or_404(Task, id=task_id)
            serializer = TaskSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'ERROR':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # delete task
    def delete(self, request, task_id):
        try:
            queryset = get_object_or_404(Task, id=task_id)
            queryset.delete()
            return Response({'message': f' Task {task_id} has been deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'ERROR': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)          
        
        
#  ############################# Relationship Endpoints ##############################

# assign task to specific team member 
class AssignTaskToTeamMember(APIView):
    
    def post(self,request, teamMember_id):
        try:
            team_member = get_object_or_404(TeamMember, id=teamMember_id) 
            task_id = request.data.get('task_id')
            cureentTask = get_object_or_404(Task, id=task_id)
            
            # have the member in (team_member) var and the task id in (cureentTask) var
            team_member.tasks.add(cureentTask)
            return Response({'message': f'Task {cureentTask.title} assigned to {team_member.name} succcessfully' 
                             }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'ERROR': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update manager for  project
class AssignManagerToProject(APIView):
    
    def post(self,request, project_id):
        try:
            project = get_object_or_404(Project, id=project_id)
            manager_id = request.data.get('manager_id')
            currentManager = get_object_or_404(Manager, id=manager_id)
            
            project.manager_id = currentManager
            project.save()
            return Response({ 'message': f'Manager {currentManager.name} assigned to {project.title} succcessfully' 
                             },status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'ERROR': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
        
# get all task for specific team member 
class TeamMemberTasks(APIView):
    
    def get(self, request, teamMember_id):
        team_member = get_object_or_404(TeamMember, id=teamMember_id)
        tasks = team_member.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# get all task for specific project 
class ProjectTask(APIView):
    
    def get(self,request, project_id):
        project= get_object_or_404(Project, id=project_id)
        tasks = Task.objects.filter(project_id=project_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    
    
    
        
        