from selenium import webdriver

# Авторизация
def test_function():

    # Инициализация драйвера
    # driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)

    # Авторизация
    driver.get('https://allure.x5.ru')
    login_field = driver.find_element('name', 'username')
    login_field.click()
    login_field.send_keys('Ariadna.Kraynova')
    password_field = driver.find_element('name', 'password')
    password_field.click()
    password_field.send_keys('Qwerty12345!')
    button = driver.find_element('xpath', '//button')
    button.click()

    # Получаем список проектов и их названия
    projects = driver.find_elements('css selector', "div.ProjectRow__name a")
    projects_names = [element.text for element in projects]

    # Проверяем, входит ли значение в список
    assert 'Пятёрочка Доставка' in projects_names

    # Остановка драйвера, освобождение ресурсов
    driver.quit()

test_function()


