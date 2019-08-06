from django.db import models

# Create your models here.
class BookModel(models.Model):
    ISBN = models.CharField(max_length = 150)
    author = models.CharField(max_length = 150, default="")
    title = models.CharField(max_length = 150)
    comment = models.CharField(max_length = 300)
    cover = models.CharField(max_length = 300)



# class Comment(models.Model):
#     text
#     book