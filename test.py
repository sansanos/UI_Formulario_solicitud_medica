import data
from selenium import webdriver

import locators
from methods import FormPage


class TestFormPage:

    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1 - Configurar Patologia
    def test_set_patologia(self):
        self.driver.get(data.URL)
        FormPage(self.driver).set_patologia()
        assert self.driver.find_element(*locators.LocatorsFormPage.patologia_linfoma).is_displayed() == True

    '''# 2 - Configurar Prueba
    def test_set_prueba(self):
        FormPage(self.driver).set_prueba()'''

    # 3 - Configurar Consentimiento
    def test_set_consentimiento(self):
        FormPage(self.driver).set_consentimiento()
        assert self.driver.find_element(*locators.LocatorsFormPage.consentimiento_si).is_selected() == True

    # 4 - Configurar Pais
    def test_set_pais(self):
        FormPage(self.driver).set_pais()
        assert self.driver.find_element(*locators.LocatorsFormPage.pais_colombia).is_selected() == True

    # 5 - Configurar Ciudad
    def test_set_ciudad(self):
        FormPage(self.driver).set_ciudad(data.ciudad)
        assert self.driver.find_element(*locators.LocatorsFormPage.ciudad_placeholder).get_property('value') == data.ciudad

    # 6 - Configurar Institucion
    def test_set_institucion(self):
        FormPage(self.driver).set_institucion()
        assert self.driver.find_element(*locators.LocatorsFormPage.institucion_2).is_selected() == True

    # 7 - Rellenar Nombres
    def test_nombres(self):
        FormPage(self.driver).set_nombres(data.nombres)
        assert self.driver.find_element(*locators.LocatorsFormPage.nombres_placeholder).get_property('value') == data.nombres

    # 8 - Rellenar Apellidos
    def test_apellidos(self):
        FormPage(self.driver).set_apellidos(data.apellidos)
        assert (self.driver.find_element(*locators.LocatorsFormPage.apellidos_placeholder).
                get_property('value') == data.apellidos)

    # 9 - Rellenar DNI
    def test_dni(self):
        FormPage(self.driver).set_dni(data.dni)
        assert (self.driver.find_element(*locators.LocatorsFormPage.dni_placeholder).
                get_property('value') == data.dni)

    # 10 - Rellenar Direccion
    def test_direccion(self):
        FormPage(self.driver).set_direccion(data.direccion)
        assert self.driver.find_element(*locators.LocatorsFormPage.direccion_placeholder).get_property(
            'value') == data.direccion

    # 11 - Configurar Indicativo
    def test_indicativo(self):
        FormPage(self.driver).set_indicativo()
        assert self.driver.find_element(*locators.LocatorsFormPage.indicativo_col).is_selected() == True

    # 12 - Rellenar Telefono
    def test_telefono_1(self):
        FormPage(self.driver).set_telefono_1(data.telefono_1)
        assert self.driver.find_element(*locators.LocatorsFormPage.telefono_1_placeholder).get_property(
            'value') == data.telefono_1

    # 13 - Dar clic en Enviar
    def test_boton_enviar(self):
        FormPage(self.driver).click_boton_enviar()
        assert self.driver.find_element(*locators.LocatorsFormPage.boton_enviar).is_enabled() == True

    # 14 - Cerrar navegador
    def test_cerrar_navegador(self):
        self.driver.quit()