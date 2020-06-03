from colossus.apps.campaigns.api import send_campaign, send_campaign_email
from colossus.apps.campaigns.tasks import send_campaign_task
from django.apps import apps

Campaign = apps.get_model("campaigns", "Campaign")
t = send_campaign(Campaign.objects.get(id=2))

task = send_campaign_email()

send_campaign_task(2)
# process is: send_campaign-->send_campaign_email_subscriber-->send_campaign_email

# test = ("%s <%s.list-id.%s>"% (email.campaign.mailing_list.name,email.campaign.mailing_list.uuid,context["domain"],))
