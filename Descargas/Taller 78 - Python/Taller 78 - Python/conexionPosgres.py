# conexion en posglessql

import psycopg2

#cursor = None
try:
    conexion = psycopg2.connect(

        host="localhost", port="5438", database="banco", user="prueba", password="aeiou123"
    )
    cursorr = conexion.cursor()
    cursorr.execute("SELECT * FROM cuenta")
    record = cursorr.fetchall()
    print("You are connected to - ", record, "\n")

except Exception as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    # if(conexion):
    cursorr.close()
    conexion.close()
    print("PostgreSQL connection is closed")
