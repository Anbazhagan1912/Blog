from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4),
    created_at = models.DateTimeField(auto_now_add=True),
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500),
    blog_text = models.TextField()
    img = models.ImageField(upload_to='blogs')

    def __str__(self) -> str:
        return self.title