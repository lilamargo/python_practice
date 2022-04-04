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
sql = 'SELECT * FROM personas'

# Utilizar método Execute para ejecutar sentencia. 
cursor.execute(sql)

# Mostrar resultado, usamos fetchall 
# que muestra todos los dato que hagamos de manera global. Existen otros tipos de fetch.
registro = cursor.fetchall()

for fila in registro:
    print(fila)

# Cerrar conexión
cursor.close()
conexion.close()