from pages.base_page_ import Page

class MainPage(Page):

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')