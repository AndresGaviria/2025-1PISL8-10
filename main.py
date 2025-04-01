import datetime;
import decimal;
import pyodbc;
from Entidades import Estados;

# REPOSITORIO
class Repositorio:
	strConnection: str = """
		Driver={MySQL ODBC 9.0 Unicode Driver};
		Server=localhost;
		Database=db_personas;
		PORT=3306;
		user=user_ptyhon;
		password=Clas3s1Nt2024_!""";

	def ConexionBasica(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """SELECT * FROM estados""";
		cursor = conexion.cursor();
		cursor.execute(consulta);

		for elemento in cursor:
			print(elemento);

		cursor.close();
		conexion.close();

	def ConexionBasica2(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """SELECT * FROM estados""";
		cursor = conexion.cursor();
		cursor.execute(consulta);

		lista: list = [];
		for elemento in cursor:
			entidad: Estados = Estados();
			entidad.SetId(elemento[0]);
			entidad.SetNombre(elemento[1]);
			lista.append(entidad);

		cursor.close();
		conexion.close();

		for estado in lista:
			print(str(estado.GetId()) + ", " + estado.GetNombre());

	def ConexionBasica3(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """SELECT p.id,
				p.cedula,
				p.nombre,
				p.estado,
				p.fecha,
				p.activo,
				e.id,
				e.nombre
			FROM `personas` p INNER JOIN `estados` e ON p.estado = e.id;""";
		cursor = conexion.cursor();
		cursor.execute(consulta);

		for elemento in cursor:
			print(elemento);

		cursor.close();
		conexion.close();

	def ConexionBasica4(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Test');""";
		cursor = conexion.cursor();
		cursor.execute(consulta);
		cursor.commit();

		cursor.close();
		conexion.close();

estado = Estados.Estados();
print(estado.GetNombre());

repositorio = Repositorio();
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