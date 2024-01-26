from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

# from django.dispatch import receiver
from users.models import Profile


# @receiver(post_save, sender=Profile) <--- another way to do.
def create_profile(sender, instance, created, **kwargs):
    """
    sender - is going to be the model that actually sends this.
    instance - going to be the instance of the model that actually triggered
    this or the object.
    created - is going to let us know it's simply going to be a true or false value, if a user was added or model was added to the database or if wa simply saved again.
    **kwargs - rest of the keyword arguments.
    """

    if created:
        user = instance
        Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, Profile)
