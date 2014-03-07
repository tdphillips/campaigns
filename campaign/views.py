from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from campaign.forms import CampaignFormSet, ProspectusForm
from campaign.models import PROSPECTUS_FIELD_HELP, Campaign, Prospectus


def create_prospectus(request):
    if request.method == 'POST':
        prospectus_form = ProspectusForm(request.POST)
        campaign_formset = CampaignFormSet(request.POST,
                                           queryset=Campaign.objects.none())

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
        campaign_formset = CampaignFormSet(queryset=Campaign.objects.none())
    return render_to_response('campaign/new_prospectus.html',
                              {'prospectus_form': prospectus_form,
                               'campaign_forms': campaign_formset,
                               'prospectus_help': PROSPECTUS_FIELD_HELP},
                              RequestContext(request))


def edit_prospectus(request, prospectus_id):
    prospectus = Prospectus.objects.get(id=prospectus_id)

    # Ensure only the owner can edit a prospectus
    # Allow staff to edit orphaned prospectuses
    if not ((request.user == prospectus.owner) or
            (prospectus.owner is None and request.user.is_staff)):
        raise Http404()

    if request.method == 'POST':
        prospectus_form = ProspectusForm(request.POST, instance=prospectus)
        campaign_formset = CampaignFormSet(
            request.POST,
            queryset=prospectus.campaign_set.all())

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
        prospectus_form = ProspectusForm(instance=prospectus)
        campaign_formset = CampaignFormSet(
            queryset=prospectus.campaign_set.all())
    return render_to_response('campaign/new_prospectus.html',
                              {'prospectus_form': prospectus_form,
                               'campaign_forms': campaign_formset,
                               'prospectus_help': PROSPECTUS_FIELD_HELP},
                              RequestContext(request))


def view_prospectus(request, prospectus_id):
    prospectus = Prospectus.objects.get(id=prospectus_id)
    return render_to_response('campaign/view_prospectus.html',
                              {'prospectus': prospectus},
                              RequestContext(request))
