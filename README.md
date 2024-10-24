# Informe de Seguridad para la Plataforma SalaryBoost

---

## Introducción

**SalaryBoost** es una plataforma diseñada para gestionar y optimizar los datos de empleados y supervisores en términos de rendimiento, compensación, y administración. Este informe aborda las medidas de seguridad implementadas en la plataforma, en cumplimiento con los requisitos de negocio, seguridad, y otros requisitos técnicos. Asimismo, se destacan áreas que requieren mejoras futuras.

---

## 1. Cumplimiento de los Requerimientos de Negocio

### 1.1. Generación de Valor con los Datos
El valor de los datos en **SalaryBoost** se genera a través de la gestión eficiente de los empleados y la toma de decisiones basadas en su desempeño. El sistema permite a los supervisores:

- Filtrar empleados que cumplen con ciertos criterios de rendimiento (*Performance Score* y *Current Employee Rating*).
- Aplicar aumentos salariales y modificar datos de empleados en función de estos criterios.

Esto proporciona un impacto positivo medible en KPIs clave como la retención de empleados, satisfacción laboral, y productividad.

### 1.2. Protección de Datos de Acuerdo con la Ley
La plataforma cumple con la **Ley Peruana de Protección de Datos Personales (Ley Nº 29733)** mediante las siguientes medidas:

- **Cifrado**: La transmisión de datos está protegida con certificados SSL, asegurando que la información personal esté cifrada durante el tránsito.
- **Gestión de Accesos**: Solo usuarios autenticados (empleados y supervisores) tienen acceso a los datos personales y laborales relevantes.
- **Control de Modificación**: Los supervisores tienen permisos específicos para modificar los datos de empleados, siempre sujetos a la autenticación adecuada.

---

## 2. Cumplimiento de los Requerimientos de Seguridad

### 2.1. Estrategias de Uso Seguro de los Datos

- **Políticas de Gestión de Acceso**: Solo los supervisores pueden realizar cambios en los datos de los empleados y registrar nuevos empleados. Los empleados solo pueden ver y modificar sus propios datos personales y laborales.
- **Procedimientos de Concientización (Awareness)**: Los usuarios son educados sobre la importancia de las contraseñas seguras y el uso de la autenticación multifactor (MFA).
- **Formación del Equipo**: Se recomienda la formación constante del equipo de desarrollo y usuarios finales en prácticas de ciberseguridad.

### 2.2. Plan de Respuesta ante Incidentes de Seguridad
Un plan básico ha sido establecido para mitigar incidentes de seguridad en caso de fuga o pérdida de datos:

- **Notificación Rápida**: Se notificará inmediatamente al equipo de soporte y a los administradores del sistema en caso de incidente.
- **Aislamiento y Recuperación**: Se aislará la base de datos afectada y se procederá a la recuperación mediante **backups** periódicos.
- **Reporte de Incidente**: Se documentará el incidente y se informará a las autoridades y usuarios afectados, cumpliendo con la normativa vigente.

### 2.3. Recomendaciones Futuras de Protección de Datos

Existen medidas de seguridad que no se han implementado pero que se recomiendan para el futuro:

- **Cifrado de Contraseñas en la Base de Datos**: Implementar algoritmos como bcrypt o Argon2 para cifrar las contraseñas en la base de datos.
- **Auditoría de Seguridad**: Implementar una auditoría periódica para revisar vulnerabilidades y actualizar las medidas de protección.
- **Registro Detallado de Logs**: Mejorar la gestión de logs para registrar acciones críticas y detectar comportamientos inusuales.
- **Protección Avanzada contra Ataques SQL Injection**: Profundizar en el uso de consultas parametrizadas en todas las interacciones con la base de datos.
- **Cifrado de Datos en Reposo**: Implementar un cifrado avanzado de los datos en reposo dentro de la base de datos.

---

## 3. Cumplimiento de Otros Requerimientos Técnicos

### 3.1. Uso de Certificados Digitales
SalaryBoost utiliza **certificados SSL** para garantizar la transmisión segura de datos entre el servidor y los usuarios. El certificado SSL autofirmado asegura que todas las comunicaciones estén cifradas y protegidas contra ataques de intermediario (*Man-in-the-Middle*).

### 3.2. Funcionalidades Basadas en Roles
Se implementan roles definidos para garantizar una correcta gestión de datos:

- **Supervisores**:
  - Filtrar empleados en base a rendimiento.
  - Aplicar aumentos salariales.
  - Modificar, registrar y eliminar empleados de la base de datos.
  - Visualizar y modificar sus propios datos personales.
  
- **Empleados**:
  - Visualizar sus datos personales y laborales.
  - Modificar su contraseña de cuenta de Gmail.

### 3.3. Registros de Auditoría (Logs)
La plataforma cuenta con **logs básicos** para registrar las acciones críticas de los supervisores, como la creación, modificación y eliminación de empleados. Esto ayuda en la resolución de incidentes y auditorías.

### 3.4. Gestión de Accesos
Se implementa una gestión de accesos robusta mediante autenticación multifactor (MFA) utilizando **smtplib.SMTP**. Esto asegura que solo usuarios autenticados puedan acceder mediante un código de verificación de un solo uso enviado a su correo electrónico.

### 3.5. Cifrado y Protección contra SQL Injection
Se emplean certificados SSL para cifrar la transmisión de datos. Aunque no se ha mostrado explícitamente en el código, se recomienda fortalecer la protección contra **SQL Injection** mediante consultas parametrizadas y validación exhaustiva de entradas de usuarios.

### 3.6. Backups
SalaryBoost realiza **backups periódicos** de la base de datos para prevenir la pérdida de datos en caso de fallos del sistema o incidentes de seguridad.

---

## Conclusiones

SalaryBoost cumple con varios requerimientos clave en cuanto a seguridad, gestión de datos y requisitos técnicos. Las siguientes medidas ya se encuentran implementadas:

- Uso de certificados SSL para transmisión segura.
- Gestión de accesos basada en roles.
- Autenticación multifactor (MFA) para aumentar la seguridad de los usuarios.
- Backups periódicos para protección contra pérdida de datos.

**Recomendaciones Futuras**:

- **Cifrado de contraseñas** en la base de datos.
- **Consultas parametrizadas** para evitar ataques de inyección SQL.
- **Auditorías de seguridad** y **logs detallados**.
- **Cifrado de datos en reposo**.

Estas mejoras fortalecerán la plataforma SalaryBoost y garantizarán el cumplimiento de estándares de seguridad más altos.

