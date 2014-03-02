from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from campaign.forms import CampaignFormSet, ProspectusForm


def create_edit_prospectus(request):
    if request.method == 'POST':
        prospectus_form = ProspectusForm(request.POST)
        campaign_formset = CampaignFormSet(request.POST)

        if prospectus_form.is_valid():
            prospectus_form.save(commit=False)
            if request.user.is_authenticated():
                prospectus_form.instance.owner = request.user
            if campaign_formset.is_valid():
                prospectus_form.instance.save()
                for campaign in campaign_formset.save(commit=False):
                    campaign.prospectus = prospectus_form.instance
                    campaign.save()

                return redirect(reverse('index'))
    else:
        prospectus_form = ProspectusForm()
        campaign_formset = CampaignFormSet()
    return render_to_response('campaign/new_prospectus.html',
                              {'prospectus_form': prospectus_form,
                               'campaign_forms': campaign_formset},
                              RequestContext(request))
