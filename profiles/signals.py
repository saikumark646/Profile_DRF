from django.contrib.auth.models import User
from profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver #its a decorator

@receiver(post_save, sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)


# once the user is created in the admin , by taking that user instance the above create_profile function will create new profile.
#step1: create function in signals.py
#step2 : mention default_app_config = 'profiles.apps.ProfileConfig' in __init__.py of the apps
#step3 : add the ready function in apps.py 
    #  def ready(self):
    #     import profiles.signals 