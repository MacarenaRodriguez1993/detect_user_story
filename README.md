# Bugster API

Bugster es una API diseñada para manejar eventos de interacción de los usuarios en diversas plataformas. Este proyecto implementa FastAPI junto con SQLAlchemy para el manejo de bases de datos.

## Instrucciones de instalación y ejecución

### Requisitos

- Python 3.12.0
- PostgreSQL
- Virtualenv (opcional, pero recomendado)

## Implementacion para correr el proyecto en un computador personal

    # Iniciamos clonando el repositorio 
    git clone <URL_del_repositorio>
    cd nombre_del_repositorio

    # Configuración del Entorno Virtual
    python -m venv nombre_del_entorno
    En Windows: nombre_del_entorno\Scripts\activate
    En Unix o MacOS: source nombre_del_entorno/bin/activate

    # Instalación de Dependencias:
    pip install -r requirements.txt

    # Ejecución del Servidor por default sera el puerto 8000
    uvicorn main:app --reload


## Crear archivo .env agregando la configuracion
    DB_NAME=tu_nombre_de_base_de_datos
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_HOST=localhost
    DB_PORT=5432


## Endpoints
    Gracias a la versatilidad de fastapi , creamos una documentacion automatica para poder visualizar los endopoint.
    Para poder acceder a la documentacion de api debo ingresar a la siguiente URL:

    * https//localhost:8000/docs

## Explicación de decisiones de diseño
    Arquitectura Hexagonal
    La arquitectura del proyecto sigue el principio de la arquitectura hexagonal o "Ports and Adapters". Este diseño facilita la separación de las capas de la aplicación, lo que permite que los casos de uso no dependan directamente de los detalles de implementación, como la base de datos.

    Capas:
    Application Layer: Contiene los casos de uso de la aplicación (use_cases), los cuales definen las acciones principales de la API.

    Domain Layer: Define los modelos de datos y la lógica del dominio (incluyendo el manejo de eventos y atributos).

    Infrastructure Layer: Implementa la persistencia de datos (repositorios) y expone las rutas de la API.

## Áreas de mejora identificadas
    Manejo de errores: Se podrían implementar estrategias de manejo de errores más específicas, como una mejor gestión de excepciones y mensajes de error más detallados.

    Optimización de consultas: A medida que el número de eventos crezca, sería útil implementar estrategias de paginación y consultas más eficientes en la capa de repositorio.

    Escalabilidad: Aunque la API es capaz de manejar una cantidad razonable de tráfico, sería necesario considerar una arquitectura más distribuida si el volumen de datos aumenta significativamente, como la introducción de microservicios o el uso de colas para el procesamiento de eventos.

## Implementacion de algoritmo deteccion de historias de usuarios
    Secuencias de eventos: Cada historia de usuario generalmente está compuesta por una secuencia lógica de eventos, como la entrada de datos, clics en botones, navegación entre páginas, etc.

    Identificación de inicio y fin: No necesariamente sabrás de antemano cuáles eventos inician o finalizan una historia, por lo que el algoritmo debe poder identificar dinámicamente esos puntos basándose en patrones generales.

    Detección de "contextos": Los eventos dentro de una historia tienden a estar relacionados dentro de un contexto común (como un flujo de interacción o una página). Identificar esos contextos es clave.

    Agrupación flexible: Debes agrupar eventos de manera flexible sin depender de un conjunto fijo de reglas predefinidas. En cambio, debes identificar "agrupaciones naturales" de eventos.

### ¿Cómo funciona este algoritmo?
    Inactividad o cambio de contexto:

    El algoritmo detecta una nueva historia de usuario cuando no ha habido actividad por un tiempo determinado (TIEMPO_MAX_INACTIVIDAD), o cuando el usuario cambia de contexto (por ejemplo, una nueva URL, o un cambio significativo en el flujo de eventos).
    Inicio de una historia:

    Se inicia una nueva historia cuando no hay una historia activa, y cada nuevo evento se asocia con un "contexto" (como una URL o una sección de la aplicación).
    Agrupación de eventos:

    Todos los eventos que ocurren dentro de un período corto de tiempo y en el mismo contexto se agrupan en la misma historia.
    Finalización de una historia:

    Si el tiempo entre eventos excede el valor de inactividad permitido o si cambia el contexto (por ejemplo, la URL), la historia actual se cierra y se inicia una nueva.
    Generalización del contexto:

### Contexto basado en URL:
    En este ejemplo, se asume que la URL es un buen indicador del contexto, pero puedes utilizar otros elementos para definir el contexto, como:
    Tipo de evento: Podrías detectar si el evento es de "input", "click", "submit", etc.
    Comportamiento del usuario: Los eventos que involucran la misma interacción del usuario, como el envío de un formulario, pueden agruparse juntos.
    Tiempo de inactividad:

    Si el usuario deja de interactuar durante más de un cierto tiempo (TIEMPO_MAX_INACTIVIDAD), puedes suponer que la historia terminó.+