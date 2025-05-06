import flask;
import jsonify;
import pyodbc;
import hashlib;
import binascii, os;
from Crypto.Cipher import AES;

class EncriptarAES:
    secretKey = b'\x11\x9b$\xe8\x13\xe7\x18\xe7\x8e{\x86v\x1ab\x8c\xb7\x911Q@ \xca\xa4e\xc75H\x95\x89\xa6\x9d\xab';

    def Cifrar(self, valor: str) -> str:
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
        response = (ciphertext, aesCipher.nonce, authTag);
        return binascii.hexlify(response[0]).decode() + '|' + binascii.hexlify(response[1]).decode() + '|' + binascii.hexlify(response[2]).decode();

    def Decifrar(self, valor: str) -> str:
        split = valor.split('|');
        ciphertext = binascii.unhexlify(split[0]);
        nonce = binascii.unhexlify(split[1]);
        authTag = binascii.unhexlify(split[2]);
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext.decode();

class Repositorio:
	encriptarAES = EncriptarAES();
	strConnection: str = """
		Driver={MySQL ODBC 9.0 Unicode Driver};
		Server=localhost;
		Database=db_personas;
		PORT=3306;
		user=user_ptyhon;
		password=Clas3s1Nt2024_!""";

	def Listar(self, datos: dict) -> dict:
		respuesta: dict = {};
		try:
			conexion = pyodbc.connect(self.strConnection);

			consulta: str = """SELECT * FROM estados""";
			cursor = conexion.cursor();
			cursor.execute(consulta);

			contador = 0;
			for elemento in cursor:
				lista: dict = {};
				lista["Id"] = elemento[0];
				lista["Nombre"] = self.encriptarAES.Decifrar(elemento[1]);
				respuesta[str(contador)] = lista;
				contador = contador + 1;

			cursor.close();
			conexion.close();

			return respuesta;
		except Exception as ex:
			respuesta["Error"] = ex;
			return respuesta;

app = flask.Flask(__name__);
@app.route('/main3/Listar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Listar(entrada: str) -> str:
    respuesta = { };
    try:
        entrada = entrada.replace("'", '"');
        datos = json.loads(entrada);
        
        repositorio = Repositorio();
        respuesta = repositorio.Listar(datos);
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        return respuesta;

app.run('localhost', 4041);

"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main3.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify
py -m pip install pycryptodome

"""