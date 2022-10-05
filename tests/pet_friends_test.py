from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestPetFriends:

    def setup(self):
        self.url = 'https://petfriends.skillfactory.ru/'
        self.name = 'Уникальное имя'
        self.login = 'Электронная почта'
        self.password = 'Пароль'

    def test_(self, browser):
        browser.maximize_window()
        browser.get(self.url + 'login')
        assert WebDriverWait(browser, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'form-control')))
        browser.find_element(By.XPATH, '//input[@id="email"]').send_keys(self.login)
        browser.find_element(By.XPATH, '//input[@id="pass"]').send_keys(self.password)
        browser.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
        assert WebDriverWait(browser, 6).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))
        assert WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//h1'))).text == 'PetFriends'
        browser.find_element(By.XPATH, '//a[@class="nav-link"  and contains(text(), "Мои питомцы")]').click()
        assert WebDriverWait(browser, 6).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))
        assert WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//h2'))).text == self.name
        browser.implicitly_wait(10)
        pets_numbers = browser.find_element(By.XPATH, '//body/div[1]/div[1]/div[1]').text.split()[2]
        pets = browser.find_elements(By.XPATH, '//div[@id="all_my_pets"]')
        images = browser.find_elements(By.CSS_SELECTOR, 'img')
        counter = 0
        pet_names = []
        pet_uniq = []
        for i in range(len(pets)):                        # берем все текстовые значения в таблице
            pets_list = pets[i].text.upper().split('\n')  # переводим все в верхний регистр для удобства поиска
        pets_list = pets_list[1::2]  # срезаем нужные, оставляя только имя, породу, возраст питомцев
        for i in range(len(images)):  # цикл считает количество питомцев без фото
            if images[i].get_attribute('src') == '':
                counter += 1
        for pet in pets_list:
            assert len(pet.split(' ')) == 3  # в цикле проверяем что у каждого питомца заполнены все три поля
            pet_names.append(pet.split(' ')[0])
            if pet in pet_uniq:  # цикл формирует список уникальных питомцев
                continue
            else:
                pet_uniq.append(pet)
        assert int(pets_numbers) == int(len(pets_list))  # проверяем что присутствуют все питомцы
        assert (round(((counter * 100) / int(pets_numbers)))) <= 50  # проверяем количество фото у питомцев в процентах
        assert len(pet_names) == len(set(pet_names))  # проверяем одинаковые имена
        assert pets_list == pet_uniq  # проверяем что нет повторяющихся питомцев













































