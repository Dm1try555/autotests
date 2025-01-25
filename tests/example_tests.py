import random
import time
from conftest import driver
from pages.example_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, UploadAndDownloadPage


class TestTextBox:

    def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            print(full_name, email, current_address, permanent_address)
            print(output_name, output_email, output_current_address, output_permanent_address)
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_current_address
            assert permanent_address == output_permanent_address


class TestCheckBox:
    def test_check_box(self,driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkbox()
        output_result = check_box_page.get_output_result()
        print(input_checkbox)
        print(output_result)
        assert input_checkbox == output_result, 'checkboxes have not been selected'

class TestRadioButton:

    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes'
        assert output_impressive == 'Impressive'
        assert output_no == 'No'


class TestWebTable:

    def test_web_table_add_person(self,driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_person()
        print(new_person)
        print(table_result)
        assert new_person in  table_result

    def test_web_table_search_person(self,driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0,5)]
        web_table_page.search_person(key_word)
        table_result = web_table_page.check_search_person()
        print(key_word)
        print(table_result)
        assert any(key_word in row for row in table_result)


    def test_web_table_update_person_info(self,driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        print(age)
        print(row)
        assert age in row


    def test_web_table_delete_person(self,driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        print (text)
        assert text == text


    def test_web_table_change_count_row(self,driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_up_to_rows()
        print(count)
        assert count == [5, 10, 20, 25, 50, 100]



class TestButtonsPage:

    def test_different_click_on_the_buttons(self,driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        double = button_page.click_on_different_button('double')
        right = button_page.click_on_different_button('right')
        click = button_page.click_on_different_button('click')
        print(double)
        print(right)
        print(click)
        assert double == 'You have done a double click'
        assert right == 'You have done a right click'
        assert click == 'You have done a dynamic click'


class TestLinkPage:

    def test_check_link(self,driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        print(href_link,current_url)


    def test_broken_link(self,driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
        print(response_code)
        assert response_code == 400


class TestUploadAndDownload:

    def test_upload_file(self,driver):
        upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_download_page.open()
        file_name, result = upload_download_page.upload_file()
        print(file_name)
        print(result)
        assert file_name == result


    def test_download_file(self,driver):
        pass














