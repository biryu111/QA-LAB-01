# QA-LAB-01: Configuración del Entorno de Pruebas

## Objetivo
Configurar el entorno de desarrollo, implementar funciones básicas y verificarlas
con pruebas automatizadas usando pytest.

## Herramientas utilizadas
- Python 3.x
- pytest
- Git / GitHub
- Visual Studio Code

## Estructura del proyecto
qa-lab-01/
├── src/
│   ├── __init__.py
│   └── calculadora.py
├── tests/
│   ├── test_saludo.py
│   └── test_calculadora.py
├── docs/
├── conftest.py
├── README.md
└── requirements.txt

## Instrucciones de ejecución
1. Clonar el repositorio:
   git clone URL_DEL_REPOSITORIO
2. Instalar pytest:
   pip install pytest
3. Ejecutar pruebas:
   pytest -v

## Resultado de las pruebas
tests/test_saludo.py::test_saludar             PASSED
tests/test_calculadora.py::test_suma           PASSED
tests/test_calculadora.py::test_resta          PASSED
tests/test_calculadora.py::test_multiplicacion PASSED
tests/test_calculadora.py::test_division       PASSED
5 passed in 0.02s

## Importancia de las pruebas automatizadas
Las pruebas automatizadas detectan errores de forma temprana y garantizan
que el código funcione correctamente ante cualquier cambio.

## Autor
Biryu Nadin Valencia Quispe
Curso: Pruebas y Aseguramiento de Calidad de Software - IS489