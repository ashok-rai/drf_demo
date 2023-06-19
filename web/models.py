from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_dt = models.TimeField(auto_now_add=True)
    updated_dt = models.TimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
    	return self.title