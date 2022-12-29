from django.db import models
from django.utils.text import slugify


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()  
    
    # Used to avoid to put the () in the end example: BlogPost.published_string instead of BlogPost.published_string()
    @property # It says that it's a property instead of a method  
    def published_string(self):
        if self.published:
            return "The article is published"  
        return "The article isn't published" 

    def save(self, *args, **kwargs): # Overload the save method

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
