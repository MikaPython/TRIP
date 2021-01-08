from django.db import models

from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.name}'
        return self.name

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False

class Country(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='countries')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='countries')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Image(models.Model):
    image = models.ImageField(upload_to='countries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url

