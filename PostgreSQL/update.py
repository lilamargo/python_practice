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

# Crear sentencia sql.
sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE idpersonas=%s'

# Solicitud de datos que se quieren actualizar a usuario.
idpersonas = input('Ingrese id de la persona a editar: ')
nombre = input('Ingrese nombre a actualizar: ')
apellido = input('Ingrese apellido a actualizar: ')
edad = input('Ingrese edad a actualizar: ')

# Recolección de Datos
datos = (nombre, apellido, edad, idpersonas)

# Utilizar el método Execute para ejecutar sentencia.
cursor.execute(sql, datos)

# Guardar actualización/modificación.
conexion.commit()

# Contar el número de actualizaciones.
actualizacion = cursor.rowcount


# Mostrar mensaje de cambio.
print(f'Actualización registrada: {actualizacion}')

# Cerrar conexión
cursor.close()
conexion.close()