from django.db import models
from django.template.response import TemplateResponse
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route


class MusicTracksIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class MusicTrackPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    track = StreamField([('video', EmbedBlock())])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel('track'),
    ]


class MusicTrackSubmissionPage(RoutablePageMixin, Page):
    intro = RichTextField(blank=True)
    submit_info = RichTextField(blank=True)
    thanks_info = RichTextField(blank=True)

    # @route(r'^$')
    # def base(self, request):
    #     return TemplateResponse(request, self.get_template(request),
    #                             self.get_context(request))

    @route(r'^$')
    def submit(self, request):
        from .views import submit_track
        return submit_track(request, self)

    @route(r'^submit-thank-you/$')
    def thanks(self, request):
        return TemplateResponse(request, 'portal_pages/thank_you.html', {
            "thanks_info": self.thanks_info
        })
