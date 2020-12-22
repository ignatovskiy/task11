from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class OrderPageObject(PageObject):
    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get(f"{self.config.get('Test', 'url')}")
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.vehicle_table.wait_until_visible()
        return self

    def choose_last_vehicle(self):
        Button(By.CSS_SELECTOR, "table tr:last-child td").click()
        return OrderPageObject(self.driver_wrapper)

    def purchase_order(self):
        Button(By.ID, 'mOrder_menu').click()
        return OrderPageObject(self.driver_wrapper)

    def send_order(self):
        send_order = Button(By.ID, 'miSendOrder_menu')
        send_order.click()
        return OrderPageObject(self.driver_wrapper)

    def open_contact_details(self):
        Button(By.ID, 'SendPurchaseOrderDialogAccordionContactInDesc').click()
        return OrderPageObject(self.driver_wrapper)

    def enter_surname(self, surname):
        surname_input = InputText(By.NAME, 'mySurname')
        surname_input.click()
        surname_input.text = surname
        return OrderPageObject(self.driver_wrapper)

    def enter_name(self, name):
        name_input = InputText(By.NAME, 'myFirstname')
        name_input.click()
        name_input.text = name
        return OrderPageObject(self.driver_wrapper)

    def enter_street_address(self, street_address):
        address_input = InputText(By.NAME, 'myStreet')
        address_input.click()
        address_input.text = street_address
        return OrderPageObject(self.driver_wrapper)

    def enter_zip_code(self, zip_code):
        zip_code_input = InputText(By.NAME, 'myZip')
        zip_code_input.click()
        zip_code_input.text = zip_code
        return OrderPageObject(self.driver_wrapper)

    def enter_city(self, city):
        city_input = InputText(By.NAME, 'myCity')
        city_input.click()
        city_input.text = city
        return OrderPageObject(self.driver_wrapper)

    def enter_country(self, country):
        country_input = InputText(By.NAME, 'myCountry')
        country_input.click()
        country_input.text = country
        return OrderPageObject(self.driver_wrapper)

    def enter_phone_number(self, phone_number):
        phone_number_input = InputText(By.NAME, 'myNumber')
        phone_number_input.click()
        phone_number_input.text = phone_number
        return OrderPageObject(self.driver_wrapper)

    def enter_e_mail(self, e_mail):
        e_mail_input = InputText(By.NAME, 'myMail')
        e_mail_input.click()
        e_mail_input.text = e_mail
        return OrderPageObject(self.driver_wrapper)

    def send_purchase_order(self):
        Button(By.ID, 'SendOrderButton').click()
        return OrderPageObject(self.driver_wrapper)

    def select_options(self):
        Button(By.ID, 'mOptions_menu').click()
        return OrderPageObject(self.driver_wrapper)

    def select_vehicles(self):
        Button(By.ID, 'miVehicles_menu').click()
        return OrderPageObject(self.driver_wrapper)

    def enter_car_info(self, name, price):
        name_input = InputText(By.ID, 'VehicleName_input')
        name_input.click()
        name_input.text = name
        price_input = InputText(By.ID, 'VehiclePrice')
        price_input.click()
        price_input.text = price
        return OrderPageObject(self.driver_wrapper)

    def click_create(self):
        Button(By.ID, 'NewButton1').click()
        Button(By.ID, 'OkButton1').click()
        return OrderPageObject(self.driver_wrapper)

    def check_added_car(self):
        added_car = Text(By.XPATH, '//*[@id="VehiclesTable"]/tbody/tr[7]/td[1]')
        assert (added_car, 'Lada Vesta')
        return OrderPageObject(self.driver_wrapper)

    def select_and_edit_car(self):
        edited_car = Button(By.XPATH, '//*[@id="VehiclesTable"]/tbody/tr[6]/td[3]/a[2]')
        edited_car.click()
        return OrderPageObject(self.driver_wrapper)

    def enter_new_info(self, name, price):
        name_input = InputText(By.ID, 'VehicleDialogEditPanelVehicleName_input')
        name_input.click()
        name_input.text = name
        price_input = InputText(By.ID, 'VehicleDialogEditPanelVehiclePrice_input')
        price_input.click()
        price_input.text = price
        return OrderPageObject(self.driver_wrapper)

    def click_ok(self):
        Button(By.ID, 'OkButton3').click()
        return OrderPageObject(self.driver_wrapper)

    def check_edited_car(self, name, price):
        edited_car_name = Text(By.XPATH, '//*[@id="VehiclesTable"]/tbody/tr[6]/td[1]')
        edited_car_price = Text(By.XPATH, '//*[@id="VehiclesTable"]/tbody/tr[6]/td[2]')
        assert (edited_car_name, name)
        assert (edited_car_price, price)

    def click_delete(self):
        Button(By.XPATH, '//*[@id="VehiclesTable"]/tbody/tr[6]/td[3]/a[1]').click()
        return OrderPageObject(self.driver_wrapper)

    def check_deleted_car(self):
        try:
            deleted = Button(By.XPATH, '//*[@id="VehiclesTable"]/tbody/tr[6]/td[3]/a[1]')
        except:
            return True
        else:
            return False

    def is_confirmed(self):
        assert ('https://ignatovskiy.github.io/testing_course/confirmEN.pdf' == self.driver.current_url)
