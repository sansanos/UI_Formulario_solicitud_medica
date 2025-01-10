from selenium.webdriver.common.by import By

class LocatorsFormPage:

    patologia_dropdown = (By.ID, 'pathology') # click()
    patologia_linfoma = (By.CSS_SELECTOR, '#pathology > option:nth-child(6)') # click
    prueba_dropdown = (By.XPATH, '//*[@id="root"]/div/form/section[1]/div[2]/div[2]/div/div[1]') # click ()
    prueba_1 = (By.ID, 'id=":r4:') # click
    consentimiento_dropdown = (By.ID, 'consent') # clcik
    consentimiento_si = (By.XPATH, '//*[@id="consent"]/option[2]') # clcik
    pais_dropdown = (By.ID, 'country') # clcik
    pais_colombia = (By.CSS_SELECTOR, '#country > option:nth-child(2)') # click
    ciudad_placeholder = (By.CSS_SELECTOR, '#\:r7\:-form-item') # send_keys()
    institucion_dropdown = (By.ID, 'institution') # click
    institucion_2 = (By.XPATH, '//*[@id="institution"]/option[3]') # click
    nombres_placeholder = (By.ID, ':r9:-form-item') # send_keys
    apellidos_placeholder = (By.ID, ':ra:-form-item') # send_keys
    dni_placeholder = (By.ID, ':rb:-form-item') # send_keys
    direccion_placeholder = (By.ID, ':rc:-form-item') # send_keys
    indicativo_dropdown = (By.ID, 'prefix1') # click
    indicativo_col = (By.CSS_SELECTOR, '#prefix1 > option:nth-child(2)') # click()
    telefono_1_placeholder = (By.CLASS_NAME, 'text-[0.8rem] font-medium text-destructive') # send_keys
    boton_enviar = (By.XPATH, '//*[@id="root"]/div/form/button') # click
