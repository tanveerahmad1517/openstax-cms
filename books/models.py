import urllib
import json
import dateutil.parser

from django.db import models
from django.conf import settings

from wagtail.wagtailcore.models import Page, Orderable, Site
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel,
                                                PageChooserPanel)
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey

from allies.models import Ally


class Quotes(models.Model):
    quote_text = RichTextField()
    quote_author = models.CharField(max_length=255)
    quote_author_school = models.CharField(max_length=255)

    api_fields = ('quote_text', 'quote_author', 'quote_author_school', )

    panels = [
        FieldPanel('quote_text'),
        FieldPanel('quote_author'),
        FieldPanel('quote_author_school'),
    ]


class FacultyResource(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField()

    api_fields = ('heading', 'description', )

    panels = [
        FieldPanel('heading'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.heading

register_snippet(FacultyResource)


class StudentResource(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField()

    api_fields = ('heading', 'description', )

    panels = [
        FieldPanel('heading'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.heading

register_snippet(StudentResource)


class FacultyResources(models.Model):
    resource = models.ForeignKey(
        FacultyResource,
        null=True,
        help_text="Manage resources through snippets.",
        related_name='+'
    )
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )
    link_text = models.CharField(max_length=255, help_text="Call to Action Text")

    api_fields = ('resource', 'link_external', 'link_page',
                  'link_document', 'link_text', )

    panels = [
        SnippetChooserPanel('resource', FacultyResource),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
        FieldPanel('link_text'),
    ]


class StudentResources(models.Model):
    resource = models.ForeignKey(
        StudentResource,
        null=True,
        help_text="Manage resources through snippets.",
        related_name='+'
    )
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )
    link_text = models.CharField(max_length=255, help_text="Call to Action Text")

    api_fields = ('resource', 'link_external', 'link_page',
                  'link_document', 'link_text', )

    panels = [
        SnippetChooserPanel('resource', StudentResource),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
        FieldPanel('link_text'),
    ]


class Authors(models.Model):
    name = models.CharField(max_length=255) 
    university = models.CharField(max_length=255, null=True, blank=True) 
    country = models.CharField(max_length=255, null=True, blank=True) 
    senior_author = models.BooleanField(default=False)
    display_at_top = models.BooleanField(default=False)
    book = ParentalKey('books.Book', related_name='book_contributing_authors', null=True, blank=True)
    
    api_fields = ('name', 'university', 'country', 'senior_author', 'display_at_top', )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('university'),
        FieldPanel('country'),
        FieldPanel('senior_author'),
        FieldPanel('display_at_top'),
    ]


class BookAlly(models.Model):
    ally = models.ForeignKey(
        Ally,
        null=True,
        help_text="Manage allies through snippets.",
        on_delete=models.SET_NULL,
        related_name='allies_ally'
    )
    book_link_url = models.URLField(blank=True, help_text="Call to Action Link")
    book_link_text = models.CharField(max_length=255, help_text="Call to Action Text")

    api_fields = ('ally', 'book_link_url', 'book_link_text', )

    panels = [
        SnippetChooserPanel('ally'),
        FieldPanel('book_link_url'),
        FieldPanel('book_link_text'),
    ]


class Subject(models.Model):
    name = models.CharField(max_length=255)
    
    api_fields = ('name', )
    
    panels = [
        FieldPanel('name'),
    ]
    
    def __str__(self):
        return self.name

register_snippet(Subject)


class BookQuotes(Orderable, Quotes):
    quote = ParentalKey('books.Book', related_name='book_quotes')


class BookFacultyResources(Orderable, FacultyResources):
    book_faculty_resource = ParentalKey('books.Book', related_name='book_faculty_resources')


class BookStudentResources(Orderable, StudentResources):
    book_student_resource = ParentalKey('books.Book', related_name='book_student_resources')


class BookAllies(Orderable, BookAlly):
    book_ally = ParentalKey('books.Book', related_name='book_allies')


class Book(Page):
    created = models.DateTimeField(auto_now_add=True)
    cnx_id = models.CharField(max_length=255, help_text="This is used to pull relevant information from CNX.")
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,
                                null=True, related_name='+')

    def get_subject_name(self):
        return self.subject.name

    subject_name = property(get_subject_name)
    updated = models.DateTimeField(auto_now=True)
    is_ap = models.BooleanField(default=False)
    short_description = RichTextField(blank=True, help_text="Description shown on Subject page.")
    description = RichTextField(blank=True, help_text="Description shown on Book Detail page.")
    cover = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_cover_url(self):
        site = Site.objects.get(is_default_site=True)
        if site.port == 80:
            return "http://{}{}".format(site.hostname, self.cover.url)
        else:
            return "http://{}:{}{}".format(site.hostname, site.port, self.cover.url)

    cover_url = property(get_cover_url)
    publish_date = models.DateField(blank=True, null=True, editable=False)
    isbn_10 = models.IntegerField(blank=True, null=True)
    isbn_13 = models.CharField(max_length=255, blank=True, null=True)
    license_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    license_version = models.CharField(max_length=255, blank=True, null=True, editable=False)
    license_url = models.CharField(max_length=255, blank=True, null=True, editable=False)
    high_resolution_pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_high_res_pdf_url(self):
        site = Site.objects.get(is_default_site=True)
        if site.port == 80:
            return "http://{}{}".format(site.hostname, self.high_resolution_pdf.url)
        else:
            return "http://{}:{}{}".format(site.hostname, site.port, self.high_resolution_pdf.url)

    high_resolution_pdf_url = property(get_high_res_pdf_url)
    low_resolution_pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_low_res_pdf_url(self):
        site = Site.objects.get(is_default_site=True)
        if site.port == 80:
            return "http://{}{}".format(site.hostname, self.low_resolution_pdf.url)
        else:
            return "http://{}:{}{}".format(site.hostname, site.port, self.low_resolution_pdf.url)

    low_resolution_pdf_url = property(get_low_res_pdf_url)
    ibook_link = models.URLField(blank=True, help_text="Link to iBook")
    webview_link = models.URLField(blank=True, help_text="Link to CNX Webview book")
    concept_coach_link = models.URLField(blank=True, help_text="Link to Concept Coach")

    content_panels = Page.content_panels + [
        FieldPanel('cnx_id'),
        SnippetChooserPanel('subject', Subject),
        FieldPanel('is_ap'),
        FieldPanel('description', classname="full"),
        DocumentChooserPanel('cover'),
        InlinePanel('book_quotes', label="Quotes"),
        InlinePanel('book_allies', label="Allies"),
        InlinePanel('book_student_resources', label="Student Resources"),
        InlinePanel('book_faculty_resources', label="Instructor Resources"),
        InlinePanel('book_contributing_authors', label="Contributing Authors"),
        FieldPanel('isbn_10'),
        FieldPanel('isbn_13'),
        DocumentChooserPanel('high_resolution_pdf'),
        DocumentChooserPanel('low_resolution_pdf'),
        FieldPanel('ibook_link'),
        FieldPanel('webview_link'),
        FieldPanel('concept_coach_link'),
    ]

    api_fields = ('created',
                  'updated',
                  'slug',
                  'title',
                  'cnx_id',
                  'subject_name',
                  'is_ap',
                  'description',
                  'cover_url',
                  'book_quotes',
                  'book_allies',
                  'book_student_resources',
                  'book_faculty_resources',
                  'book_contributing_authors',
                  'publish_date',
                  'isbn_10',
                  'isbn_13',
                  'license_name',
                  'license_version',
                  'license_url',
                  'high_resolution_pdf_url',
                  'low_resolution_pdf_url',
                  'ibook_link',
                  'webview_link',
                  'concept_coach_link',)

    parent_page_types = ['books.BookIndex']

    # we are overriding the save() method to go to CNX and fetch information with the CNX ID
    def save(self, *args, **kwargs):
        url = '{}/contents/{}.json'.format(settings.CNX_ARCHIVE_URL, self.cnx_id)
        response = urllib.request.urlopen(url).read()
        result = json.loads(response.decode('utf-8'))
        
        self.license_name = result['license']['name']
        self.license_version = result['license']['version']
        self.license_url = result['license']['url']
        
        self.publish_date = dateutil.parser.parse(result['created'], dayfirst=True).date()
        
        return super(Book, self).save(*args, **kwargs)


class BookIndex(Page):
    page_description = RichTextField()
    dev_standards_heading = models.CharField(max_length=255, blank=True, null=True)
    dev_standard_1_heading = models.CharField(max_length=255, blank=True, null=True)
    dev_standard_1_description = RichTextField()
    dev_standard_2_heading = models.CharField(max_length=255, blank=True, null=True)
    dev_standard_2_description = RichTextField()
    dev_standard_3_heading = models.CharField(max_length=255, blank=True, null=True)
    dev_standard_3_description = RichTextField()
    subject_list_heading = models.CharField(max_length=255, blank=True, null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('page_description'),
        FieldPanel('dev_standards_heading'),
        FieldPanel('dev_standard_1_heading'),
        FieldPanel('dev_standard_1_description'),
        FieldPanel('dev_standard_2_heading'),
        FieldPanel('dev_standard_2_description'),
        FieldPanel('dev_standard_3_heading'),
        FieldPanel('dev_standard_3_description'),
        FieldPanel('subject_list_heading'),
    ]
    
    api_fields = (
        'title',
        'page_description',
        'dev_standards_heading',
        'dev_standard_1_heading',
        'dev_standard_1_description',
        'dev_standard_2_heading',
        'dev_standard_2_description',
        'dev_standard_3_heading',
        'dev_standard_3_description',
        'subject_list_heading',
    )
    
    parent_page_types = ['pages.HomePage']
    subpage_types = ['books.Book']
