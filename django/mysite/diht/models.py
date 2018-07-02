from django.db import models


class Article (models.Model):

    url = models.SlugField (max_length = 128, unique = True)
    title = models.CharField (max_length = 128)
    dateCreated = models.DateTimeField (auto_now_add = True)
#    dateModidied =
#    previewImage = models.ImageField ()
    previewText = models.TextField ()
#    categories =

    def __str__ (self) :
        return "Article " + self.url + " '" + self.title + "'"


class Human (models.Model) :

    name = models.CharField (max_length = 20)
    nickname = models.CharField (max_length = 20)

    def __str__ (self) :
        return self.name + "'" + self.nickname + "'"