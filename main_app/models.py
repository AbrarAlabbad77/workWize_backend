from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    deadline = models.DateField()
    manager_id = models.ForeignKey(Manager, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.title
    
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    due_data = models.DateField()
    project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.title 

    
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    # M TO M between Task and Team Member
    tasks = models.ManyToManyField(Task)
    
    def __str__(self):
        return self.name 
    

