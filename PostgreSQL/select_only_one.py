# Importación del modulo
import psycopg2

# Conexión a Base de Datos
conexion = psycopg2.connect(user='postgres', 
                            password= '123456789', 
                            host='localhost', 
                            port='5432', 
                            database='db_personas')

# Ahora utilizaremos el método CURSOR 
# nos sirve para hacer ciertas funciones como ejecución, mostrar registros, cerrar conexión, etc.
cursor = conexion.cursor()

# Crear sentencia SQL que enviará la base de datos para obtener una respuesta.
sql = 'SELECT * FROM personas WHERE idpersonas=%s'

# Solicitar datos a usuario.
idpersonas = input('Ingrese el ID de la persona a mostrar: ')

# Utilizar método Execute para ejecutar sentencia. 
cursor.execute(sql, idpersonas)

# Mostrar resultado, usamos fetone 
# que muestra solo un elemento solicitado. Existen otros tipos de fetch.
registro = cursor.fetchone()
print(registro)

# Cerrar conexión
cursor.close()
conexion.close()