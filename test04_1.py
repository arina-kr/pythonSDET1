from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Авторизация
def test04_1_function():

    # Инициализация драйвера

    chrome_options = Options()
    chrome_options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)

    # пункт 1: Перейти в раздел Test cases
    driver.get('https://allure.x5.ru/project/123/test-cases?treeId=419')
    driver.implicitly_wait(10)
    login_field = driver.find_element('name', 'username')
    login_field.click()
    login_field.send_keys('Ariadna.Kraynova')
    password_field = driver.find_element('name', 'password')

    password_field.click()
    password_field.send_keys('Asdasd12345!')
    button = driver.find_element('xpath', '//button')
    button.click()

    # пункт 2: Сделать комбинированную фильтрацию. Выбрать Layer: UI тест и status: Active

    case_filter = driver.find_element('xpath', "//*[@class = 'TestCaseTreeContainer__controls']//button")
    case_filter.click()

    new_filter = driver.find_element('xpath',"//div[@class = 'SavedFilters__title']//button[@class = 'Button Button_size_small Button_style_default Button_shape_round ']")
    new_filter.click()

    # Выбрать Layer: UI тест
    driver.implicitly_wait(10)
    ui_tests_checkbox = driver.find_element('xpath', "//*[@class = 'FilterGroup']//fieldset[last()]//li[last()-2]//*[@class = 'Checkbox FilterChoice__checkbox']")
    ui_tests_checkbox.click()

    # Фильтрация по status: Active
    active_checkbox = driver.find_element('xpath', "//span[text() = 'Active']")
    active_checkbox.click()

    # Проверить, что фильтрация работает
    def check_ui_and_active():
        try:
            driver.find_element('xpath',"//*[@class = 'FilterGroup']//fieldset[last()-2]//li[last()-21]//*[@class = 'Icon Icon_size_tiny Checkbox__icon Checkbox__icon_highlighted']") and driver.find_element('xpath',"//*[@class = 'FilterGroup']//fieldset[last()]//li[last()-2]//*[@class = 'Icon Icon_size_tiny Checkbox__icon Checkbox__icon_highlighted']")
        except NoSuchElementException:
            return False
        return True

    check_ui_and_active()

    input('Press ENTER to exit')


test04_1_function()