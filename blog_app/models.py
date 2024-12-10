from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
# 1-1 relationship
# 1 user can have only 1 profile => 1
# 1 user is associated to only 1 user => 1
# OneToOneField()=>Any model

# 1-M Relationship
# 1 user can have only M post => M
# 1 post is associated to only 1 user => 1
# In django use ForeignKey() ==> Use in Many side model

# M-M relationship
# 1 student can learn from M teachers ==>M
# 1 teachers can teach M student ==> M
# ManyTOManyField()==>Any place


