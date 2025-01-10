import time
import pytest
import data
import locators
import methods
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from methods import FormPage


class TestFormPage:

    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1 - Configurar Patologia
    def test_set_patologia(self):
        self.driver.get(data.URL)
        FormPage(self.driver).set_patologia()

    # 2 - Configurar Prueba
    '''def test_set_prueba(self):
        FormPage(self.driver).set_prueba()'''

    # 3 - Configurar Consentimiento
    def test_set_consentimiento(self):
        FormPage(self.driver).set_consentimiento()

    # 4 - Configurar Pais
    def test_set_pais(self):
        FormPage(self.driver).set_pais()

    # 5 - Configurar Ciudad
    def test_set_ciudad(self):
        FormPage(self.driver).set_ciudad(data.ciudad)

    # 6 - Configurar Institucion
    def test_set_institucion(self):
        FormPage(self.driver).set_institucion()

    # 7 - Rellenar Nombres
    def test_nombres(self):
        FormPage(self.driver).set_nombres(data.nombres)

    # 8 - Rellenar Apellidos
    def test_apellidos(self):
        FormPage(self.driver).set_apellidos(data.apellidos)

    # 9 - Rellenar DNI
    def test_dni(self):
        FormPage(self.driver).set_dni(data.dni)

    # 10 - Rellenar Direccion
    def test_direccion(self):
        FormPage(self.driver).set_direccion(data.direccion)

    # 11 - Configurar Indicativo
    def test_indicativo(self):
        FormPage(self.driver).set_indicativo()

    # 12 - Rellenar Telefono
    def set_telefono_1(self):
        FormPage(self.driver).set_telefono_1(data.telefono_1)

    # 13 - Dar clic en Enviar
    def test_boton_enviar(self):
        FormPage(self.driver).click_boton_enviar()
        time.sleep(3)

    # 14 - Cerrar navegador
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()