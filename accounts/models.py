from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)



# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         print("create")

# # post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)
# def update(sender, instance, created, **kwargs):
#     if not created:
#         try:
#             instance.user.save()
#             print("update")

#         except:
#             Profile.objects.create(user=instance)
#             print("update2")


# # post_save.connect(update, sender=User)



















# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)