from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Авторизация
def test02_function():

    # Инициализация драйвера

    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)

    # пункт 1: Перейти в раздел Test cases
    driver.get('https://allure.x5.ru/project/123/test-cases?treeId=419')
    driver.implicitly_wait(10)
    login_field = driver.find_element('name', 'username')
    login_field.click()
    login_field.send_keys('Ariadna.Kraynova')
    password_field = driver.find_element('name', 'password')

    password_field.click()
    password_field.send_keys('Qwerty12345!')
    button = driver.find_element('xpath', '//button')
    button.click()

    # пункт 2: Проверить, что выбран вид отображения кейсов Features
    def check_exists_Features():
        try:
            driver.find_element('xpath', "//span[text()='Features']")
        except NoSuchElementException:
            return False
        return True
    check_exists_Features()

    # пункт 3: Проверить, что тест-кейсы на странице отображаются в папках
    def check_exists_folders():
        try:
            driver.find_element('xpath', "//ul[@class = 'LoadableTree__view']//li[last()-1]//div[@class = 'GroupIcon']//*[@class='Icon Icon_size_tiny ']")
        except NoSuchElementException:
            return False
        return True
    check_exists_folders()

    # пункт 4: Изменить вид отображения кейсов на Test-cases
    case_display_switch = driver.find_element('xpath', "//div[@class = 'LoadableTreeViewToggle__arrow']//*[@class = 'Icon Icon_size_small angle angle-down Arrow Arrow_expanded_bottom ']")
    case_display_switch.click()
    type_test_cases = driver.find_element('xpath', "//div[@class = 'tippy-content']//div[last()-1]")
    type_test_cases.click()

    # пункт 5: Проверить, что меняется заголовок на Test-cases
    def check_exists_test_cases():
        try:
            driver.find_element('xpath', "//span[text()='Test cases']")
        except NoSuchElementException:
            return False
        return True
    check_exists_test_cases()

    # пункт 6: Проверить, что и на странице отображаются тест-кейсы без папок
    def check_exists_no_folders():
        try:
            driver.find_element('xpath',"//ul[@class = 'LoadableTree__view']//li[last()-1]//div[@class = 'GroupIcon']//*[@class='Icon Icon_size_tiny ']")
        except NoSuchElementException:
            return False
        return True
    check_exists_no_folders()
    input('Press ENTER to exit')

test02_function()

