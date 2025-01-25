from selenium.webdriver.common.by import By


#class TextBoxPageLocators:

    #formfields

#    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
#    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
#    CURRENT_ADDRESS =(By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
 #   PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
 #   SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #created form
#CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
 #   CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
  #  CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
   # CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

#DOCUMENTS
#checkbox
class CheckBoxPageLocators:
    ALL_ELEMENT = (By.XPATH, '(//input[@class="PrivateSwitchBase-input css-j8yymo"])[1]')
    ONE_ELEMENT = (By.XPATH, '(//input[@class="PrivateSwitchBase-input css-j8yymo"])[2]')
    TWO_ELEMENT = (By.XPATH, '(//input[@class="PrivateSwitchBase-input css-j8yymo"])[3]')
    THREE_ELEMENT = (By.XPATH, '(//input[@class="PrivateSwitchBase-input css-j8yymo"])[4]')
    FOUR_ELEMENT = (By.XPATH, '(//input[@class="PrivateSwitchBase-input css-j8yymo"])[5]')
    FIVE_ELEMENT = (By.XPATH, '(//input[@class="PrivateSwitchBase-input css-j8yymo"])[6]')

    CHECKED_SELECT_NO_ALL_ELEMENT = (By.CSS_SELECTOR, 'span[class="MuiButtonBase-root MuiCheckbox-root MuiCheckbox-indeterminate MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-indeterminate MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium MuiCheckbox-root MuiCheckbox-indeterminate MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium sc-KXCwU bvhRWD css-d771x4"]')
    CHECKED_SELECT_ALL_ELEMENT = (By.CSS_SELECTOR, 'span[class="MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium Mui-checked MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium sc-KXCwU bvhRWD css-d771x4"]')

class SearchInputPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[class="search__input"]')


class SearchFiltersPageLocators:
    ADVANCED_SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class="center-vertical expand"]')
    ID_MEETING_INPUT = (By.CSS_SELECTOR, 'input[placeholder="id xxxx"]')
    FULL_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введіть Найменування або ПІБ"]')
    IPN_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введіть цифри"]')
    NAME_COMPANY_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введіть частину назви"]')
    TYPE_DOCUMENT_BUTTON = (By.XPATH, "//span[text()='Оберіть тип']")
    OPTION_ONE = (By.XPATH, "//div[text()='Опція 1']")
    CHECK_ONE_OPTION = (By.XPATH,"//span[text()='Опція 1'] ")
    OPTION_TWO = (By.XPATH, "//div[text()='Опція 2']")
    CHECK_TWO_OPTION = (By.XPATH, "//span[text()='Опція 2'] ")
    STATUS_BUTTON = (By.XPATH, "//span[text()='Оберіть статус']")
    CREATE_DATE = (By.XPATH, '(//div[@class="center-vertical pointer inputWrapper__container inputWrapper__dateRange"])[1]')
    CHANGE_DATE = (By.XPATH, '(//div[@class="center-vertical pointer inputWrapper__container inputWrapper__dateRange"])[2]')
    DAYS_DATE = (By.CSS_SELECTOR, 'span[class="rdrDayNumber"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[class="closeButton"]')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'button[class="button__button mr-3 primary medium"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class="button__button danger medium"]')

class InAndOutDocumentsLocators:
    OUT_DOCUMENTS_BUTTON = (By.XPATH, "//div[text()='Вихідні']")
    IN_DOCUMENTS_BUTTON = (By.XPATH, "//div[text()='Вхідні']")
    FULL_SECTION_TABLE = (By.CSS_SELECTOR, 'thead[class="table__thead flex-column"]')

class NumberSeeDocumentsLocators:
    CLICK_SEE_5 = (By.XPATH, "//button[text()='5']")
    CLICK_SEE_10 = (By.XPATH, "//button[text()='10']")
    CLICK_SEE_20 = (By.XPATH, "//button[text()='20']")
    CHECKED_SEE_DOCUMENTS = (By.CSS_SELECTOR, 'tr[class="pointer"]')

class NumberPageDocumentsLocators:
    PAGE_1 = (By.XPATH, "//button[text()='1']")
    PAGE_2 = (By.XPATH, "//button[text()='2']")
    PAGE_3 = (By.XPATH, "//button[text()='3']")
    BUTTON_NEXT_PAGE = (By.CSS_SELECTOR, 'button[class="next  center"]')
    BUTTON_PREV_PAGE = (By.CSS_SELECTOR, 'button[class="prev  center"]')
    CHECK_SELECT_PAGE = (By.CSS_SELECTOR, 'button[class="paginator__activePage"]')

class ActionsDocumentsPageLocators:
    # ВХІДНІ документи
    ACTION_BUTTON = (By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-auoq4t"]')
    VIEW_BUTTON = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(1)')
    DUPLICATE_BUTTON = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(2)')
    SIGN_BUTTON = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(3)')
    SEND_IN_CD_BUTTON = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(4)')
    HISTORY_BUTTON = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(5)')
    DELETE_BUTTON = (By.XPATH, '(//li[@class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-5dycmn"])[6]')
    # ВИХІДНІ документи
    VIEW_BUTTON_OUTPUT = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(1)')
    RELATED_DOCUMENT_BUTTON_OUTPUT = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(2)')
    DUPLICATE_BUTTON_OUTPUT = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(3)')
    SIGN_BUTTON_OUTPUT = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(4)')
    SEND_IN_CD_BUTTON_OUTPUT = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(5)')
    HISTORY_BUTTON_OUTPUT = (By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-5dycmn:nth-of-type(6)')
    DELETE_BUTTON_OUTPUT = (By.XPATH, '(//li[@class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-5dycmn"])[7]')

#Community
class CommunityPageLocators:
    SEARCH_INPUT_COMMUNITY = (By.CSS_SELECTOR, 'input[type="text"]')
    EXPORT_BUTTON = (By.CSS_SELECTOR, 'button[class="communityPage__btn center"]')

    ADD_COMMUNITY_BUTTON = (By.CSS_SELECTOR, 'button[class="communityPage__btnCommunity center-vertical"]')
    SEARCH_INPUT_EDRPOU = (By.CSS_SELECTOR, 'input[placeholder="Введіть ЄДРПОУ"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class="button__button ml-3 danger"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[tabindex="0"]')
#СПИСОК товариств
    OPEN_INFO_ONE_BUTTON = (By.XPATH, '(//div[@class="accordion__icon"])[1]')
    OPEN_INFO_TWO_BUTTON = (By.XPATH, '(//span[@class="communityPage__span"])[6]')
    OPEN_INFO_THREE_BUTTON = (By.XPATH, '(//div[@class="accordion__icon"])[6]')

    MEMBER_INFO = (By.XPATH, '//div[text()="Учасник"]')
    MANAGER_INFO = (By.XPATH, "//div[text()='Розпорядник']")
    FIRST_PERSON_INFO = (By.XPATH, '//div[text()="Перша особа"]')

    CREATE_VITYAG_BUTTON_FOR_FIRST = (By.XPATH,'(//button[@class="button__button communityPage__addButton dark medium"])[1]')
    EDIT_ANKETA_BUTTON = (By.CSS_SELECTOR, 'button[class="button__button gray medium"]')
#ЧЕК НАЗВАНИЙ
    # ПЕРВОЕ ТОВАРИСТВО
    #Учасник
    CHECK_ROLE = (By.XPATH, "//label[@class='communityPage__label' and text()='Роль']")
    CHECK_SHARE = (By.XPATH, "//label[@class='communityPage__label' and text()='Ваша частка']")
    CHECK_MANAGER = (By.XPATH, "//label[@class='communityPage__label' and text()='Розпорядник']")
    CHECK_ACCOUNT_MANAGER = (By.XPATH, "//label[@class='communityPage__label' and text()='Керуючий рахунком']")
    CHECK_SIGNATURE_SYSTEM = (By.XPATH, "//label[@class='communityPage__label' and text()='Система підписів']")
    ALL_MANAGER_BUTTON_FOR_MEMBER = (By.XPATH, '(//button[text()="Всі розпорядники"])[1]')
    #Розпорядник
    CHECK_ROLE_MANAGER = (By.XPATH, "(//label[@class='communityPage__label' and text()='Роль'])[2]")
    CHECK_MEMBER_MANAGER = (By.XPATH, "(//label[@class='communityPage__label' and text()='Учасник'])[1]")
    CHECK_SIGNATURE_SYSTEM_MANAGER = (By.XPATH, "(//label[@class='communityPage__label' and text()='Система підписів'])[2]")
    ALL_MEMBER_BUTTON_FOR_MANAGER = (By.XPATH, '(//button[text()="Всі учасники"])[1] ')
    #Перша особа
    CHECK_ROLE_FIRST_PERSON = (By.XPATH, "(//label[@class='communityPage__label' and text()='Роль'])[3]")
    CHECK_MEMBER_FIRST_PERSON = (By.XPATH, "(//label[@class='communityPage__label' and text()='Учасник'])[2]")
    CHECK_SIGNATURE_FIRST_PERSON = (By.XPATH, "(//label[@class='communityPage__label' and text()='Система підписів'])[3]")
    ALL_MEMBER_BUTTON_FOR_FIRST_PERSON = (By.XPATH, '(//button[text()="Всі учасники"])[2]')

    # ВТОРОЕ ТОВАРИСТВО
    CREATE_VITYAG_BUTTON_FOR_SECOND = (By.XPATH, '(//button[@class="button__button communityPage__addButton dark medium"])[2]')
    CHECK_NAME = (By.XPATH, '(//label[text()="Найменування"])[2]')
    CHECK_EDRPOU = (By.XPATH, '(//label[text()="ЄДРПОУ"])[2]')
    CHECK_ROLE_SECOND = (By.XPATH, '(//label[text()="Роль"])[4]')
    CHECK_ACCOUNT_MANAGER_SECOND = (By.XPATH, '(//label[text()="Керуючий рахунком"])[2]  ')
    CHECK_MANAGER_FROM_ACCOUNT_MANAGER = (By.XPATH, '(//label[text()="Розпорядник від Керуючого рахунком"])[1]  ')
    CHECK_MEMBER_SECOND = (By.XPATH, '(//label[text()="Учасник"])[3]')

    ALL_MANAGER_BUTTON_FOR_SECOND = (By.XPATH, '(//button[text()="Всі розпорядники"])[2]')
    ALL_MEMBER_BUTTON_FOR_SECOND = (By.XPATH, '(//button[text()="Всі учасники"])[3]')

    #ТРЕТЬЕ ТОВАРИСТВО
    OTHER_PERSON_BUTTON = (By.XPATH, '(//span[@class="communityPage__span"])[9]')
    CHECK_NAME_THREE = (By.XPATH, '(//label[text()="Найменування"])[3]')
    CHECK_EDRPOU_THREE = (By.XPATH, '(//label[text()="ЄДРПОУ"])[3]')
    CHECK_ROLE_THREE = (By.XPATH, '(//label[text()="Роль"])[5]')
    CHECK_SHARE_THREE = (By.XPATH, '(//label[text()="Ваша частка"])[2] ')












    #EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    #ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    #CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    #TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    #OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

#class RadioButtonPageLocators:
 #   YES = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
  #  IMPRESSIVE = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
   # NO = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    #OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

#class WebTablePageLocators:
    #add_person_form
    #ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
 #   FIRSTNAME_INPUT =(By.CSS_SELECTOR, 'input[id="firstName"]')
  #  LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
   # EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    #AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
   # SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    #DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    #SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #table
    #FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    #search
    #SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    #DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    #ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    #NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
   # COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    #update
    #UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


#class ButtonsPageLocators:
    #DOUBLE_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    #RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    #CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')

    #result
    #SUCCESS_DOUBLE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    #SUCCESS_RIGHT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    #SUCCESS_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


#class LinksPageLocators:
    #SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    #BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')

#class UploadAndDownloadLocators:
    #UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    #UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
