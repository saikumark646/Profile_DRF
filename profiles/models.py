from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 100)
    city = models.CharField(max_length = 50)
    avatar = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.user )


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    status_content = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)

    # class Meta:
    #     verbose_name_plural = "statuses" 
#here class meta returns model profllestatus name to statuses in admin panel

    def __str__(self):
        return str(self.user_profile)
    