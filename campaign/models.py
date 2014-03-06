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


PROSPECTUS_FIELD_HELP = {
    'privacy_status': [
        'Private: Only the creator',
        'Public: Everyone',
        'Registered Only: Only registered users',
        'Invite Only: Only people the creator invites',
        'Anyone With Link: Anyone who is provided with a link'],
    'vote_type': [
        'Ranking: Voters order based on preference',
        ('Point Assignment: Voters invest points per campaign to '
         'indicate interest')],
    'point_multiplier': [
        ('Voters have a point total equal to this times the number of '
         'campaigns that can be spent on ranking, with higher totals '
         'meaning more interest')]

}


class Prospectus(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, default=None)
    privacy_status = models.CharField(max_length=2,
                                      choices=PRIVACY_CHOICES,
                                      default=PRIVACY_CHOICES[0][0],
                                      help_text='Who can see this prospectus')
    private_votes = models.BooleanField(default=False,
                                        help_text=("Voters can't see how "
                                                   "others voted until "
                                                   "voting commences"))
    vote_type = models.CharField(max_length=10,
                                 choices=VOTE_CHOICES,
                                 default=VOTE_CHOICES[0][0],
                                 help_text=('How voters can vote on the '
                                            'associated campaigns'))
    point_multiplier = models.IntegerField(blank=True, null=True,
                                           help_text=(
                                               'If using Point Assignment, '
                                               'indicates how many points '
                                               'users can spend ranking '
                                               'campaigns'))
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    stars = models.IntegerField(default=0, editable=False)
    
    class Meta:
        verbose_name_plural = 'prospectuses'


class Campaign(models.Model):
    prospectus = models.ForeignKey(Prospectus)
    short_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)


class Vote(models.Model):
    voter = models.ForeignKey(User)
    campaign = models.ForeignKey(Campaign)
    rating = models.IntegerField()