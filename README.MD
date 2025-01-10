# Proyecto Formulario de Solicitud Médica

***Elaborado por Santiago Sánchez Ospina***

Este proyecto tiene como propósito desarrollar una solución de automatización empleando Selenium y Pytest, herramientas clave para la verificación funcional de aplicaciones web. El objetivo principal es automatizar las pruebas de validación y envío de un formulario médico en la plataforma, asegurando su correcta funcionalidad y cumplimiento de los criterios de aceptación establecidos.
Sobre la aplicación

El formulario de solicitud médica permite a los usuarios (pacientes) ingresar información personal, datos del médico remitente y detalles de la prueba médica que desean realizar. Este flujo garantiza que los datos enviados al laboratorio sean validados y procesados adecuadamente.
Proceso

Este proyecto utiliza el patrón de diseño POM (Page Object Model) para estructurar y organizar el código de prueba. Este enfoque divide las responsabilidades en diferentes componentes:

- Datos: Organización de datos a usar en las pruebas.
- Localizadores: Identificación de elementos web necesarios para la interacción.
- Métodos: Definición de las funciones para realizar las acciones de prueba.
- Pruebas: Ejecución de casos de prueba diseñados para validar el flujo de envío del formulario.

Pasos para ejecutar las pruebas

- Instalar las dependencias necesarias:
        Usando la terminal:

    pip install pytest
    pip install selenium

    Desde PyCharm: Busca e instala pytest y selenium en la pestaña Python Packages.

Clonar el repositorio:

git clone <URL del repositorio>
cd <nombre del repositorio>

Ejecutar las pruebas:

- pytest test_cases.py

Campos obligatorios en el formulario

- Pruebas a solicitar (mínimo una selección).
- Patología (una selección).
- Consentimiento informado (checkbox obligatorio).
- País, ciudad e institución médica.
- Información del paciente: nombre, apellidos, dirección, DNI.
- Teléfono principal con prefijo.

Solicitudes requeridas

- Seleccionar las pruebas a realizar.
- Configurar la patología.
- Confirmar el consentimiento informado.
- Seleccionar país, ciudad e institución médica.
- Ingresar datos del paciente (nombre, apellidos, dirección, DNI, teléfono).
- Validar mensajes de error o éxito según el flujo.

Tecnologías

El proyecto fue desarrollado utilizando:

- Lenguaje: Python.
- Herramientas: Selenium WebDriver, Pytest.
- Entorno de desarrollo: PyCharm.
- Navegador: Google Chrome (configurado con Selenium).

El patrón POM permitió organizar y mantener el código de forma eficiente, simulando el flujo completo de un usuario al interactuar con el formulario. Cada paso del flujo fue verificado mediante asserts, garantizando el cumplimiento de las expectativas funcionales y detectando posibles áreas de mejora.