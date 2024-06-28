from django.db import models
import uuid
from django.contrib.auth.models import User

class YoutubeVideo(models.Model):
    video=models.FileField(upload_to='youtube')

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Colors(BaseModel):
    color_code=models.CharField(max_length=100)


class People(BaseModel):
    name =models.CharField(max_length=100)
    about=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    colors=models.ManyToManyField(Colors)


class PeopleAddress(BaseModel):
    people=models.ForeignKey(People, on_delete=models.CASCADE, related_name="address")
    address=models.TextField()

# Create your models here.
