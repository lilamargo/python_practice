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

# Sentencia SQL
sql = 'DELETE FROM personas WHERE idpersonas=%s'

# Solicitar dato al usuario.
idpersonas = input('Ingrese el ID del registro que desea eliminar: ')

# Utilizar el método Execute.
cursor.execute(sql, idpersonas)

# Guardar cambios
conexion.commit()

# Contar el registro eliminado.
eliminar = cursor.rowcount

# Mostrar mensaje de cambio.
print(f'Registros eliminados: {eliminar}')

# Cerrar conexión
cursor.close()
conexion.close()