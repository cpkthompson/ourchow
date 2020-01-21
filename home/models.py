from __future__ import unicode_literals

from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import BaseStreamBlock


class HomePage(Page):
    pass


class AboutPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ListPage(Page):
    pass


class BlogIndexPage(Page):
    pass


class BlogPost(Page):
    pass


class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]
