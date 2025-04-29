import jwt;

try:
    print("JWT");
    clave = "kjhdf1gydi4ufy654gi4uy";

    valor = jwt.encode({"Usuario":"123Abc"}, clave, algorithm="HS256");
    print(valor);
    
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
