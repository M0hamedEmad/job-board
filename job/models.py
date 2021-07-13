from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from project.settings import MEDIA_ROOT
import os

JOB_TYPE = [
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
]




def image_upload(instance, filename):
    _ , extension = filename.split('.')
    return f"jobs/{instance.id}.{extension}"

class Job(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    # location
    job_type = models.CharField(max_length=10, choices=JOB_TYPE)
    published_at = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField(default=0)
    vacancy = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):

        # Slug Handle
        jobs = Job.objects.filter(title=self.title)
        jobs_num = len(jobs)
        obj = jobs.exists()

        if obj:
            self.slug = slugify(self.title)
            self.slug+=f"-{str(jobs_num)}"
        else:
            self.slug = slugify(self.title)

        # image rename handle 
        if self.pk is None:
            img = self.image
            self.image = None
            super(Job, self).save(*args, **kwargs)
            self.image = img

        super(Job, self).save(*args, **kwargs)

    
    def save(self, *args, **kwargs):
        if self.pk is None:
            img = self.image
            self.image = None
            super(Job, self).save(*args, **kwargs)
            self.image = img

        super(Job, self).save(*args, **kwargs)




    def __str__(self):
        return self.title

class Categorie(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



# @receiver(post_save, sender=Job)
# def rename_image(sender, instance, created, **kwargs):
#     if created:
#         current_image_path = instance.image.path
#         _ , extension = instance.image.name.split('.')
#         new_path = str(MEDIA_ROOT) + f'/jobs/{instance.id}.{extension}'

#         os.makedirs(os.path.dirname(new_path), exist_ok=True)
        
#         os.rename(current_image_path, new_path)
#         instance.image = new_path
#         instance.save()



# @receiver(post_save, sender=Job)
# def rename_image(sender, instance, created, **kwargs):
#     if created:
#         current_image_path = instance.image.path
#         _ , extension = instance.image.name.split('.')
#         new_path = str(MEDIA_ROOT) + f'/jobs/{instance.id}.{extension}'
#         os.makedirs(os.path.dirname(new_path), exist_ok=True)
#         os.rename(current_image_path, new_path)
#         instance.image = new_path
#         instance.save()




class Apply(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    cv = models.FileField(upload_to='Aplly/')
    cover_letter = models.TextField(max_length=300)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply')
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Apply"
