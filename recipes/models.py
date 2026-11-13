from django.db import models



class Recipe(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField('auth.User', related_name='liked_recipes', blank=True)

    
    def __str__(self):
        return self.title 


   
   
   

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name