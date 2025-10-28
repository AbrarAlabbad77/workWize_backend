from django.urls import path
from .views import ManagerIndex, ManagerDetails, TeamMemberDetails,AssignTaskToTeamMember
from .views import TeamMemberIndex, ProjectDetails, ProjectIndex, TaskDetails, TaskIndex
from .views import AssignManagerToProject, TeamMemberTasks, ProjectTask

urlpatterns = [
    # Manger CRUD
    path('managers/', ManagerIndex.as_view(), name='manager_path'),
    path('managers/<int:manager_id>/', ManagerDetails.as_view(), name='ManagerDetails_path'),
    
    # Team member CRUD 
    path('members/', TeamMemberIndex.as_view(), name='TeamMemberIndex_path'),
    path('members/<int:teamMember_id>/', TeamMemberDetails.as_view(), name='TeamMemberDetails_path'),
    
     # Project CRUD 
    path('projects/', ProjectIndex.as_view(), name='ProjectIndex_path'),
    path('projects/<int:project_id>/', ProjectDetails.as_view(), name='ProjectDetails_path'),
  
    # Task CRUD 
    path('tasks/', TaskIndex.as_view(), name='TaskIndex_path'),
    path('tasks/<int:task_id>/', TaskDetails.as_view(), name='TaskDetailsm_path'),
    
    
    # Relationship Endpoints
    path('projects/<int:project_id>/assign-manager/',AssignManagerToProject.as_view(), name='AssignManager_path'),
    path('projects/<int:project_id>/tasks/',ProjectTask.as_view(),name='ProjectTask_path'),
    
    path('members/<int:teamMember_id>/tasks/', TeamMemberTasks.as_view(), name='TeamMemberTasks_path'),
    path('members/<int:teamMember_id>/assign-task/',AssignTaskToTeamMember.as_view(), name='assign-task_path'),

   
]
