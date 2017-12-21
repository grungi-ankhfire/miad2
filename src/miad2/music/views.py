from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from wagtail.wagtailadmin.utils import send_notification
from .forms import MusicTrackForm


# Create your views here.
def submit_track(request, tracks_index):

    form = MusicTrackForm(data=request.POST or None, label_suffix='')

    if request.method == 'POST' and form.is_valid():
        track_page = form.save(commit=False)
        track_page.slug = slugify(track_page.title)
        track = tracks_index.add_child(instance=track_page)
        if track:
            # blog.unpublish()
            # Submit page for moderation. This requires first saving a revision.
            track.save_revision(submitted_for_moderation=True)
            # Then send the notification to all Wagtail moderators.
            send_notification(track.get_latest_revision().id, 'submitted',
                              None)
        return HttpResponseRedirect(
            tracks_index.url + tracks_index.reverse_subpage('thanks'))
    context = {
        'form': form,
        'blog_index': tracks_index,
    }
    return render(request, 'music/track_add.html', context)
