# SalaryBoost - Plataforma de Gestión Salarial

## 1. Objetivo General
La plataforma **SalaryBoost** busca facilitar la gestión de salarios, aumentos y administración de empleados para empresas pequeñas y medianas. Proporciona herramientas tanto a supervisores como a empleados, mejorando la transparencia, eficiencia y satisfacción en la gestión del recurso humano, en un entorno seguro que cumple con los estándares de seguridad de datos.

## 2. Requerimientos de Negocio

### 1. Gestión y Optimización de Salarios
- **Valor generado**: Los supervisores pueden ajustar salarios basados en indicadores clave como **Performance Score** y **Current Employee Rating**.
  
- **Indicadores clave (KPIs)**:
  - **% de empleados con aumento**.
  - **Aumento promedio (%) por trimestre**.
  - **Costo total de los aumentos**.
  
- **Proceso**:
  - Filtrado de empleados que cumplan con los criterios de rendimiento.
  - Aplicación de un porcentaje de aumento salarial basado en el rendimiento.

- **Criterios de Evaluación**:
  - **Current Employee Rating** superior a 8.
  - **Performance Score** al menos "Satisfactorio".

### 2. Seguridad y Protección de Datos
- **Valor generado**: Cumplir con las leyes de protección de datos garantiza la seguridad de la información confidencial de empleados y supervisores.

- **Indicadores clave (KPIs)**:
  - **% de cumplimiento con estándares de seguridad**.
  - **Número de incidentes de seguridad**.

- **Proceso**:
  - Encriptación de datos y credenciales (ej. Gmail).
  - Cumplimiento con la Ley Peruana de Protección de Datos.

### 3. Contingencias y Recuperación de Datos
- **Valor generado**: Asegura la disponibilidad continua de los datos, minimizando riesgos en caso de ataques o fallos.

- **Indicadores clave (KPIs)**:
  - **Frecuencia de backups**.
  - **Tiempo promedio de recuperación (RTO)**.
  - **Pérdida máxima de datos permitida (RPO)**.

- **Proceso**:
  - Revisar los procesos de contingencia periódicamente para adaptarse a nuevas amenazas o cambios legislativos.

### 4. Administración de Usuarios

#### 4.1. Supervisores
- **Valor generado**: Los supervisores pueden gestionar eficientemente los datos de empleados, realizar ajustes salariales, eliminaciones, modificaciones y registros de nuevos empleados.

- **Indicadores clave (KPIs)**:
  - **Tiempo de gestión**.
  - **Satisfacción del supervisor**.

- **Procesos**:
  - Filtrar empleados por **Performance Score** y **Current Employee Rating**.
  - Eliminar empleados con **EmpID**.
  - Modificar datos de empleados filtrando por **EmpID**.
  - Registrar nuevos empleados.

#### 4.2. Empleados
- **Valor generado**: Los empleados acceden a su perfil para visualizar sus datos personales y laborales, verificando si han recibido aumentos salariales.

- **Indicadores clave (KPIs)**:
  - **% de accesos de empleados**.
  - **Satisfacción del empleado**.

- **Procesos**:
  - Ver datos personales: **EmpID**, **FirstName**, **LastName**, **Email**, etc.
  - Ver datos laborales: **Title**, **EmployeeType**, **Performance Score**, **Current Employee Rating**, **monthly_salary**.
  - Cambiar contraseña de correo electrónico.

### 5. Cumplimiento con la Ley de Protección de Datos Personales en Perú
- **Valor generado**: Asegurar la protección de los datos, alineados con normativas locales e internacionales.

- **Indicadores clave (KPIs)**:
  - **% de cumplimiento legal**.
  - **Revisión periódica de políticas de seguridad**.

## 3. Funcionalidades de la Plataforma

1. **Módulo de gestión salarial (supervisores)**:
   - Filtrar empleados por **Performance Score** y **Current Employee Rating**.
   - Ajustar salarios según porcentaje.

2. **Módulo de administración de empleados**:
   - Eliminar empleados con **EmpID**.
   - Modificar datos tras filtrar por **EmpID**.
   - Registrar nuevos empleados.

3. **Módulo de seguridad**:
   - Cambiar contraseñas de Gmail para supervisores y empleados.
   - Acceso seguro con encriptación de datos.

4. **Módulo de visualización (empleados)**:
   - Ver datos personales y laborales.
   - Ver si ha sido beneficiado con un aumento salarial.

5. **Backups y recuperación de datos**:
   - Implementación de backups periódicos y procesos de recuperación ante incidentes.

Con **SalaryBoost**, las empresas gestionan eficientemente los salarios y datos de empleados, brindando seguridad y transparencia en cada paso del proceso.
