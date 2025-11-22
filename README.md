# ANALYTIC PRO
Sistema de Análisis y Predicción de Ventas

---

## Información del Curso

| Asignatura | Minería de Datos - 7AR |
| :--- | :--- |
| Docente | Ing. Edgar Morillo Vergel |
| Fecha | Noviembre 2023 |

## Integrantes del Equipo

* Ali Mesino
* Eder Madera
* Jesus Rueda

---

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación web integral utilizando Python, diseñada para automatizar el flujo de trabajo en la minería de datos. La herramienta permite la ingesta de datos crudos de ventas, su procesamiento y limpieza automática, y la posterior generación de valor mediante análisis descriptivo y predictivo.

El objetivo central es facilitar la toma de decisiones basada en datos, permitiendo al usuario visualizar el comportamiento histórico de las ventas y proyectar resultados futuros mediante algoritmos de Machine Learning.

---

## Stack Tecnológico

Se seleccionó un conjunto de librerías especializadas para garantizar la eficiencia en el cálculo matemático y la renderización de gráficos.

| Componente | Tecnología | Función |
| :--- | :--- | :--- |
| Lenguaje | Python 3.11 | Núcleo de lógica y procesamiento. |
| Interfaz | Streamlit | Despliegue de la aplicación web interactiva. |
| Procesamiento | Pandas, NumPy | Manipulación de estructuras de datos y limpieza. |
| Visualización | Plotly Express | Generación de gráficos dinámicos e interactivos. |
| Estadística | Seaborn, Matplotlib | Generación de mapas de calor y correlaciones. |
| Machine Learning | Scikit-Learn | Entrenamiento del modelo de regresión y métricas. |

---

## Arquitectura de Software

El proyecto sigue un patrón de arquitectura modular para asegurar la escalabilidad y el mantenimiento del código. Se ha separado la lógica de negocio (Backend) de la capa de presentación (Frontend).

Estructura del sistema:

main.py (Punto de entrada de la aplicación)
requirements.txt (Gestión de dependencias)
src/
    services/
        data_loader.py (Lógica de extracción y transformación de datos)
        ai_model.py (Lógica de entrenamiento y predicción)
    ui/
        styles.py (Configuración de estilos visuales)
        views/
            home.py (Módulo de bienvenida)
            dashboard.py (Módulo de análisis exploratorio)
            prediction.py (Módulo de modelado predictivo)
    utils/
        constants.py (Variables globales)

---

## Funcionalidades Principales

### 1. Gestión y Limpieza de Datos
El sistema implementa un algoritmo de carga resiliente capaz de interpretar archivos CSV con diferentes delimitadores (comas o puntos y coma). Incluye procesos automáticos para la conversión de formatos numéricos (monedas y decimales europeos) y la eliminación de registros duplicados para asegurar la integridad de la información.

### 2. Análisis Exploratorio de Datos (EDA)
Se dispone de un panel de control que ofrece una visión completa del estado del negocio:
* Cálculo de métricas clave (KPIs) como ventas totales y promedios.
* Visualización de rankings y tendencias temporales.
* Análisis de distribución mediante diagramas de caja (Boxplots).
* Matrices de correlación para identificar relaciones entre variables numéricas.

### 3. Modelo Predictivo
El sistema incorpora un motor de Inteligencia Artificial basado en Regresión Lineal Múltiple.
* Preprocesamiento: Estandarización de variables numéricas y codificación de variables categóricas.
* Entrenamiento: División automática de datos en conjuntos de entrenamiento y prueba.
* Evaluación: Cálculo de coeficiente de determinación (R²) y error cuadrático medio (MSE).
* Simulación: Interfaz para la proyección de ventas basada en parámetros ingresados por el usuario.

---

## Cumplimiento de Objetivos

El desarrollo del proyecto abarca la totalidad de los requerimientos establecidos en la rúbrica de evaluación:

1. Limpieza y manejo de datos: Implementado en el módulo de servicios mediante Pandas.
2. Análisis exploratorio: Implementado mediante gráficos interactivos y estadísticos.
3. Modelado y predicción: Implementado mediante Scikit-Learn con métricas de validación.
4. Aplicación web: Despliegue funcional y navegable mediante Streamlit.
5. Presentación y código: Estructura organizada modularmente siguiendo buenas prácticas de ingeniería.

---
Universidad de la Costa - 2023