from django.db import models
from django.urls import reverse

# Create your models here.

#Class that holds the team objects and attributes
class Team(models.Model):

    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    #Define default String to return the name of the object
    def __str__(self):
        return self.name
    
    #Returns the url to access the object
    def get_absolute_url(self):
        return reverse("team-detail", args=[str(self.id)])
    
#Class that holds the post objects and attributes
class Post(models.Model):
    STARRATING = (
        ('★', '1-Star Rating'),
        ('★★', '2-Star Rating'),
        ('★★★', '3-Star Rating'),
        ('★★★★', '4-Star Rating'),
        ('★★★★★', '5-Star Rating'),
        ('★★★★★★', '6-Star Rating')
    )
    title = models.CharField(max_length=200, blank = False)
    post = models.TextField(blank = False)
    rating = models.CharField(max_length=200, choices=STARRATING)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, default = None)

    #Define default String to return the name of the object
    def __str__(self):
        return self.title
    
    #Returns the url to access the object
    def get_absolute_url(self):
        return reverse("post-detail",  args=[str(self.id)])