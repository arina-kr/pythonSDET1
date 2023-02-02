from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Авторизация
def test04_function():

    # Инициализация драйвера
    # driver = webdriver.Chrome()

    #options = webdriver.ChromeOptions()
    #options.add_argument('ignore-certificate-errors')
    #driver = webdriver.Chrome(chrome_options=options)

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

    # пункт 2: Навести курсор на иконку фильтрации. Проверить что появляется попап
    case_filter = driver.find_element('xpath', "//*[@class = 'TestCaseTreeContainer__controls']//button")
    ActionChains(driver).move_to_element(case_filter).perform()

    def check_exists_icon_filter():
        try:
            driver.find_element('xpath', "//div[@class = 'tippy-popper']")
        except NoSuchElementException:
            return False
        return True
    check_exists_icon_filter()

    # пункт 3: Нажать на кнопку фильтрации
    case_filter.click()

    # пункт 4: Нажать на +
    new_filter = driver.find_element('xpath', "//div[@class = 'SavedFilters__title']//button[@class = 'Button Button_size_small Button_style_default Button_shape_round ']")
    new_filter.click()

    # пункт 5: Отфильтровать тест-кейсы по статусу Review и проверить, что фильтрация работает
    status_review = driver.find_element('xpath', "//span[text() = 'Review']")
    status_review.click()

    def check_review():
        try:
            driver.find_element('xpath',"//ul[@class = 'list']//li[last()-2]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon Checkbox__icon_highlighted']") and driver.find_element('xpath',"//ul[@class = 'list']//li[last()-21]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon']") and driver.find_element('xpath',"//ul[@class = 'list']//li[last()-15]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon']") and driver.find_element('xpath',"//ul[@class = 'list']//li[last()-7]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon']")
        except NoSuchElementException:
            return False
        return True

    check_review()

    # пункт 6: Отфильтровать тест-кейсы по тегу: ввести значение regress. Нажать на Enter.
    #status_review = driver.find_element('xpath', "//span[text() = 'Review']")
    #status_review.click()

    #filter_tag = driver.find_element('xpath', "//*[@class = 'FilterGroup']//label[last()-6]//*[@class = ' css-129fuww-control']")
    #filter_tag.click()
    #time.sleep(5)
    #filter_tag.send_keys('regress')
    #filter_tag.key_down(Keys.ENTER)



    input('Press ENTER to exit')

test04_function()