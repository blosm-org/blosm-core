from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumIntegerField
from django.db.models.signals import post_save

from .enums import ClusterType, MemberType, SettingsType

import uuid



class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = EnumIntegerField(MemberType)

    clusters = models.ManyToManyField('core.Cluster')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return self.user.username


class Settings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey('core.Member', related_name='settings', null=False, blank=False)
    type = EnumIntegerField(SettingsType)

    key = models.CharField(max_length=32)
    label = models.CharField(max_length=32)
    # can be anything here
    value = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

    def __str__(self):
        return '%s %s' % (self.member, self.type)


class Cluster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', null=True, blank=True)
    type = EnumIntegerField(ClusterType)

    name = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"

    def __str__(self):
        return self.name


# signal callback
def create_member(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        member = Member(user=user, type=MemberType.STUDENT)
        member.save()
post_save.connect(create_member, sender=User)
