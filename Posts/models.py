from django.db import models

# Create your models here.
class PostCot(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# Create your models here.
class Posts(models.Model):
    title = models.ForeignKey(PostCot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_date =models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    sort_info = models.TextField()
    desc = models.TextField()

    # def __str__(self):
    #     return self.name