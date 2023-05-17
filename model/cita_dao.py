from tkinter import messagebox
import sqlite3
def crearTabla():
    base_datos= "database/citas.db"
    con=sqlite3.connect(base_datos, isolation_level= None)
    cursor= con.cursor()
    sql='''
    CREATE TABLE Citas (
        id INTEGER,
        nombre VARCHAR(100),
        direccion VARCHAR(30),
        productos VARCHAR(200),
        PRIMARY KEY(id AUTOINCREMENT)
    );
    '''
    try:
        cursor.execute(sql)
        cursor.close()
        con.close
    except:
        pass

def borrar_tabla():
    base_datos= "database/citas.db"
    con=sqlite3.connect(base_datos, isolation_level= None)
    cursor= con.cursor()
    sql = 'DROP TABLE Citas;'
    try:
        cursor.execute(sql)
        cursor.close()
        titulo= "Eliminar Tabla"
        mensaje = "Se eliminó la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo= "Eliminar Tabla"
        mensaje = "La tabla no existe"
        messagebox.showwarning(titulo, mensaje)
        
class Cita:
    def __init__(self, nombre, direccion, productos):
        self.id=None
        self.nombre= nombre
        self.direccion= direccion
        self.productos= productos
        
    def __str__(self):
        return  f'Cita[{self.nombre}, {self.direccion}, {self.productos}]'
    
def guardar(cita):
    base_datos= "database/citas.db"
    con=sqlite3.connect(base_datos, isolation_level= None)
    cursor= con.cursor()
    sql= f"""INSERT INTO Citas(nombre, direccion, productos) VALUES ("{cita.nombre}", "{cita.direccion}", "{cita.productos}");"""
    try:
        cursor.execute(sql)
        cursor.close()
    except:
        titulo= "Conexion al Registro"
        mensaje = "La tabla no existe"
        messagebox.showerror(titulo, mensaje)
        
def listar():
    base_datos= "database/citas.db"
    con=sqlite3.connect(base_datos, isolation_level= None)
    cursor= con.cursor()
    listaCitas= []
    sql="SELECT * FROM Citas;"
    try:
        cursor.execute(sql)
        listaCitas=cursor.fetchall()
        cursor.close()
    except:
        titulo= "Conexion al Registro"
        mensaje = "La tabla no existe"
        messagebox.showerror(titulo, mensaje)
    
    return listaCitas

def editar(cita, id):
    base_datos= "database/citas.db"
    con=sqlite3.connect(base_datos, isolation_level= None)
    cursor= con.cursor()
    sql=f"""UPDATE Citas
    SET nombre= "{cita.nombre}", direccion="{cita.direccion}", productos="{cita.productos}" WHERE id= "{id}";
    """
    try:
        cursor.execute(sql)
        cursor.close()
    except:
        titulo= "Conexion al Registro"
        mensaje = "No se pudo editar"
        messagebox.showerror(titulo, mensaje)

def eliminar(id):
    base_datos= "database/citas.db"
    con=sqlite3.connect(base_datos, isolation_level= None)
    cursor= con.cursor()

    sql=f"DELETE FROM Citas WHERE id= {id};"
    try:
        cursor.execute(sql)
        cursor.close()
    except:
        titulo= "Conexion al Registro"
        mensaje = "No se pudo eliminar"
        messagebox.showerror(titulo, mensaje) 