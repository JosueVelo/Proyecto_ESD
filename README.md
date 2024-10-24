# Informe de Seguridad para la Plataforma SalaryBoost

---

## Introducción

SalaryBoost es una plataforma diseñada para gestionar y optimizar los datos de empleados y supervisores en términos de rendimiento, compensación y administración. Este informe aborda las medidas de seguridad implementadas en la plataforma, en cumplimiento con los requisitos de negocio, seguridad, y otros requerimientos técnicos. Asimismo, se destacan áreas que requieren mejoras futuras.

---

## 1. Cumplimiento de los Requerimientos de Negocio

### 1.1. Generación de Valor con los Datos
El valor de los datos en SalaryBoost se genera principalmente a través de la gestión eficiente de los empleados y la toma de decisiones basadas en su desempeño. El sistema permite a los supervisores:

- Filtrar empleados que cumplen con ciertos criterios de rendimiento (Performance Score y Current Employee Rating).
- Aplicar aumentos salariales y modificar datos de empleados en función de estos criterios.

Esto proporciona un impacto positivo medible en KPIs clave como la retención de empleados, satisfacción laboral, y productividad. Los supervisores pueden hacer un seguimiento de estos indicadores para evaluar el éxito de la plataforma.

### 1.2. Protección de Datos de Acuerdo con la Ley
La plataforma cumple con la **Ley Peruana de Protección de Datos Personales (Ley Nº 29733)** al asegurar que los datos personales de los empleados y supervisores sean manejados de manera confidencial, implementando medidas de seguridad como:

- **Cifrado**: La transmisión de datos está protegida con certificados SSL, asegurando que la información personal esté cifrada durante el tránsito.
- **Gestión de Accesos**: Solo usuarios autenticados (empleados y supervisores) tienen acceso a los datos personales y laborales relevantes.
- **Control de Modificación**: Los supervisores tienen permisos específicos para modificar los datos de empleados, siempre sujetos a la autenticación adecuada.

---

## 2. Cumplimiento de los Requerimientos de Seguridad

### 2.1. Estrategias de Uso Seguro de los Datos
Para garantizar el uso seguro de los datos en la plataforma, se han implementado las siguientes estrategias:

- **Políticas de Gestión de Acceso**: Solo los supervisores pueden realizar cambios en los datos de los empleados y registrar nuevos empleados. Los empleados solo pueden ver y modificar sus propios datos personales y laborales.
- **Procedimientos de Concientización (Awareness)**: Los usuarios son educados sobre la importancia de las contraseñas seguras y el uso de la autenticación multifactor (MFA).
- **Formación del Equipo**: Se recomienda la formación constante del equipo de desarrollo y usuarios finales en prácticas de ciberseguridad, como la detección de posibles amenazas y el manejo seguro de datos.

### 2.2. Plan de Respuesta ante Incidentes de Seguridad
Se ha establecido un plan básico para mitigar incidentes de seguridad en caso de fuga o pérdida de datos:

- **Notificación Rápida**: En caso de incidente, se notificará inmediatamente al equipo de soporte y a los administradores del sistema.
- **Aislamiento y Recuperación**: Se aislará la base de datos afectada y se procederá a la recuperación mediante **backups** periódicos.
- **Reporte de Incidente**: Se documentará el incidente y se informará a las autoridades y usuarios afectados, cumpliendo con la normativa vigente.

---

## 3. Cumplimiento de Otros Requerimientos Técnicos

### 3.1. Uso de Certificados Digitales
SalaryBoost utiliza **certificados SSL** para garantizar la transmisión segura de datos entre el servidor y los usuarios. El certificado SSL autofirmado garantiza que todas las comunicaciones estén cifradas y protegidas contra ataques de intermediario (Man-in-the-Middle).

### 3.2. Funcionalidades Basadas en Roles
Se implementan roles claramente definidos entre empleados y supervisores para garantizar una correcta gestión de datos:

- **Supervisores**:
  - Filtrar empleados en base a rendimiento.
  - Aplicar aumentos salariales.
  - Modificar, registrar y eliminar empleados de la base de datos.
  - Visualizar y modificar sus propios datos personales.

- **Empleados**:
  - Visualizar sus datos personales y laborales.
  - Modificar su contraseña de cuenta de Gmail.

### 3.3. Registros de Auditoría (Logs)
La plataforma cuenta con logs básicos para registrar las acciones de los supervisores, como la creación, modificación y eliminación de empleados. Estos logs permiten rastrear cambios y ayudar en la resolución de incidentes.

### 3.4. Gestión de Accesos
Se implementa una gestión de accesos robusta mediante autenticación multifactor (MFA) usando el módulo **smtplib.SMTP**, lo que asegura que los usuarios solo puedan acceder mediante la verificación de un código de un solo uso enviado a su cuenta de correo.

### 3.5. Cifrado y Protección contra SQL Injection
Se emplean certificados SSL para cifrar la transmisión de datos, y aunque no se muestra explícitamente en el código, se recomienda mejorar la protección contra **SQL Injection** mediante consultas parametrizadas y una validación exhaustiva de entradas de usuarios.

### 3.6. Backups
SalaryBoost realiza **backups periódicos** de la base de datos para prevenir la pérdida de datos en caso de fallos del sistema o incidentes de seguridad.

---

## Conclusiones

SalaryBoost cumple con varios requerimientos clave en cuanto a seguridad, gestión de datos y requisitos técnicos. A través de la implementación de SSL, autenticación de dos factores y gestión de accesos, se asegura la protección de los datos sensibles de los empleados y supervisores. Sin embargo, se recomienda implementar las siguientes mejoras a futuro:

### Recomendaciones de Protección de Datos Futura

1. **Auditoría de Seguridad Periódica**
   - **Justificación**: La implementación de auditorías de seguridad regulares permitirá identificar y corregir vulnerabilidades antes de que sean explotadas. Estas auditorías pueden ayudar a evaluar la eficacia de las medidas de seguridad actuales y garantizar el cumplimiento con las mejores prácticas.

2. **Educación y Concientización en Ciberseguridad**
   - **Justificación**: Invertir en programas de formación continua para todos los empleados sobre las mejores prácticas en ciberseguridad es crucial. Esto ayudará a crear una cultura de seguridad dentro de la organización y a reducir el riesgo de errores humanos que podrían comprometer los datos.

3. **Implementación de un Sistema de Gestión de Incidentes de Seguridad**
   - **Justificación**: Desarrollar un sistema robusto para gestionar incidentes de seguridad garantizará que todos los incidentes sean registrados, analizados y tratados de manera eficiente. Esto permitirá una respuesta rápida y efectiva a cualquier fuga de datos o incidente de seguridad.

4. **Mejoras en la Autenticación Multifactor (MFA)**
   - **Justificación**: Considerar la adopción de métodos de MFA más avanzados, como biometría o tokens de hardware, podría aumentar la seguridad del acceso a la plataforma. Esto dificultará el acceso no autorizado incluso si las credenciales se ven comprometidas.

5. **Implementación de Políticas de Retención de Datos**
    - **Justificación**: Desarrollar políticas claras sobre la retención y eliminación de datos ayudará a garantizar que la organización no mantenga información innecesaria, reduciendo el riesgo en caso de una violación de datos. Esto es especialmente importante para cumplir con las regulaciones de protección de datos.

Implementar estas recomendaciones fortalecerá aún más la plataforma SalaryBoost y garantizará el cumplimiento de estándares de seguridad más altos.
