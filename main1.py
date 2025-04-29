import hashlib;
import binascii, os;
from Crypto.Cipher import AES;

class EncriptarMD5:
    def Ejecutar(self) -> None:
        valor = "Clase";
        cifrado = self.Cifrar(valor);
        print(cifrado);
        valor = "ClasE";
        cifrado = self.Cifrar(valor);
        print(cifrado);
        valor = "ClaSE";
        cifrado = self.Cifrar(valor);
        print(cifrado);

    def Cifrar(self, valor: str) -> str:
        resultado = str(hashlib.md5(valor.encode('utf-8')).hexdigest());
        return resultado;

    def Decifrar(self, valor: str) -> str:
        return None;

class EncriptarAES:
    secretKey = os.urandom(32);

    def Ejecutar(self) -> None:
        valor = "Test";
        cifrado = self.Cifrar(valor);
        print(cifrado);

        decifrado = self.Decifrar(cifrado);
        print(decifrado);

    def Cifrar(self, valor: str) -> str:
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
        return (ciphertext, aesCipher.nonce, authTag);

    def Decifrar(self, valor: str) -> str:
        (ciphertext, nonce, authTag) = valor;
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext;

encriptarMD5 = EncriptarMD5();
encriptarMD5.Ejecutar();

encriptarAES = EncriptarAES();
encriptarAES.Ejecutar();

"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main1.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pycryptodome
"""
