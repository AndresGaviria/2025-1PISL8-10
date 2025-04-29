import hashlib;
import binascii, os;
from Crypto.Cipher import AES;

class EncriptarMD5:
    def Ejecutar(self) -> None:
        valor = "Clase de integracion";
        cifrado = self.Cifrar(valor);
        print(cifrado);

    def Cifrar(self, valor: str) -> str:
        resultado = str(hashlib.md5(valor.encode('utf-8')).hexdigest());
        return resultado;

    def Decifrar(self, valor: str) -> str:
        return None;

encriptarMD5 = EncriptarMD5();
encriptarMD5.Ejecutar();


"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main1.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pycryptodome
"""
