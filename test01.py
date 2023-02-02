from selenium import webdriver


# Авторизация
def test01_function():
    # Инициализация драйвера
    # driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)

    # пункт 1: Открыть главную страницу https://allure.x5.ru/project/123/dashboards
    driver.get('https://allure.x5.ru/project/123/dashboards')
    driver.implicitly_wait(10)
    login_field = driver.find_element('name', 'username')
    login_field.click()
    login_field.send_keys('Ariadna.Kraynova')
    password_field = driver.find_element('name', 'password')
    password_field.click()
    password_field.send_keys('Qwerty12345!')
    button = driver.find_element('xpath', '//button')
    button.click()

    # пункт 2: Перейти в раздел Test cases
    testcases_icon = driver.find_element('name', 'test-cases-icon')
    testcases_icon.click()

    # пункт 3: Проверить, что url содержит значение /test-cases
    url = driver.current_url
    assert '/test-cases' in url

    # пункт 4: Вернуться на главную страницу при помощи встроенных инструментов навигации браузера
    driver.execute_script("window.history.go(-1)")

    input('Press ENTER to exit')


test01_function()
