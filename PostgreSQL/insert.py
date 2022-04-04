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

# Crear sentencia SQL
sql = 'INSERT INTO personas(nombre,apellido,edad) VALUES(%s, %s, %s)' 

# Solicitud de datos al usuario 
nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')
edad = input('Ingrese la edad: ')

# Recolección de Datos
datos = (nombre, apellido, edad)

# Hacer uso del método Execute para ejecutar sentencia.
cursor.execute(sql, datos)

# Guardar registros
conexion.commit()

# Registros insertados
registros = cursor.rowcount

# Mostrar mensaje
print(f'Registro insertado: {registros}')

# Cerrar conexión
cursor.close()
conexion.close()