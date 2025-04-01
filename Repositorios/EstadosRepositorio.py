import pyodbc;
from Entidades import Estados;
from Utilidades import Configuracion;

class EstadosRepositorio:

	def Listar(self) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

			consulta: str = """{CALL proc_select_estados();}""";
			cursor = conexion.cursor();
			cursor.execute(consulta);

			lista: list = [];
			for elemento in cursor:
				entidad: Estados = Estados.Estados();
				entidad.SetId(elemento[0]);
				entidad.SetNombre(elemento[1]);
				lista.append(entidad);

			cursor.close();
			conexion.close();

			for estado in lista:
				print(str(estado.GetId()) + ", " + estado.GetNombre());
		except Exception as ex:
			print(str(ex));