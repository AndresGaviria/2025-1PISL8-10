import datetime;
import decimal;
import pyodbc;
from Entidades import Estados;
from Repositorios import Repositorio;

estado = Estados.Estados();
print(estado.GetNombre());

repositorio = Repositorio.Repositorio();
repositorio.ConexionBasica();
# repositorio.ConexionBasica2();
# repositorio.ConexionBasica3();
# repositorio.ConexionBasica4();

"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""