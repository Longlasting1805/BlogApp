from django.db import models


# Create your models here.

class Blog(models.Model):
    home = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    blog = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.home

    def save(self, *args, **kwargs):
        self.home = f"{self.home} - {self.blog}"
        super().save(*args, **kwargs)


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=225)
#     body_Text = models.TextField()
#     pub_date = models.DateTimeField()
#     mod_date = models.DateTimeField()
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField()
#     number_of_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline
