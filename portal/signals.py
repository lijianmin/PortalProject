from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site
from portal.models import post

def create_redirect(sender, instance, **kwargs):
  if sender == post:
    try:
      o = sender.objects.get(id=instance.id)
      if o.title_slug != instance.title_slug:
        old_path = o.get_absolute_url()
        new_path = instance.get_absolute_url()
        # Update any existing redirects that are pointing to the old url
        for redirect in Redirect.objects.filter(new_path=old_path):
          redirect.new_path = new_path
          # If the updated redirect now points to itself, delete it
          # (i.e. slug = A -> slug = B -> slug = A again)
          if redirect.new_path == redirect.old_path:
            redirect.delete()
          else:
            redirect.save()
        # Now add the new redirect
        Redirect.objects.create(
          site=Site.objects.get_current(),
          old_path=old_path,
          new_path=new_path)
    except sender.DoesNotExist:
        pass