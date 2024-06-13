Brawl Stars Brawler Search
Índice

    Descripción de la API
    Estructura
    Funcionamiento
    Modo de trabajo
    Bibliografía

Descripción de la API

API: Brawl Stars

La API de Brawl Stars ofrece acceso a una gran variedad de datos del juego Brawl Stars, incluyendo información detallada sobre los brawlers, sus gadgets y star powers. Esto permite a los desarrolladores crear aplicaciones y servicios que integren y utilicen datos actualizados directamente desde el juego.

Algunos de los servicios más relevantes que proporciona la API incluyen la obtención de listas completas de brawlers, así como detalles específicos de cada uno, lo que incluye estadísticas y habilidades especiales.

Endpoints Relevantes:

    Lista de Brawlers: https://api.brawlstars.com/v1/brawlers
    Detalles de un Brawler: https://api.brawlstars.com/v1/brawlers/{brawlerId}

Para utilizar la API, es necesario registrarse en el sitio web de desarrolladores de Brawl Stars y obtener una clave de API, la cual se utiliza para autenticar las solicitudes.
Estructura
Archivos y Carpetas Principales

    forms.py: Contiene funciones y clases para gestionar la lógica de las solicitudes a la API de Brawl Stars. Este archivo incluye métodos que construyen las URLs de las solicitudes basadas en los parámetros de entrada y la clave de API.

    templates/: Esta carpeta contiene las plantillas HTML utilizadas en la aplicación:
        base.html: Es la plantilla base que contiene la estructura común para todas las páginas.
        brawlers_list.html: Extiende base.html y muestra la lista de brawlers con sus gadgets y star powers.
        brawler_detail.html: Extiende base.html y muestra detalles específicos de un brawler seleccionado.

Template

El archivo base.html es la plantilla principal que define la estructura común de la página, como el encabezado, el pie de página y el diseño general. Las otras plantillas heredan de esta y solo modifican la sección de contenido, proporcionando una forma eficiente de manejar diferentes vistas con un diseño coherente.
Funcionamiento

La aplicación comienza en la página de inicio, donde se presenta un menú desplegable para seleccionar un brawler específico de la lista. Al seleccionar un brawler, se muestran detalles como sus gadgets y star powers.
Pasos:

    Inicio: La página principal (index) tiene un menú desplegable que permite al usuario seleccionar un brawler de la lista.

    Visualización de Detalles: Después de seleccionar un brawler y hacer clic en "Ver Detalles", se redirige a la página de resultados donde se muestran las estadísticas y habilidades específicas del brawler.

    Navegación: Se puede volver a la página de inicio en cualquier momento utilizando el navbar, que facilita la navegación y permite realizar nuevas búsquedas de brawlers.

El flujo de la aplicación permite a los usuarios interactuar con los datos de forma sencilla y obtener información detallada de los brawlers de interés.
Modo de Trabajo

Para cumplir con la consigna y la necesidad de utilizar un framework CSS, se ha utilizado Bootstrap para mejorar la interfaz de usuario. Esto incluye la creación de un navbar que facilita la navegación entre las páginas y la visualización de datos en una tabla estilizada.
Diseño con Bootstrap

    Navbar: Se ha creado un navbar utilizando Bootstrap para permitir la fácil navegación entre la página de inicio y la página de resultados.
    Tablas: Los datos de los brawlers se muestran en tablas con las columnas Nombre, Gadget y Star Power, proporcionando una presentación clara y ordenada de la información obtenida de la API.

Solicitudes a la API

Para obtener la información de los brawlers, se realizan solicitudes GET a la API de Brawl Stars utilizando la biblioteca requests en Python. La respuesta se procesa y se muestra en la interfaz de usuario de la aplicación.
Bibliografía

    Documentación oficial de Bootstrap: Bootstrap 5 Documentation
    Documentación oficial de Brawl Stars API: Brawl Stars API Documentation
    Documentación oficial de Django: Django Documentation