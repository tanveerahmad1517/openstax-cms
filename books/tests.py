from wagtail.tests.utils import WagtailPageTests
from wagtail.core.models import Page
from pages.models import HomePage
from books.models import BookIndex, Book
from snippets.models import Subject


class BookTests(WagtailPageTests):
    def setUp(self):
        pass

    def test_can_create_book_index(self):
        #create root page
        root_page = Page.objects.get(title="Root")
        #create homepage
        homepage = HomePage(title="Hello World",
                            slug="hello-world",
                            )
        #add homepage to root page
        root_page.add_child(instance=homepage)
        #create book index page
        book_index = BookIndex(title="Book Index",
                               page_description="Test",
                               dev_standard_1_description="Test",
                               dev_standard_2_description="Test",
                               dev_standard_3_description="Test",
                               )
        #add book index to homepage
        homepage.add_child(instance=book_index)

        retrieved_page = Page.objects.get(id=book_index.id)
        self.assertEqual(retrieved_page.title, "Book Index")

    def test_can_create_book(self):
        subject = Subject(name="Science")

        book = Book(cnx_id='031da8d3-b525-429c-80cf-6c8ed997733a',
                    salesforce_abbreviation='University Phys (Calc)',
                    salesforce_name='University Physics',
                    subject=subject,
                    description="Test Book",
                    )
        self.assertEqual(book.salesforce_abbreviation, 'University Phys (Calc)')

    def test_allowed_subpages(self):
        self.assertAllowedSubpageTypes(BookIndex, {
            Book
        })

