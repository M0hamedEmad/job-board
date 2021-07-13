from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("create")

# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update(sender, instance, created, **kwargs):
    if not created:
        try:
            instance.user.save()
            print("update")

        except:
            Profile.objects.create(user=instance)
            print("update2")


# post_save.connect(update, sender=User)

