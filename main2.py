import jwt;

try:
    print("JWT");
    clave = "12346467987987";

    valor = jwt.encode({"Usuario":"HolaMundo"}, clave, algorithm="HS256");
    print(valor);

    resultado = jwt.decode(valor, clave, algorithms="HS256");
    print(resultado);
except Exception as ex:
    print(ex);

"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main1.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install PyJWT
"""
