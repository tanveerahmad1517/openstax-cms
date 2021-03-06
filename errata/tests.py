from django.test import TestCase

from errata.models import Errata
from books.models import Book, BookIndex, Subject
from pages.models import Page, HomePage


class ErrataTest(TestCase):

    def setUp(self):
        # create root page
        root_page = Page.objects.get(title="Root")
        # create homepage
        homepage = HomePage(title="Hello World",
                            slug="hello-world",
                            )
        # add homepage to root page
        root_page.add_child(instance=homepage)
        # create book index page
        book_index = BookIndex(title="Book Index",
                               page_description="Test",
                               dev_standard_1_description="Test",
                               dev_standard_2_description="Test",
                               dev_standard_3_description="Test",
                               )
        # add book index to homepage
        homepage.add_child(instance=book_index)
        # create subject
        subject = Subject.objects.create(name="Science")
        # create book (finally! needed for Errata reports)
        book = Book(cnx_id='d50f6e32-0fda-46ef-a362-9bd36ca7c97d',
                            title='University Physics',
                            salesforce_abbreviation='University Phys (Calc)',
                            salesforce_name='University Physics',
                            subject=subject,
                            description="Test Book",
                            )
        book_index.add_child(instance=book)

    def test_can_create_errata(self):
        errata = Errata.objects.create(
            book=Book.objects.get(cnx_id='d50f6e32-0fda-46ef-a362-9bd36ca7c97d'),
            detail="This is a test.",
        )
        self.assertEqual("New", errata.status)
