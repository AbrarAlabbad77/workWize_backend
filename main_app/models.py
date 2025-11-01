from django.db import models
from django.contrib.auth import get_user_model



# --------------------
# MANAGER MODEL
# --------------------
class Manager(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,  unique=True)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name



# --------------------
# PROJECT MODEL
# --------------------
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    deadline = models.DateField()
    manager_id = models.ForeignKey(Manager, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.title


# --------------------
# TEAM MEMBER MODEL
# --------------------
User =  get_user_model()
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,  unique=True)
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  

    # M TO M between Task and Team Member
    # tasks = models.ManyToManyField("Task")
    
    def __str__(self):
        return self.name 


# --------------------
# CONSTANTS (choices)
# --------------------
STATUS = (
     ('To Do', 'To Do'),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
 ) 

PRIORITY = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
)


# --------------------
# TASK MODEL
# --------------------
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    due_data = models.DateField()
    state = models.CharField(max_length=50, choices=STATUS)
    priority = models.CharField(max_length=20, choices=PRIORITY, default="Medium")
    created_at = models.DateTimeField(auto_now_add=True)
    assignee = models.ForeignKey(TeamMember, on_delete=models.SET_NULL,null=True, blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)
    
    
    def __str__(self):
        return self.title 


    

