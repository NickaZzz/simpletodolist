from django.conf import settings
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session


class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        
        if self.staging_server:
            session_key = create_session_on_server(self.staging_server, email)
        else:
            session_key = create_pre_authenticated_session(email)
        ## Set cookies that are needed for the first visit to the domain
        ## 404 pages load the fastest
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/'
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_out(email)

        # Эдит является зарегистрированным пользователем
        self.create_pre_authenticated_session(email)
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_in(email)

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Эдит является зарегистрированным пользователем
        self.create_pre_authenticated_session('edith@example.com')

        # Эдит открывает домашнюю страницу и начинает новый список
        self.browser.get(self.live_server_url)
        self.add_list_item('First item')
        self.add_list_item('Second item')
        first_list_url = self.browser.current_url

        # Она замечает ссылку на "Мои списки" в первый раз.
        self.browser.find_element_by_link_text('My lists').click()

        # Она видит, что её список находится там, и он назван
        # на основе первого элемента списка
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('First item')
        )
        self.browser.find_element_by_link_text('First item').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)  
        )

        # Она решеает начать ещё один список, чтобы только убедиться
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Под заголовком "Мои списки" появляется ее новый список
        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )

        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # Она выходит из системы. Опция "Мои списки" исчезает
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        ))
