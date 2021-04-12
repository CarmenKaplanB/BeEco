import mysql.connector

class Alumnos():
# Conexion
        def connect(self):
            try:
                self.cnx = mysql.connector.connect(
                    # Usamos el nombre de nuestro usuario con la contrasena.
                    user='hjqz78ypq3u6ghdf', 
                    password='biodqrcu5739n88h',
                    host='ol5tz0yvwp930510.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                    port=3306,
                    database='bwnvg0mm64o1zf73'
                    )
                self.cursor = self.cnx.cursor()

            except Exception as e:
                print(e)


        # Realizamos una consulta de todos los datos existentes de todas las columnas y filas
        def select(self):
            try:
                self.connect()
                # Consulta
                query = ("SELECT * from alumnos;")
                self.cursor.execute(query)
                # Arreglo
                result = []
                for row in self.cursor:
                    # Diccionario para almacenamiento
                    r = {
                        'id_alumno':row[0],
                        'nombre':row[1],
                        'primer_apellido':row[2],
                        'contrasena':row[3],
                        'fecha_nacimiento':row[4],
                    }
                    result.append(r)
                self.cursor.close()
                self.cnx.close()
                return result

            except Exception as e:
                print(e)
                # En caso de que haya problemas con el diccionario
                result = []
                return result
    # Insertar

        def insertar(self, nombre, primer_apellido, contrasena, fecha_nacimiento):
            try:
                self.connect()
                query = ("INSERT INTO alumnos (nombre, primer_apellido, contrasena, fecha_nacimiento) values(%s, %s, %s, %s);")
                values = (matricula, nombre, primer_apellido, contrasena, fecha_nacimiento)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False

    # Eliminar

        def borrar(self, id_alumno, ):
            try:
                self.connect()
                query = ("DELETE FROM alumnos WHERE id_alumno = %s;")
                values = (id_alumno,)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False

    # Vista

        def view(self, id_alumno):
            try:
                self.connect()
                query = ("SELECT * from alumnos where id_alumno = %s;")
                values = (id_alumno,)
                self.cursor.execute(query, values)
                result = []
                for row in self.cursor:
                     r = {
                        'id_alumno':row[0],
                        'nombre':row[1],
                        'primer_apellido':row[2],
                        'contrasena':row[3],
                        'fecha_nacimiento':row[4],
                    }
                result.append(r)
                self.cursor.close()
                self.cnx.close()
                return result
            except Exception as e:
                print(e)
                result = []
                return result

    # Actualizar

        def modificar(self, id_alumno, nombre, primer_apellido, contrasena, fecha_nacimiento):
            try:
                self.connect()
                query = ("UPDATE alumnos SET  nombre=%s, primer_apellido=%s, contrasena=%s, fecha_nacimiento=%s WHERE id_alumno=%s;")
                values = (nombre, primer_apellido, contrasena, fecha_nacimiento, id_alumno)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False


objeto = Alumnos()
objeto.connect()

# objeto.modificar(7, 123423567,'Melanie', 'Kaplan', 'Armstrong', 19, '2000-10-10', 'Femenino', 'Soltero'),
#for row in objeto.select():
#    print(row)

for row in objeto.view(1):
    print(row)
    
    # En caso de requerir solo uno es como:
    # print(row['nombre'])

