from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END

import psycopg2

root = Tk()
root.title("Python & PosgreSQL Transaccion")


#hostt= "localhost"
#portt = "5438"
# db = "banco"
# user = "prueba"
# password = "aeiou123"

def search(id):
    conn = psycopg2.connect(host=hostt, port=portt, database=db, user= user, password=password)
    cursor = conn.cursor()
    query = '''SELECT saldo FROM cuenta where idcuenta=%s'''
    cursor.execute(query, (id))

    row = cursor.fetchone()
    print(row)
    display_search_result(row)

    conn.commit()
    conn.close()


def display_search_result(row):
    listbox = Listbox(frame, width=8, height=1)
    listbox.grid(row=5, columnspan=3, sticky=E)
    listbox.insert(END, row)


def consultar_estado_cuenta():
    conn = psycopg2.connect( host=hostt, port=portt, database=db, user= user, password=password)
    cursor = conn.cursor()
    query = '''SELECT * FROM cuenta'''
    cursor.execute(query)
    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=4)
    listbox.grid(row=11, columnspan=4, sticky=W+E)
    for x in row:
      listbox.insert(END, x)

    conn.commit()
    conn.close()
  
    

def PA_INSERTAR_TRANSACCIONAL(PIDCUENTAORIGEN, PIDCUENTADESTINO, PVALOR):
  
    with psycopg2.connect(
         host=hostt, port=portt, database=db, user= user, password=password
    ) as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("CALL PA_INSERTAR_TRANSACCIONAL(%s, %s, %s)", (PIDCUENTAORIGEN, PIDCUENTADESTINO, PVALOR))
                conn.commit()
                #cursor.execute("SELECT result FROM my_table WHERE id = 1")
                #result = cursor.fetchone()[0]
                print("succesfully data inserted")
                # cursor.close()
                # conn.close()
                return True
            except:
                conn.rollback()
                return False
            finally:
                cursor.close()
                conn.close()
def PA_INSERTAR_NO_TRANSACCIONAL(PIDCUENTAORIGEN, PIDCUENTADESTINO, PVALOR):
    with psycopg2.connect(
        host=hostt, port=portt, database=db, user= user, password=password
    ) as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("CALL PA_INSERTAR_NO_TRANSACCIONAL(%s, %s, %s)", (PIDCUENTAORIGEN, PIDCUENTADESTINO, PVALOR))
                conn.commit()
                #cursor.execute("SELECT result FROM my_table WHERE id = 1")
                #result = cursor.fetchone()[0]
                return True
            except:
                conn.rollback()
                return False
            finally:
                cursor.close()
                conn.close()
def guardar_configuracion(host, puerto, userr, passwordd, dbb):
    global hostt
    global portt
    global db
    global user
    global password
    hostt = host
    portt = puerto
    db = dbb
    user = userr
    password = passwordd
    print("host: ", hostt)
    print("port: ", portt)
    print("db: ", db)   
    



# Canva
canvas = Canvas(root, height=380, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Transaccion: tranferencia bancaria")
label.grid(row=0, column=1)


# Name Input
label = Label(frame, text="Configuraciones de la conexion")
label.grid(row=1, column=0)
label = Label(frame, text="Host")
label.grid(row=2, column=0)
entry_host = Entry(frame)
entry_host.grid(row=2, column=1)
entry_host.focus()
label = Label(frame, text="Puerto")
label.grid(row=3, column=0)
entry_port = Entry(frame)
entry_port.grid(row=3, column=1)
entry_port.focus()
label = Label(frame, text="Usuario")
label.grid(row=2, column=2)
entry_user = Entry(frame)
entry_user.grid(row=2, column=3)
entry_user.focus()
label = Label(frame, text="Contraseña")
label.grid(row=3, column=2)
entry_contraseña = Entry(frame)
entry_contraseña.grid(row=3, column=3)
entry_contraseña.focus()
label = Label(frame, text="DB")
label.grid(row=2, column=4)
entry_db = Entry(frame)
entry_db.grid(row=2, column=5)
entry_db.focus()
# Button
button = Button(frame, text="Guardar Configuración", command=lambda: guardar_configuracion(entry_host.get(), entry_port.get(), entry_user.get(), entry_contraseña.get(), entry_db.get() ))
button.grid(row=1, column=3)


# Name Input
label = Label(frame, text="Buscar cuenta por ID")
label.grid(row=4, column=0)

entry_id = Entry(frame)
entry_id.grid(row=4, column=1)
entry_id.focus()
# Button
button = Button(frame, text="Buscar", command=lambda: search(entry_id.get()))
button.grid(row=4, column=2, sticky=W+E)



# Button
button = Button(frame, text="Consultar todo", command=lambda: consultar_estado_cuenta())
button.grid(row=4, column=3, sticky=W+E)

# transaccion 
label = Label(frame, text="Transferir dinero")#titulo 
label.grid(row=5, column=1)

label = Label(frame, text="ID cuenta origen")#etiqeta
label.grid(row=6, column=0)

id_origen = Entry(frame)                    #entrada
id_origen.grid(row=6, column=1)

label = Label(frame, text="ID cuenta destino")
label.grid(row=7, column=0)

id_destino = Entry(frame)
id_destino.grid(row=7, column=1)

label = Label(frame, text="El valor a transferir")
label.grid(row=8, column=0)

v_trans = Entry(frame)
v_trans.grid(row=8, column=1)

button = Button(frame, text="Tranferir (Modo Transaccional)", command=lambda: PA_INSERTAR_TRANSACCIONAL(id_origen.get(), id_destino.get(), v_trans.get())) 
button.grid(row=9, column=1)

button = Button(frame, text="Tranferir (Modo No Transaccional)", command=lambda: PA_INSERTAR_NO_TRANSACCIONAL(id_origen.get(), id_destino.get(), v_trans.get()))
button.grid(row=10, column=1)



# display_students()
root.mainloop()
