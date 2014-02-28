from django.contrib.auth.models import User
from django.db import models

VOTE_CHOICES = (
    ('RANK', 'Ranking'),
    ('POINT', 'Point Assignment'),
)

PRIVACY_CHOICES = (
    ('PR', 'Private'),
    ('PU', 'Public'),
    ('RO', 'Registered Only'),
    ('IO', 'Invite Only'),
    ('LO', 'Anyone With Link'),
)


class Prospectus(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, default=None)
    privacy_status = models.CharField(max_length=2,
                                      choices=PRIVACY_CHOICES,
                                      default=PRIVACY_CHOICES[0][0])
    private_votes = models.BooleanField(default=False)
    vote_type = models.CharField(max_length=10,
                                 choices=VOTE_CHOICES,
                                 default=VOTE_CHOICES[0][0])
    point_multiplier = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    stars = models.IntegerField(default=0, editable=False)
    
    class Meta:
        verbose_name_plural = 'prospectuses'


class Campaign(models.Model):
    prospectus = models.ForeignKey(Prospectus)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)


class Vote(models.Model):
    voter = models.ForeignKey(User)
    campaign = models.ForeignKey(Campaign)
    rating = models.IntegerField()