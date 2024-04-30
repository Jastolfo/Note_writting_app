from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()

  # "auto_now_add" field will automatically assign current time without being influenced by user's input
  created_at = models.DateTimeField(auto_now_add=True)

  """
    connect "author" to a user (foreign key)
    "on_delete = models.CASCADE" will delete the whole note if the referenced user is removed
    "related_name=notes" allows user to access the notes referenced to them
  """
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

  def __str__(self) -> str:
    return self.title