from django.forms.models import modelform_factory, modelformset_factory

from campaign.models import Campaign, Prospectus, Vote


CampaignFormSet = modelformset_factory(Campaign, extra=2, max_num=15, exclude=['prospectus'])


ProspectusForm = modelform_factory(Prospectus, exclude=['owner'])
