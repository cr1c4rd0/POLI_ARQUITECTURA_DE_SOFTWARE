# POLI_ARQUITECTURA_DE_SOFTWARE

Resumen del curso de **Arquitectura de Software** del Politécnico Grancolombiano. El curso está organizado en 4 unidades y 8 escenarios de aprendizaje.

---

## Unidad 1 — Fundamentos de Arquitectura de Software

### Escenario 1: Conceptos Fundamentales

#### ¿Qué es la Arquitectura de Software?
La arquitectura de software es la estructura o estructuras de un sistema, que comprende los elementos de software, las propiedades visibles externamente de esos elementos y las relaciones entre ellos. Existen múltiples definiciones según diferentes autores:

- **Bass, Clements y Kazman**: Estructura(s) del sistema compuestas por elementos de software, sus propiedades visibles externamente y sus relaciones.
- **Garlan y Shaw**: Nivel de diseño que va más allá de los algoritmos y estructuras de datos, incluyendo la organización global del sistema y sus componentes.
- **IEEE 1471-2000**: Organización fundamental de un sistema, encarnada en sus componentes, las relaciones entre ellos y el ambiente, y los principios que guían su diseño y evolución.

#### Vistas y Puntos de Vista Arquitectónicos
- **Vista**: Representación de un sistema desde la perspectiva de un conjunto de preocupaciones relacionadas.
- **Punto de vista**: Conjunto de convenciones para construir, interpretar y usar una vista.
- **Modelo 4+1 (Kruchten)**: Cinco vistas complementarias:
  - Vista Lógica — funcionalidad del sistema
  - Vista de Procesos — aspectos de concurrencia y sincronización
  - Vista de Desarrollo — organización del software en el entorno de desarrollo
  - Vista Física — topología del sistema en hardware
  - Vista de Escenarios (+1) — casos de uso que integran las demás vistas

#### El Rol del Arquitecto de Software
El arquitecto de software es responsable de:
- Tomar decisiones de diseño de alto nivel
- Definir estándares técnicos, herramientas y plataformas
- Traducir los requisitos del negocio en requisitos técnicos
- Garantizar que el sistema cumpla con los atributos de calidad
- Comunicar la arquitectura a todos los interesados (stakeholders)

#### Estilos Arquitectónicos
Los estilos arquitectónicos son patrones de organización de sistemas software que definen tipos de componentes, conectores y restricciones de configuración:

| Estilo | Descripción |
|--------|-------------|
| **Cliente/Servidor** | División en clientes que solicitan servicios y servidores que los proveen |
| **Capas (Layers)** | Organización jerárquica donde cada capa provee servicios a la superior |
| **Tuberías y Filtros (Pipes & Filters)** | Procesamiento de datos a través de una cadena de transformaciones |
| **N-Tier** | Generalización multicapa con separación física de responsabilidades |
| **Peer-to-Peer (P2P)** | Nodos que actúan simultáneamente como clientes y servidores |
| **Publicador-Suscriptor (Pub/Sub)** | Desacoplamiento mediante canales de eventos o mensajes |

#### Drivers Arquitectónicos
Los drivers son los factores que determinan las decisiones de arquitectura:

- **Requisitos Funcionales**: Lo que el sistema debe hacer (casos de uso, funcionalidades)
- **Requisitos No Funcionales (Atributos de Calidad)**: Cómo debe comportarse el sistema — rendimiento, disponibilidad, seguridad, mantenibilidad, escalabilidad, portabilidad
- **Restricciones de Negocio**: Presupuesto, tiempo de entrega, estándares empresariales
- **Restricciones Técnicas**: Tecnologías predefinidas, plataformas existentes, interoperabilidad

#### Frameworks y Patrones de Diseño

**Patrones GOF (Gang of Four)** — 23 patrones en 3 categorías:
- *Creacionales*: Singleton, Factory Method, Abstract Factory, Builder, Prototype
- *Estructurales*: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
- *Comportamentales*: Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor, Interpreter

**Patrones GRASP** (General Responsibility Assignment Software Patterns):
- Experto en información, Creador, Controlador, Bajo Acoplamiento, Alta Cohesión
- Polimorfismo, Fabricación Pura, Indirección, Variaciones Protegidas

**Patrones de Concurrencia**:
- Monitor Object, Half-Sync/Half-Async, Leader/Followers, Active Object, Thread Pool

**Patrones de Fowler** (Enterprise Application Architecture):
- Domain Model, Table Module, Service Layer, Data Mapper, Active Record, Repository
- Unit of Work, Identity Map, Lazy Load, MVC, Page Controller, Front Controller

---

### Escenario 2: Arquitectura Orientada a Servicios (SOA)

#### Definición de SOA
La Arquitectura Orientada a Servicios (SOA) es un paradigma de diseño que organiza y utiliza capacidades distribuidas, bajo el control de diferentes dominios propietarios, donde la interacción se da a través de servicios débilmente acoplados e interoperables.

**Principios fundamentales de SOA:**
- Contrato de servicio estandarizado
- Bajo acoplamiento
- Abstracción del servicio
- Reusabilidad del servicio
- Autonomía del servicio
- Statelessness (sin estado)
- Descubrimiento del servicio
- Composición del servicio

#### Beneficios de SOA
- Reutilización de activos de TI
- Alineación entre negocio y TI
- Flexibilidad y agilidad empresarial
- Reducción de costos por integración
- Escalabilidad y mantenibilidad mejoradas

#### Evolución hacia SOA
1. Aplicaciones monolíticas
2. Arquitecturas cliente/servidor
3. Arquitecturas de componentes distribuidos (CORBA, COM/DCOM, EJB)
4. Servicios web (SOAP/WSDL/UDDI)
5. SOA
6. Microservicios (evolución moderna)

#### Los 83 Patrones SOA
Los patrones SOA se organizan en 4 categorías principales:

**1. Patrones de Diseño de Servicios** (Service Design Patterns):
- Service Façade, Decomposed Capability, Service Normalization
- Distributed Capability, Agnostic Sub-Controller

**2. Patrones de Inventario de Servicios** (Service Inventory Patterns):
- Logic Centralization, Canonical Resources, Service Layers
- Service Decomposition, Service Encapsulation

**3. Patrones de Composición de Servicios** (Service Composition Patterns):
- Orchestration, Choreography, Aggregator
- Scatter-Gather, Service Broker, Process Centralization

**4. Patrones de Seguridad y Gestión** (Service Security & Management Patterns):
- Service Perimeter Guard, Brokered Authentication, Data Confidentiality
- Exception Shielding, Service Monitoring, Service SLA

---

## Unidad 2 — Servicios Web: REST y SOAP

### Escenario 3: Transferencia de Estado Representacional (REST)

#### ¿Qué es REST?
REST (Representational State Transfer) es un estilo arquitectónico para sistemas hipermedia distribuidos, definido por Roy Fielding en su tesis doctoral (2000). No es un protocolo ni un estándar, sino un conjunto de restricciones arquitectónicas.

**Las 6 restricciones REST:**
1. **Cliente-Servidor**: Separación de responsabilidades entre interfaz de usuario y almacenamiento de datos
2. **Sin Estado (Stateless)**: Cada petición del cliente contiene toda la información necesaria
3. **Cacheable**: Las respuestas deben indicar si son cacheables
4. **Interfaz Uniforme**: Identificación de recursos, manipulación a través de representaciones, mensajes autodescriptivos, HATEOAS
5. **Sistema en Capas**: El cliente no puede saber si está conectado directamente al servidor final
6. **Código bajo Demanda** (opcional): Servidores pueden enviar código ejecutable al cliente

#### Recursos y Representaciones REST
- **Recurso**: Cualquier información que pueda ser nombrada (concepto, no dato)
- **Representación**: Estado actual o deseado de un recurso (JSON, XML, HTML, etc.)
- **URI**: Identificador uniforme de recurso — `/usuarios/123`, `/productos/abc`

#### Métodos HTTP en REST
| Método | Operación CRUD | Descripción |
|--------|---------------|-------------|
| GET | Read | Obtener representación de un recurso |
| POST | Create | Crear un nuevo recurso |
| PUT | Update | Actualizar un recurso completo |
| PATCH | Update | Actualizar parcialmente un recurso |
| DELETE | Delete | Eliminar un recurso |

#### SOAP (Simple Object Access Protocol)
SOAP es un protocolo de mensajería basado en XML para intercambio de información en entornos distribuidos:

**Estructura de un mensaje SOAP:**
```xml
<Envelope>
  <Header> <!-- Opcional: metadatos, autenticación --> </Header>
  <Body>   <!-- Obligatorio: contenido del mensaje --> </Body>
  <Fault>  <!-- Opcional: información de errores -->  </Fault>
</Envelope>
```

**Características de SOAP:**
- Protocolo formal con estándar W3C
- Independiente del transporte (HTTP, SMTP, FTP)
- Soporte nativo para WS-Security, WS-ReliableMessaging
- Verboso (XML) pero con tipado fuerte
- Contratos formales mediante WSDL

#### WSDL (Web Services Description Language)
WSDL es un lenguaje basado en XML para describir servicios web. Define:
- **Types**: Tipos de datos usados
- **Message**: Datos intercambiados
- **PortType/Interface**: Operaciones del servicio
- **Binding**: Protocolo y formato de datos
- **Service**: Endpoint del servicio

#### REST vs SOAP — Comparación

| Aspecto | REST | SOAP |
|---------|------|------|
| Protocolo | Estilo arquitectónico | Protocolo formal |
| Formato | JSON, XML, texto | Solo XML |
| Verbosidad | Liviano | Pesado |
| Estado | Stateless | Puede ser stateful |
| Seguridad | HTTPS, OAuth | WS-Security |
| Estándar | No formal | W3C |
| Uso típico | APIs web públicas | Servicios empresariales |

---

### Escenario 4: Aplicaciones Prácticas REST y SOAP

#### Diseño de APIs RESTful
Buenas prácticas para diseño de APIs REST:
- Usar sustantivos en plural para recursos: `/usuarios`, `/productos`
- Usar HTTP verbs correctamente para acciones
- Versionar la API: `/v1/usuarios`
- Usar códigos de estado HTTP apropiados (200, 201, 400, 401, 404, 500)
- Implementar HATEOAS para autodescubrimiento
- Documentar con OpenAPI/Swagger

#### Códigos de Estado HTTP
- **2xx**: Éxito (200 OK, 201 Created, 204 No Content)
- **3xx**: Redirección (301 Moved Permanently, 304 Not Modified)
- **4xx**: Error del cliente (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
- **5xx**: Error del servidor (500 Internal Server Error, 503 Service Unavailable)

---

## Unidad 3 — Integración de Sistemas y ESB

### Escenario 5: Arquitecturas de Integración de Sistemas

#### Estándares W3C y OASIS
- **W3C (World Wide Web Consortium)**: Organización que desarrolla estándares para la web — HTML, CSS, XML, SOAP, WSDL, OWL
- **OASIS (Organization for the Advancement of Structured Information Standards)**: Consorcio para estándares de e-business — SAML, WS-Security, ebXML, BPEL, AMQP

#### UDDI (Universal Description, Discovery and Integration)
UDDI es un directorio de servicios web que permite:
- **Páginas Blancas**: Información sobre la empresa proveedora del servicio
- **Páginas Amarillas**: Categorización del servicio por industria o tipo
- **Páginas Verdes**: Información técnica del servicio (WSDL, endpoints)

UDDI fue descontinuado como registro público (2006) pero su concepto persiste en registros privados empresariales.

#### Integración Empresarial
La integración de sistemas busca conectar aplicaciones heterogéneas para que compartan datos y procesos de negocio.

**Patrones de Integración Empresarial (EIP — Enterprise Integration Patterns):**
- **Message Channel**: Canal por el cual los mensajes son transportados
- **Message Router**: Enruta mensajes basándose en condiciones
- **Message Translator**: Convierte formatos de mensajes
- **Message Endpoint**: Conexión entre aplicación y sistema de mensajería
- **Aggregator**: Combina múltiples mensajes en uno
- **Splitter**: Divide un mensaje en múltiples partes
- **Scatter-Gather**: Envía a múltiples destinos y agrega respuestas

#### Tipos de Integración Empresarial

**Integración Vertical (Silo)**:
- Cada sistema de negocio es integrado de forma independiente
- Genera dependencias punto a punto (n×(n-1)/2 conexiones)
- Difícil de mantener y escalar

**Integración Horizontal (ESB)**:
- Bus centralizado que conecta todos los sistemas
- Reduce conexiones a n (uno por sistema al bus)
- Más fácil de gestionar, monitorear y escalar

---

### Escenario 6: Buses de Servicios e Integración (ESB)

#### Enterprise Service Bus (ESB)
El ESB es una infraestructura de software que proporciona servicios fundamentales para arquitecturas complejas mediante un bus basado en estándares.

**Componentes principales del ESB:**

1. **MOM (Message-Oriented Middleware)**:
   - Intermediario de mensajes asíncronos
   - Garantiza entrega confiable (at-least-once, exactly-once)
   - Patrones: Colas de mensajes (punto a punto) y Tópicos (publicar/suscribir)
   - Ejemplos: Apache ActiveMQ, IBM MQ, RabbitMQ, Apache Kafka

2. **Contenedor de Servicios**:
   - Ambiente de ejecución para servicios desplegados en el bus
   - Gestiona el ciclo de vida de los servicios
   - Provee interceptores para seguridad, logging, transformación

3. **Facilidad de Gestión**:
   - Monitoreo y administración del bus
   - Registro y repositorio de servicios
   - Políticas de SLA y QoS (Quality of Service)

**Capacidades del ESB:**
- Enrutamiento inteligente de mensajes
- Transformación y traducción de formatos
- Orquestación de procesos de negocio
- Gestión de seguridad centralizada
- Monitoreo y auditoría

#### Orquestación vs Coreografía

| Aspecto | Orquestación | Coreografía |
|---------|-------------|-------------|
| Control | Centralizado (orquestador) | Distribuido (cada servicio) |
| Visibilidad | Alta — proceso visible | Baja — distribuida |
| Acoplamiento | Mayor acoplamiento | Menor acoplamiento |
| Flexibilidad | Menos flexible | Más flexible |
| Herramienta | BPEL, BPMN | Eventos, mensajes |

#### BPEL (Business Process Execution Language)
BPEL es un lenguaje basado en XML para definir procesos de negocio ejecutables que orquestan servicios web:
- Define el flujo de trabajo entre servicios
- Maneja excepciones y compensaciones
- Soporta actividades paralelas y secuenciales
- Estándar OASIS WS-BPEL 2.0

#### BPMN (Business Process Model and Notation)
BPMN es una notación gráfica estándar para modelar procesos de negocio:
- Puente entre diseño de negocio y implementación técnica
- Elementos: Eventos, Actividades, Compuertas, Flujos, Pools, Lanes
- Versión actual: BPMN 2.0 (OMG)
- Puede ser ejecutable (mapeado a BPEL) o descriptivo

**Tipos de eventos BPMN:**
- *Inicio*: Start Event, Message Start, Timer Start
- *Intermedios*: Catching/Throwing events
- *Fin*: End Event, Error End, Terminate End

---

## Unidad 4 — Metodologías y Documentación

### Escenario 7: Metodologías y Procesos de Arquitectura

#### ACDM (Architecture Centric Design Method)
Metodología iterativa centrada en arquitectura para el desarrollo de sistemas:

**Fases del ACDM:**
1. **Descubrimiento y Experimentación**: Identificar requisitos y explorar soluciones
2. **Descripción de la Arquitectura**: Documentar la arquitectura candidata
3. **Revisión de la Arquitectura**: Evaluar la arquitectura con stakeholders
4. **Producción de la Arquitectura**: Refinar y finalizar la arquitectura
5. **Utilización de la Arquitectura**: Guiar el desarrollo basado en la arquitectura

**Principios del ACDM:**
- La arquitectura guía el proceso de desarrollo
- Las decisiones se toman con base en trade-offs explícitos
- La arquitectura evoluciona iterativamente
- Se centra en los drivers arquitectónicos de mayor riesgo

#### QAWM (Quality Attribute Workshop Method)
Método para identificar, priorizar y refinar los atributos de calidad de un sistema:

**Proceso QAWM:**
1. Presentación del sistema y su contexto
2. Identificación de stakeholders y sus preocupaciones
3. Elicitación de escenarios de atributos de calidad
4. Consolidación y priorización de escenarios
5. Refinamiento de escenarios en escenarios de utilidad

**Árbol de Utilidad (Utility Tree):**
Estructura jerárquica que organiza los atributos de calidad:
- Nivel 1: Utilidad del sistema
- Nivel 2: Atributos de calidad (rendimiento, disponibilidad, seguridad, etc.)
- Nivel 3: Escenarios de atributos de calidad refinados
- Prioridad: (H/M/L, H/M/L) — (importancia para negocio, dificultad técnica)

#### Modelo 4+1 de Kruchten
Modelo de vistas múltiples para describir la arquitectura de software:

```
         +------------------+
         |  Vista Lógica    |  (Diseñadores, Usuarios finales)
         +------------------+
                 |
    +------------+------------+
    |                         |
+----------+          +------------------+
|  Vista   |          |  Vista de        |
| Procesos |          |  Desarrollo      |
+----------+          +------------------+
    |                         |
    +------------+------------+
                 |
         +------------------+
         |  Vista Física    |  (Ingenieros de sistemas)
         +------------------+
                 |
         +------------------+
         |  Escenarios (+1) |  (Todos los stakeholders)
         +------------------+
```

#### FURPS+
Modelo de clasificación de requisitos de calidad:
- **F**unctionality: Capacidad, seguridad, reusabilidad
- **U**sability: Factores humanos, estética, consistencia, documentación
- **R**eliability: Frecuencia de fallas, capacidad de recuperación, predictibilidad
- **P**erformance: Velocidad, eficiencia, disponibilidad, rendimiento, escalabilidad
- **S**upportability: Mantenibilidad, adaptabilidad, internacionalización, configurabilidad
- **+**: Restricciones de diseño, requisitos de implementación, requisitos de interfaz, requisitos físicos

---

### Escenario 8: Documentación de la Arquitectura

#### Catálogo de Diagramas UML
UML (Unified Modeling Language) define 14 tipos de diagramas organizados en dos grupos:

**Diagramas Estructurales (7):**
| Diagrama | Propósito |
|----------|-----------|
| Clases | Estructura estática del sistema y relaciones entre clases |
| Objetos | Instancias de clases en un momento específico |
| Componentes | Organización y dependencias de componentes |
| Despliegue | Distribución física en nodos de hardware |
| Paquetes | Agrupación y dependencias de paquetes |
| Estructura Compuesta | Estructura interna de un clasificador |
| Perfiles | Extensiones del metamodelo UML |

**Diagramas de Comportamiento (7):**
| Diagrama | Propósito |
|----------|-----------|
| Casos de Uso | Funcionalidades del sistema y actores |
| Actividad | Flujo de trabajo o proceso de negocio |
| Máquina de Estados | Comportamiento de objetos con estados |
| Secuencia | Interacción entre objetos en el tiempo |
| Comunicación | Interacción enfocada en enlaces entre objetos |
| Temporización | Comportamiento en función del tiempo |
| Visión General de Interacción | Combinación de diagramas de interacción |

#### Marco TRIVADIS para Documentación
Marco de referencia para documentar arquitecturas de software empresariales:

**Niveles de Arquitectura:**

1. **Arquitectura de Referencia**:
   - Define estándares, principios y directrices corporativas
   - Marco tecnológico y de proceso de la organización
   - Vocabulario y conceptos comunes
   - Independiente de proyectos específicos

2. **Arquitectura de Solución**:
   - Diseño arquitectónico de un sistema o proyecto específico
   - Basada en la arquitectura de referencia
   - Define componentes, interfaces y tecnologías concretas
   - Orientada a satisfacer los drivers del proyecto

3. **Arquitectura de Implementación**:
   - Detalle técnico de cómo se construye la solución
   - Especificaciones de despliegue e infraestructura
   - Guías de implementación para el equipo de desarrollo
   - Decisiones de tecnología específicas

#### Atributos de Calidad de la Documentación
La documentación de arquitectura debe ser:
- **Completa**: Cubrir todas las vistas relevantes
- **Consistente**: Sin contradicciones entre vistas
- **Comprensible**: Clara para todos los stakeholders
- **Actualizada**: Refleja el estado actual del sistema
- **Accesible**: Fácil de encontrar y navegar
- **Trazable**: Vinculada a requisitos y decisiones

---

## Resumen por Unidades

| Unidad | Escenarios | Temas Principales |
|--------|-----------|-------------------|
| **1** | 1-2 | Fundamentos, estilos, patrones GOF/GRASP/Fowler, drivers arquitectónicos, SOA básico |
| **2** | 3-4 | REST, SOAP, WSDL, APIs RESTful, comparación REST vs SOAP |
| **3** | 5-6 | Integración empresarial, ESB, MOM, BPEL, BPMN, orquestación |
| **4** | 7-8 | ACDM, QAWM, 4+1, FURPS+, UML 14 diagramas, TRIVADIS |

---

## Recursos del Curso

Los materiales de lectura se encuentran en la carpeta `DOCUMENTACIÓN/`:

- `ESCENARIO_1/` — Fundamentos de arquitectura de software
- `ESCENARIO_2/` — Arquitectura orientada a servicios (SOA)
- `ESCENARIO_3/` — REST y servicios web
- `ESCENARIO_4/` — Aplicaciones prácticas REST/SOAP
- `ESCENARIO_5/` — Integración de sistemas empresariales
- `ESCENARIO_6/` — ESB, BPEL y BPMN
- `ESCENARIO_7/` — Metodologías de arquitectura
- `ESCENARIO_8/` — Documentación de arquitectura
- `TRABAJO_GRUPAL/` — Materiales para el trabajo colaborativo

---

## CiberEscudo — Guía de instalación y ejecución local

CiberEscudo es el proyecto práctico del curso. Es una aplicación web desarrollada en **Flask (Python)** que permite verificar si un correo electrónico ha sido filtrado en brechas de datos conocidas, comprobar contraseñas comprometidas con k-Anonymity y consultar guías de acción en español.

### Requisitos previos

- **Python 3.10 o superior** — [python.org/downloads](https://www.python.org/downloads/)
- **Git** — [git-scm.com](https://git-scm.com/)
- Terminal (PowerShell, CMD o bash)

---

### 1. Clonar el repositorio

```bash
git clone https://github.com/cr1c4rd0/POLI_ARQUITECTURA_DE_SOFTWARE.git
cd POLI_ARQUITECTURA_DE_SOFTWARE
```

---

### 2. Crear el entorno virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

> Sabrás que el entorno está activo cuando el prompt muestre `(.venv)` al inicio.

---

### 3. Instalar Flask y dependencias

```bash
pip install -r requirements.txt
```

Esto instala:

| Paquete | Versión | Uso |
|---|---|---|
| `flask` | 3.1.3 | Framework web |
| `requests` | 2.32.3 | Consultas HTTP a HIBP |
| `python-dotenv` | 1.0.1 | Variables de entorno |

---

### 4. Ejecutar el proyecto

```bash
python app.py
```

Deberías ver en consola:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

Abre tu navegador y ve a: **http://127.0.0.1:5000**

---

### 5. Iniciar sesión

La aplicación usa un usuario fijo para el entorno de desarrollo:

| Campo | Valor |
|---|---|
| **Usuario** | `admin` |
| **Contraseña** | `ciberescudo123` |

Ingresa las credenciales en la pantalla de login y haz clic en **Iniciar Sesión**. Serás redirigido automáticamente al panel principal.

---

### Estructura del proyecto

```
POLI_ARQUITECTURA_DE_SOFTWARE/
├── app.py                  # Punto de entrada principal
├── config.py               # Configuración y registro de servicios
├── requirements.txt        # Dependencias
├── routes/                 # Blueprints (servicios SOA)
│   ├── auth.py             # Autenticación
│   ├── monitoring.py       # Consulta de brechas por correo
│   ├── passwords.py        # Verificación de contraseñas (k-Anonymity)
│   ├── guides.py           # Guías de acción
│   └── history.py          # Historial de alertas
├── services/               # Lógica de negocio
│   ├── hibp_service.py     # Servicio HIBP (brechas de correo)
│   ├── password_checker.py # Verificación con k-Anonymity
│   ├── action_guides.py    # Guías en español
│   └── history_service.py  # Persistencia SQLite
├── templates/              # Vistas HTML (Jinja2 + Bootstrap 5)
└── static/css/             # Estilos personalizados
```

---

### Endpoints disponibles

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET | Panel principal |
| `/auth/login` | GET / POST | Iniciar sesión |
| `/auth/logout` | GET | Cerrar sesión |
| `/monitoring/check` | POST | Verificar correo |
| `/passwords/check` | GET / POST | Verificar contraseña |
| `/history/` | GET | Historial de alertas |
| `/guides/<tipo>` | GET | Guía de acción |
| `/api/v1/health` | GET | Estado global del sistema |
