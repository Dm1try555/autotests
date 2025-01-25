import os
import random
import time
from itertools import count
from tabnanny import check

import requests
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import SearchFiltersPageLocators, SearchInputPageLocators, \
    InAndOutDocumentsLocators, CheckBoxPageLocators, NumberSeeDocumentsLocators, NumberPageDocumentsLocators, \
    ActionsDocumentsPageLocators, CommunityPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

#DOCUMENTS
class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def click_all_checkbox(self):
        self.element_is_present(self.locators.ALL_ELEMENT).click()
        time.sleep(5)
        check_all_element = self.element_are_present(self.locators.CHECKED_SELECT_ALL_ELEMENT)
        assert check_all_element != self.locators.CHECKED_SELECT_NO_ALL_ELEMENT

    def click_one_element(self):
        self.element_is_present(self.locators.ONE_ELEMENT).click()
        time.sleep(5)
        check_one_element = self.element_is_present(self.locators.CHECKED_SELECT_NO_ALL_ELEMENT)
        assert check_one_element != self.locators.CHECKED_SELECT_ALL_ELEMENT


class SearchInputPage(BasePage):
    locators = SearchInputPageLocators()

    def click_input_search_and_send(self):
        search_input = self.element_is_visible(self.locators.SEARCH_INPUT)  # Получаем элемент
        search_input.click()  # Кликаем по полю ввода
        text_to_enter = "Депозитарій"
        search_input.send_keys(text_to_enter)  # Вводим текст
        time.sleep(5)
        entered_text = search_input.get_attribute("value")  # Получаем значение из поля ввода
        print(entered_text)  # Печатаем текст
        return entered_text  # Возвращаем текст


class SearchFiltersPage(BasePage):
    locators = SearchFiltersPageLocators()

    def click_on_the_advanced_search(self):
        self.element_is_visible(self.locators.ADVANCED_SEARCH_BUTTON).click()

    def fill_all_fields(self):
        person_info = next(generated_person())
        id_meeting = person_info.id_meeting
        full_name = person_info.full_name
        ipn_of_the_participant = person_info.ipn_of_the_participant
        name_of_the_company = person_info.name_of_the_company
        self.element_is_visible(self.locators.ID_MEETING_INPUT).send_keys(id_meeting)
        self.element_is_visible(self.locators.FULL_NAME_INPUT).send_keys(full_name)
        self.element_is_visible(self.locators.IPN_INPUT).send_keys(ipn_of_the_participant)
        self.element_is_visible(self.locators.NAME_COMPANY_INPUT).send_keys(name_of_the_company)
        self.element_is_visible(self.locators.TYPE_DOCUMENT_BUTTON).click()
        option_one = self.element_is_visible(self.locators.OPTION_ONE)
        option_one.click()
        assert self.element_is_present(self.locators.CHECK_ONE_OPTION)
        self.element_is_visible(self.locators.CHECK_ONE_OPTION).click()
        option_two = self.element_is_visible(self.locators.OPTION_TWO)
        option_two.click()
        assert self.element_is_present(self.locators.CHECK_TWO_OPTION)

        self.element_is_visible(self.locators.STATUS_BUTTON).click()
        option_one = self.element_is_visible(self.locators.OPTION_ONE)
        option_one.click()
        assert self.element_is_present(self.locators.CHECK_ONE_OPTION)
        self.element_is_visible(self.locators.CHECK_ONE_OPTION).click()
        option_two = self.element_is_visible(self.locators.OPTION_TWO)
        option_two.click()
        assert self.element_is_present(self.locators.CHECK_TWO_OPTION)
        return id_meeting, full_name, ipn_of_the_participant, name_of_the_company

    def click_random_date_create(self):
        # Кликнуть на поле выбора даты
        self.element_is_visible(self.locators.CREATE_DATE).click()

        # Найти все доступные даты в календаре
        date_elements = self.elements_are_visible(self.locators.DAYS_DATE)

        # Отфильтровать элементы с числами от 1 до 31
        valid_dates = [elem for elem in date_elements if elem.text.isdigit() and 1 <= int(elem.text) <= 31]

        # Проверить, что есть доступные даты
        if not valid_dates:
            raise Exception("Нет доступных дат для выбора.")

        # Выбрать случайную дату
        random_date = random.choice(valid_dates)

        # Кликнуть на выбранную дату
        random_date.click()
        print(f"Выбрана дата: {random_date.text}")


    def click_random_date_change(self):
        self.element_is_visible(self.locators.CHANGE_DATE).click()

        # Найти все доступные даты в календаре
        date_elements = self.elements_are_visible(self.locators.DAYS_DATE)

        # Отфильтровать элементы с числами от 1 до 31
        valid_dates = [elem for elem in date_elements if elem.text.isdigit() and 1 <= int(elem.text) <= 31]

        # Проверить, что есть доступные даты
        if not valid_dates:
            raise Exception("Нет доступных дат для выбора.")

        # Выбрать случайную дату
        random_date = random.choice(valid_dates)

        # Кликнуть на выбранную дату
        random_date.click()
        print(f"Выбрана дата: {random_date.text}")

    def click_close_button(self):
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.ADVANCED_SEARCH_BUTTON).click()

    def click_cancel_button(self):
        self.element_is_visible(self.locators.CANCEL_BUTTON).click()
        self.element_is_visible(self.locators.ADVANCED_SEARCH_BUTTON).click()

    def click_search_button(self):
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()


class InAndOutDocuments(BasePage):
    locators = InAndOutDocumentsLocators()

    def out_documents(self):
        self.element_is_visible(self.locators.OUT_DOCUMENTS_BUTTON).click()
        section_list = self.element_are_present(self.locators.FULL_SECTION_TABLE)
        data = []
        for item in section_list:
            data.append(item.text.splitlines())
            print(data)
        return data

    def in_documents(self):
        self.element_is_visible(self.locators.IN_DOCUMENTS_BUTTON).click()
        section_list = self.element_are_present(self.locators.FULL_SECTION_TABLE)
        data = []
        for item in section_list:
            data.append(item.text.splitlines())
            print(data)
        return data


class NumberSeeDocuments(BasePage):
    locators = NumberSeeDocumentsLocators()

    def see_5_documents(self):
        self.element_is_visible(self.locators.CLICK_SEE_5).click()
        document_list = self.element_are_present(self.locators.CHECKED_SEE_DOCUMENTS)
        # Проверяем количество элементов
        if len(document_list) != 5:
            print(f"Ожидалось 5 элементов, но найдено {len(document_list)}")
        else:
            print("\n""Найдено ровно 5 элементов, как ожидалось.")
        # assert len(document_list) == 5

        data = []
        # Собираем строки из текста
        for item in document_list:
            data.extend(item.text.splitlines())  # Добавляем строки в общий список

        # Формируем вывод с отступом после каждого 5-го элемента
        formatted_data = []
        for i, line in enumerate(data, start=1):
            formatted_data.append(line)
            if i % 5 == 0:  # После каждого 5-го элемента добавляем пустую строку
                formatted_data.append("")

        # Печатаем данные
        #print("\n".join(formatted_data))
        return formatted_data


    def see_10_documents(self):
        self.element_is_visible(self.locators.CLICK_SEE_10).click()
        document_list = self.element_are_present(self.locators.CHECKED_SEE_DOCUMENTS)
        # Проверяем количество элементов
        if len(document_list) != 10:
            print(f"Ожидалось 10 элементов, но найдено {len(document_list)}")
        else:
            print("\n""Найдено ровно 10 элементов, как ожидалось.")
        # assert len(document_list) == 10

        data = []
        # Собираем строки из текста
        for item in document_list:
            data.extend(item.text.splitlines())  # Добавляем строки в общий список

        # Формируем вывод с отступом после каждого 5-го элемента
        formatted_data = []
        for i, line in enumerate(data, start=1):
            formatted_data.append(line)
            if i % 5 == 0:  # После каждого 5-го элемента добавляем пустую строку
                formatted_data.append("")

        # Печатаем данные
        #print("\n".join(formatted_data))
        return formatted_data

    def see_20_documents(self):
        self.element_is_visible(self.locators.CLICK_SEE_20).click()
        document_list = self.element_are_present(self.locators.CHECKED_SEE_DOCUMENTS)
        # Проверяем количество элементов
        if len(document_list) != 20:
            print(f"Ожидалось 20 элементов, но найдено {len(document_list)}")
        else:
            print("\n""Найдено ровно 20 элементов, как ожидалось.")
        #assert len(document_list) == 20

        data = []
        # Собираем строки из текста
        for item in document_list:
            data.extend(item.text.splitlines())  # Добавляем строки в общий список

        # Формируем вывод с отступом после каждого 5-го элемента
        formatted_data = []
        for i, line in enumerate(data, start=1):
            formatted_data.append(line)
            if i % 5 == 0:  # После каждого 5-го элемента добавляем пустую строку
                formatted_data.append("")

        # Печатаем данные
        #print("\n".join(formatted_data))
        return formatted_data


class NumberPageDocuments(BasePage):
    locators = NumberPageDocumentsLocators()

    def click_number_page(self):

        self.element_is_visible(self.locators.PAGE_2).click()
        check_select =  self.element_is_present(self.locators.CHECK_SELECT_PAGE)
        assert check_select.text == "2", f"Ожидалась активная страница '2', но отображается '{check_select.text}'"
        print("Активная страница корректно отображается: 2")

        self.element_is_visible(self.locators.PAGE_3).click()
        check_select = self.element_is_present(self.locators.CHECK_SELECT_PAGE)
        assert check_select.text == "3", f"Ожидалась активная страница '3', но отображается '{check_select.text}'"
        print("Активная страница корректно отображается: 3")

        self.element_is_visible(self.locators.PAGE_1).click()
        check_select = self.element_is_present(self.locators.CHECK_SELECT_PAGE)
        assert check_select.text == "1", f"Ожидалась активная страница '1', но отображается '{check_select.text}'"
        print("Активная страница корректно отображается: 1")


class ActionsInputDocumentsPage(BasePage):

    locators = ActionsDocumentsPageLocators()

    # ВХІДНІ документи

    def click_view(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        view_button = self.element_is_visible(self.locators.VIEW_BUTTON)
        if view_button:
            view_button.click()
            print('1)Успешно выполнен клик на элемент "Перегляд"')
        else:
            print("Элементы не найдены!")


    def click_duplicate_document(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        duplicate_button = self.element_is_visible(self.locators.DUPLICATE_BUTTON)
        if duplicate_button:
            duplicate_button.click()
            print('2)Успешно выполнен клик на элемент "Дублювати документ"')
        else:
            print("Элементы не найдены!")


    def click_sign_document(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        sign_button = self.element_is_visible(self.locators.SIGN_BUTTON)
        if sign_button:
            sign_button.click()
            print('3)Успешно выполнен клик на элемент "Підписати"')
        else:
            print("Элементы не найдены!")


    def click_send_in_cd(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        send_button = self.element_is_visible(self.locators.SEND_IN_CD_BUTTON)
        if send_button:
            send_button.click()
            print('4)Успешно выполнен клик на элемент "Відправити в ЦД"')
        else:
            print("Элементы не найдены!")


    def click_history_document(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        history_button = self.element_is_visible(self.locators.HISTORY_BUTTON)
        if history_button:
            history_button.click()
            print('5)Успешно выполнен клик на элемент "Історія"')
        else:
            print("Элементы не найдены!")

    def click_delete_document(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        if delete_button:
            delete_button.click()
            print('6)Успешно выполнен клик на элемент "Видалити"')
        else:
            print("Элементы не найдены!")

# ВИХІДНІ документи

    def click_view_output(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        view_button_output = self.element_is_visible(self.locators.VIEW_BUTTON_OUTPUT)
        if view_button_output:
            view_button_output.click()
            print('1)Успешно выполнен клик на элемент "Перегляд"')
        else:
            print("Элементы не найдены!")


    def click_related_document_output(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        related_button_output = self.element_is_visible(self.locators.RELATED_DOCUMENT_BUTTON_OUTPUT)
        if related_button_output:
            related_button_output.click()
            print('2)Успешно выполнен клик на элемент "Пов’язаний документ"')
        else:
            print("Элементы не найдены!")


    def click_duplicate_document_output(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        duplicate_button_output = self.element_is_visible(self.locators.DUPLICATE_BUTTON_OUTPUT)
        if duplicate_button_output:
            duplicate_button_output.click()
            print('3)Успешно выполнен клик на элемент "Дублювати документ"')
        else:
            print("Элементы не найдены!")


    def click_sign_document_output(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        sign_button_output = self.element_is_visible(self.locators.SIGN_BUTTON_OUTPUT)
        if sign_button_output:
            sign_button_output.click()
            print('4)Успешно выполнен клик на элемент "Підписати"')
        else:
            print("Элементы не найдены!")


    def click_send_in_cd_output(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        send_button_output = self.element_is_visible(self.locators.SEND_IN_CD_BUTTON_OUTPUT)
        if send_button_output:
            send_button_output.click()
            print('5)Успешно выполнен клик на элемент "Відправити в ЦД"')
        else:
            print("Элементы не найдены!")


    def click_history_document_output(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        history_button_output = self.element_is_visible(self.locators.HISTORY_BUTTON_OUTPUT)
        if history_button_output:
            history_button_output.click()
            print('6)Успешно выполнен клик на элемент "Історія"')
        else:
            print("Элементы не найдены!")


    def click_delete_document_output(self):
        self.element_is_visible(self.locators.ACTION_BUTTON).click()
        delete_button_output = self.element_is_visible(self.locators.DELETE_BUTTON_OUTPUT)
        if delete_button_output:
            delete_button_output.click()
            print('7)Успешно выполнен клик на элемент "Видалити"')
        else:
            print("Элементы не найдены!")


class CommunityPage(BasePage):
    locators = CommunityPageLocators()

    def search_input(self):
        search_input = self.element_is_visible(self.locators.SEARCH_INPUT_COMMUNITY)
        search_input.click()
        text_to_enter = "Депозитарій"
        search_input.send_keys(text_to_enter)
        time.sleep(5)
        entered_text = search_input.get_attribute("value")  # Получаем значение из поля ввода
        print(entered_text)
        return entered_text

    def click_export(self):
        self.element_is_visible(self.locators.EXPORT_BUTTON).click()

    def add_community(self):
        self.element_is_visible(self.locators.ADD_COMMUNITY_BUTTON).click()
        search_input = self.element_is_visible(self.locators.SEARCH_INPUT_EDRPOU)
        text_to_enter = "Депозитарій"
        search_input.send_keys(text_to_enter)
        time.sleep(5)
        entered_text = search_input.get_attribute("value")  # Получаем значение из поля ввода
        print(entered_text)
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()
        return entered_text

    def click_edit_anketa(self):
        anketa = self.element_is_visible(self.locators.EDIT_ANKETA_BUTTON)
        if anketa:
            anketa.click()
            print('Успешно выполнен клик на элемент "Зміна анкети рахунка"')
        else:
            print('Клик на элемент не сработал')

    def click_create_vityag(self):
        vityag = self.element_is_visible(self.locators.CREATE_VITYAG_BUTTON_FOR_FIRST)
        if vityag:
            vityag.click()
            print('Успешно выполнен клик на элемент "Сформувати витяг"')
        else:
            print('Клик на элемент не сработал')
#УЧАСНИК
    def additional_info_about_first_community_member(self):
        self.element_is_visible(self.locators.OPEN_INFO_ONE_BUTTON).click()
        member = self.element_is_visible(self.locators.MEMBER_INFO)
        if member:
            member.click()
            print('Клик открыл доп инфу')
        else:
            print('Клик на элемент не сработал')

        label_elements = (
            self.element_is_visible(self.locators.CHECK_ROLE),
            self.element_is_visible(self.locators.CHECK_SHARE),
            self.element_is_visible(self.locators.CHECK_MANAGER),
            self.element_is_visible(self.locators.CHECK_ACCOUNT_MANAGER),
            self.element_is_visible(self.locators.CHECK_SIGNATURE_SYSTEM)
        )

        for element in label_elements:
            if element:
                print(f"Название: {element.text}")
            else:
                print("Элемент не найден.")
        return label_elements

    def click_all_manager(self):
        self.element_is_visible(self.locators.OPEN_INFO_ONE_BUTTON).click()
        self.element_is_visible(self.locators.MEMBER_INFO).click()
        all_manager_button = self.element_is_visible(self.locators.ALL_MANAGER_BUTTON_FOR_MEMBER)
        if all_manager_button:
            all_manager_button.click()
            print('Клик открыл "Всі розпорядники"')
        else:
            print('Клик на элемент не сработал')
#РОЗПОРЯДНИК
    def additional_info_about_first_community_manager(self):
        self.element_is_visible(self.locators.OPEN_INFO_ONE_BUTTON).click()
        manager = self.element_is_visible(self.locators.MANAGER_INFO)
        if manager:
            manager.click()
            print('Клик открыл доп инфу')
        else:
            print('Клик на элемент не сработал')

        label_elements = (
            self.element_is_visible(self.locators.CHECK_ROLE_MANAGER),
            self.element_is_visible(self.locators.CHECK_MEMBER_MANAGER),
            self.element_is_visible(self.locators.CHECK_SIGNATURE_SYSTEM_MANAGER)
        )

        for element in label_elements:
            if element:
                print(f"Название: {element.text}")
            else:
                print("Элемент не найден.")
        return label_elements

    def click_all_member_for_manager(self):
        self.element_is_visible(self.locators.OPEN_INFO_ONE_BUTTON).click()
        self.element_is_visible(self.locators.MANAGER_INFO).click()
        all_member_button = self.element_is_visible(self.locators.ALL_MEMBER_BUTTON_FOR_MANAGER)
        if all_member_button:
            all_member_button.click()
            print('Клик открыл "Всі учасники"')
        else:
            print('Клик на элемент не сработал')

#ПЕРША ОСОБА
    def additional_info_about_first_community_first_person(self):
        self.element_is_visible(self.locators.OPEN_INFO_ONE_BUTTON).click()
        first_person = self.element_is_visible(self.locators.FIRST_PERSON_INFO)
        if first_person:
            first_person.click()
            print('Клик открыл доп инфу')
        else:
            print('Клик на элемент не сработал')

        label_elements = (
            self.element_is_visible(self.locators.CHECK_ROLE_FIRST_PERSON),
            self.element_is_visible(self.locators.CHECK_MEMBER_FIRST_PERSON),
            self.element_is_visible(self.locators.CHECK_SIGNATURE_FIRST_PERSON)
        )

        for element in label_elements:
            if element:
                print(f"Название: {element.text}")
            else:
                print("Элемент не найден.")
        return label_elements

    def click_all_member_for_first_person(self):
        self.element_is_visible(self.locators.OPEN_INFO_ONE_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_PERSON_INFO).click()
        all_member_button = self.element_is_visible(self.locators.ALL_MEMBER_BUTTON_FOR_FIRST_PERSON)
        if all_member_button:
            all_member_button.click()
            print('Клик открыл "Всі учасники"')
        else:
            print('Клик на элемент не сработал')

# ВТОРОЕ ТОВАРИСТВО
    def click_create_vityag_for_second(self):
        vityag = self.element_is_visible(self.locators.CREATE_VITYAG_BUTTON_FOR_SECOND)
        if vityag:
            vityag.click()
            print('Успешно выполнен клик на элемент "Сформувати витяг"')
        else:
            print('Клик на элемент не сработал')

    def  additional_info_about_second_community(self):
        info = self.element_is_visible(self.locators.OPEN_INFO_TWO_BUTTON)
        if info:
            info.click()
            print('Клик открыл доп инфу')
        else:
            print('Клик на элемент не сработал')

        label_elements = (
            self.element_is_visible(self.locators.CHECK_NAME),
            self.element_is_visible(self.locators.CHECK_EDRPOU),
            self.element_is_visible(self.locators.CHECK_ROLE_SECOND),
            self.element_is_visible(self.locators.CHECK_ACCOUNT_MANAGER_SECOND),
            self.element_is_visible(self.locators.CHECK_MANAGER_FROM_ACCOUNT_MANAGER),
            self.element_is_visible(self.locators.CHECK_MEMBER_SECOND)
        )

        for element in label_elements:
            if element:
                print(f"Название: {element.text}")
            else:
                print("Элемент не найден.")
        return label_elements

    def click_all_manager_for_second(self):
        self.element_is_visible(self.locators.OPEN_INFO_TWO_BUTTON).click()
        all_manager_button = self.element_is_visible(self.locators.ALL_MANAGER_BUTTON_FOR_SECOND)
        if all_manager_button:
            all_manager_button.click()
            print('Клик открыл "Всі розпорядники"')
        else:
            print('Клик на элемент не сработал')

    def click_all_member_for_second(self):
        self.element_is_visible(self.locators.OPEN_INFO_TWO_BUTTON).click()
        all_member_button = self.element_is_visible(self.locators.ALL_MEMBER_BUTTON_FOR_SECOND)
        if all_member_button:
            all_member_button.click()
            print('Клик открыл "Всі учасники"')
        else:
            print('Клик на элемент не сработал')

#ТРЕТЬЕ ТОВАРИСТВО
    def  additional_info_about_three_community(self):
        self.element_is_visible(self.locators.OPEN_INFO_THREE_BUTTON).click()
        info = self.element_is_visible(self.locators.OTHER_PERSON_BUTTON)
        if info:
            info.click()
            print('Клик открыл доп инфу')
        else:
            print('Клик на элемент не сработал')

        label_elements = (
            self.element_is_visible(self.locators.CHECK_NAME_THREE),
            self.element_is_visible(self.locators.CHECK_EDRPOU_THREE),
            self.element_is_visible(self.locators.CHECK_ROLE_THREE),
            self.element_is_visible(self.locators.CHECK_SHARE_THREE)
        )

        for element in label_elements:
            if element:
                print(f"Название: {element.text}")
            else:
                print("Элемент не найден.")
        return label_elements



















