from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"

#Функция для проверки наличия кнопки "Добавить в корзину"     
def check_basket_by_xpath(browser, xpath):

    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def test_basket(browser):

    #Открываем ссылку и нажимаем на "Все товары"
    browser.get(link)
    browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()

    #Открываем ссылку на страницу книги "Coders at work"
    browser.find_element(By.LINK_TEXT, 'Coders at Work').click()
    
    #Проверка наличия кнопки "Добавить в корзину"
    basket = check_basket_by_xpath(browser, '//*[@id="add_to_basket_form"]/button')

    assert basket == True, "Кнопка 'Добавить в корзину' отсутствует"

