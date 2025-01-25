import random
import time
from conftest import driver
from pages.elements_page import CheckBoxPage, SearchFiltersPage, SearchInputPage, InAndOutDocuments, NumberSeeDocuments, \
    NumberPageDocuments, ActionsInputDocumentsPage, CommunityPage


#DOCUMENTS
class TestCheckBox:
   def test_check_box(self,driver):
       check_box = CheckBoxPage(driver, 'https://competent-volhard-77625e.netlify.app/documents')
       check_box.open()
       check_box.click_all_checkbox()
       check_box.click_one_element()


class TestSearchInput:
    def test_search_input(self,driver):
        search_input = SearchInputPage(driver, 'https://competent-volhard-77625e.netlify.app/documents')
        search_input.open()
        search_input.click_input_search_and_send()


class TestSearchFilters:
    def test_search_filters(self,driver):
        search_page = SearchFiltersPage(driver, 'https://competent-volhard-77625e.netlify.app/documents')
        search_page.open()
        search_page.click_on_the_advanced_search()
        fill_all_fields = search_page.fill_all_fields()
        print(fill_all_fields)
        search_page.click_random_date_create()
        search_page.click_random_date_change()
        search_page.click_close_button()
        search_page.click_cancel_button()
        search_page.click_search_button()


class TestInAndOutDocuments:
    def test_display_in_and_out_documents(self,driver):
        in_and_out_page = InAndOutDocuments(driver, 'https://competent-volhard-77625e.netlify.app/documents')
        in_and_out_page.open()
        out_section = in_and_out_page.out_documents()
        time.sleep(2)
        assert out_section == [['ДОКУМЕНТ', 'СТАТУС', 'ДАТА', 'УЧАСНИК', 'ТОВ/ТДВ']]
        in_section = in_and_out_page.in_documents()
        assert in_section == [['ДОКУМЕНТ', 'ДАТА', 'УЧАСНИК', 'ТОВ/ТДВ']]

    



class TestNumberSeeElements:
    def test_number_see_elements(self,driver):
        number_see_page = NumberSeeDocuments(driver, 'https://competent-volhard-77625e.netlify.app/documents')
        number_see_page.open()
        number_see_page.see_5_documents()
        number_see_page.see_10_documents()
        number_see_page.see_20_documents()


class TestPagination:
    def test_number_page(self,driver):
        number_page = NumberPageDocuments(driver, 'https://competent-volhard-77625e.netlify.app/documents')
        number_page.open()
        number_page.click_number_page()

class TestActionsDocuments:
    # ВХІДНІ документи
    def test_function_actions_input_documents(self,driver):
        function_actions = ActionsInputDocumentsPage(driver, 'https://competent-volhard-77625e.netlify.app/documents')
        function_actions.open()
        print("ВХІДНІ документи:")
        function_actions.click_view()
        function_actions.click_duplicate_document()
        function_actions.click_sign_document()
        function_actions.click_send_in_cd()
        function_actions.click_history_document()
        function_actions.click_delete_document()
    #ВИХІДНІ документи
    def test_function_actions_output_documents(self,driver):
        function_actions = ActionsInputDocumentsPage(driver, 'https://competent-volhard-77625e.netlify.app/documents?tableMode=OUTCOME')
        function_actions.open()
        print("ВИХІДНІ документи:")
        function_actions.click_view_output()
        function_actions.click_related_document_output()
        function_actions.click_duplicate_document_output()
        function_actions.click_sign_document_output()
        function_actions.click_send_in_cd_output()
        function_actions.click_history_document_output()
        function_actions.click_delete_document_output()

#ТОВАРИСТВА
class TestCommunity:
    def test_search_input(self, driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.search_input()

    def test_export(self, driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_export()

    def test_add_community(self, driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.add_community()
#ПЕРВОЕ ТОВАРИСТВО
    # УЧАСНИК
    def test_list_community_first_member(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_edit_anketa()
        search_input.click_create_vityag()
        result = search_input.additional_info_about_first_community_member()
        # Извлекаем текст из каждого элемента
        result_texts = [element.text for element in result]

        # Ожидаемый результат
        valid_results = ['Роль', 'Ваша частка', 'Розпорядник', 'Керуючий рахунком', 'Система підписів']

        # Проверяем совпадение текстов
        assert result_texts == valid_results, f"Результаты {result_texts} не совпадают с ожидаемыми {valid_results}"

    def test_list_community_first_click_member_all_manager(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_all_manager()
        time.sleep(2)

    # РОЗПОРЯДНИК
    def test_list_community_first_manager(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        result = search_input.additional_info_about_first_community_manager()
        # Извлекаем текст из каждого элемента
        result_texts = [element.text for element in result]

        # Ожидаемый результат
        valid_results = ['Роль', 'Учасник', 'Система підписів']

        # Проверяем совпадение текстов
        assert result_texts == valid_results, f"Результаты {result_texts} не совпадают с ожидаемыми {valid_results}"

    def test_list_community_first_click_all_member_for_manager(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_all_member_for_manager()
        time.sleep(2)

    # ПЕРША ОСОБА
    def test_list_community_first_first_person(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        result = search_input.additional_info_about_first_community_first_person()
        # Извлекаем текст из каждого элемента
        result_texts = [element.text for element in result]

        # Ожидаемый результат
        valid_results = ['Роль', 'Учасник', 'Система підписів']

        # Проверяем совпадение текстов
        assert result_texts == valid_results, f"Результаты {result_texts} не совпадают с ожидаемыми {valid_results}"

    def test_list_community_first_click_all_member_for_first_person(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_all_member_for_first_person()
        time.sleep(2)
#ВТОРОЕ ТОВАРИСТВО
    def test_list_community_second(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_create_vityag_for_second()
        result = search_input.additional_info_about_second_community()
# Извлекаем текст из каждого элемента
        result_texts = [element.text for element in result]

        # Ожидаемый результат
        valid_results = ['Найменування', 'ЄДРПОУ', 'Роль', 'Керуючий рахунком', 'Розпорядник від Керуючого рахунком', 'Учасник']

        # Проверяем совпадение текстов
        assert result_texts == valid_results, f"Результаты {result_texts} не совпадают с ожидаемыми {valid_results}"

    def test_list_community_second_click_all_manager(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_all_manager_for_second()
        time.sleep(2)

    def test_list_community_second_click_all_member(self,driver):
        search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        search_input.open()
        search_input.click_all_member_for_second()
        time.sleep(2)

#ТРЕТЬЕ ТОВАРИСТВО
    #def test_list_community_three(self,driver):
       # search_input = CommunityPage(driver, 'https://competent-volhard-77625e.netlify.app/community')
        #search_input.open()
       # result = search_input.additional_info_about_three_community()
# Извлекаем текст из каждого элемента
       # result_texts = [element.text for element in result]

        # Ожидаемый результат
        #valid_results = ['Найменування', 'ЄДРПОУ', 'Роль', 'Ваша частка']

        # Проверяем совпадение текстов
        #assert result_texts == valid_results, f"Результаты {result_texts} не совпадают с ожидаемыми {valid_results}"









