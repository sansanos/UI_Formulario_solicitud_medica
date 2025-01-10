from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from data import apellidos

class FormPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # acciones
    def set_patologia(self):
        self.driver.find_element(*locators.LocatorsFormPage.patologia_dropdown).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsFormPage.patologia_linfoma))
        self.driver.find_element(*locators.LocatorsFormPage.patologia_linfoma).click()

    def set_prueba(self):
        self.driver.find_element(*locators.LocatorsFormPage.prueba_dropdown).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsFormPage.prueba_1))
        self.driver.find_element(*locators.LocatorsFormPage.prueba_1).click()

    def set_consentimiento(self):
        self.driver.find_element(*locators.LocatorsFormPage.consentimiento_dropdown).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsFormPage.consentimiento_si))
        self.driver.find_element(*locators.LocatorsFormPage.consentimiento_si).click()

    def set_pais(self):
        self.driver.find_element(*locators.LocatorsFormPage.pais_dropdown).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsFormPage.pais_colombia))
        self.driver.find_element(*locators.LocatorsFormPage.pais_colombia).click()

    def set_ciudad(self, ciudad):
        return self.driver.find_element(*locators.LocatorsFormPage.ciudad_placeholder).send_keys(ciudad)

    def set_institucion(self):
        self.driver.find_element(*locators.LocatorsFormPage.institucion_dropdown).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsFormPage.institucion_2))
        self.driver.find_element(*locators.LocatorsFormPage.institucion_2).click()

    def scroll_boton_enviar(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();", locators.LocatorsFormPage.boton_enviar)

    def set_nombres(self, nombres):
        self.driver.find_element(*locators.LocatorsFormPage.nombres_placeholder).send_keys(nombres)

    def set_apellidos(self, nombres):
        self.driver.find_element(*locators.LocatorsFormPage.apellidos_placeholder).send_keys(apellidos)

    def set_dni(self, dni):
        self.driver.find_element(*locators.LocatorsFormPage.dni_placeholder).send_keys(dni)

    def set_direccion(self, direccion):
        self.driver.find_element(*locators.LocatorsFormPage.direccion_placeholder).send_keys(direccion)

    def set_indicativo(self):
        self.driver.find_element(*locators.LocatorsFormPage.indicativo_dropdown).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsFormPage.institucion_2))
        self.driver.find_element(*locators.LocatorsFormPage.indicativo_col).click()

    def set_telefono_1(self, telefono_1):
        self.driver.find_element(*locators.LocatorsFormPage.telefono_1_placeholder).send_keys(telefono_1)

    def click_boton_enviar(self):
        self.driver.find_element(*locators.LocatorsFormPage.boton_enviar).click()