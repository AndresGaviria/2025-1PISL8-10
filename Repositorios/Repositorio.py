import pyodbc;
from Entidades import Estados;
from Utilidades import Configuracion;

class Repositorio:

	def ConexionBasica(self) -> None:
		conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

		consulta: str = """SELECT * FROM estados""";
		cursor = conexion.cursor();
		cursor.execute(consulta);

		for elemento in cursor:
			print(elemento);

		cursor.close();
		conexion.close();

	def ConexionBasica2(self) -> None:
		conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

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
		conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

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
		conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

		consulta: str = """INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Test');""";
		cursor = conexion.cursor();
		cursor.execute(consulta);
		cursor.commit();

		cursor.close();
		conexion.close();