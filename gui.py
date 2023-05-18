import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ctypes
from model.cita_dao import crearTabla, borrar_tabla
from model.cita_dao import Cita, guardar, listar, editar, eliminar
import threading


def barra_menu(root):
    barra_menu=tk.Menu(root)
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    anchoPantalla, altoPantalla = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    root.config(menu=barra_menu,width=anchoPantalla, height=20)
    
    #Barra de menus
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    
    #menu_inicio.add_command(label="Crear un registro en base de datos", command=crearTabla)
    #menu_inicio.add_command(label="Eliminar un registro en base de datos", command=borrar_tabla)
    menu_inicio.add_command(label="Salir", command = root.destroy)
    
    barra_menu.add_cascade(label="Consultas", menu=menu_inicio)
    barra_menu.add_cascade(label="Ayuda", menu=menu_inicio)


class frame(tk.Frame):
    def __init__(self, root):
        self.root=root
        self.nombre=tk.StringVar()
        self.direccion=tk.StringVar()
        self.productos=tk.StringVar()
        user32=ctypes.windll.user32
        user32.SetProcessDPIAware()
        self.anchoPantalla=user32.GetSystemMetrics(0)
        self.altoPantalla=user32.GetSystemMetrics(1)
        self.allFont=int(self.anchoPantalla*0.009375)
        root.geometry(str(self.anchoPantalla)+"x"+str(self.altoPantalla))
        super().__init__(root, width=str(self.anchoPantalla), height=str(self.altoPantalla))
        self.size()
        crearTabla()
        self.campos()
        self.deshabilitar_campos()
        self.tabla_citas()
        self.idCita=None
        
        #self.size()
        
    def size(self):
        user32=ctypes.windll.user32
        user32.SetProcessDPIAware()
        self.anchoPantalla=user32.GetSystemMetrics(0)
        self.altoPantalla=user32.GetSystemMetrics(1)
        self.config(bg="white", width=str(self.altoPantalla), height=str(self.altoPantalla))
        self.pack()
        
    def campos(self):
        #labels de los campos
        self.label_nombre=tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=("Arial", self.allFont, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_direccion=tk.Label(self, text="Dirección: ")
        self.label_direccion.config(font=("Arial", self.allFont, "bold"))
        self.label_direccion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_productos=tk.Label(self, text="Productos: ")
        self.label_productos.config(font=("Arial", self.allFont, "bold"))
        self.label_productos.grid(row=2, column=0, padx=10, pady=10)
        
        #entries de los campos
        self.entry_nombre=tk.Entry(self, textvariable= self.nombre) # type: ignore
        self.entry_nombre.config(width=62, font=("Arial", self.allFont, "bold"))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.entry_direccion=tk.Entry(self, textvariable= self.direccion) # type: ignore
        self.entry_direccion.config(width=62, font=("Arial", self.allFont, "bold"))
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.entry_productos=tk.Entry(self, textvariable= self.productos) # type: ignore
        self.entry_productos.config(width=62, font=("Arial", self.allFont, "bold"))
        self.entry_productos.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        
        #botones de los campos
        
        self.boton_nuevo=tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=25, font=("Arial", self.allFont, "bold"), fg="white", bg="#28B463", cursor="hand2", activebackground="#48DC86")
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)
        
        self.boton_guardar=tk.Button(self, text="Guardar", command= self.guardar_Datos)
        self.boton_guardar.config(width=25, font=("Arial", self.allFont, "bold"), fg="white", bg="#2E86C1", cursor="hand2", activebackground="#5DADE2")
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)
        
        self.boton_cancelar=tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=25, font=("Arial", self.allFont, "bold"), fg="white", bg="#E60A0A", cursor="hand2", activebackground="#EA5555")
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)
        
    def habilitar_campos(self):
        self.entry_nombre.config(state="normal")
        self.entry_direccion.config(state="normal")
        self.entry_productos.config(state="normal")
        
        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")
        
    def deshabilitar_campos(self):
        self.nombre.set("")
        self.direccion.set("")
        self.productos.set("")
        self.entry_nombre.config(state="disabled")
        self.entry_direccion.config(state="disabled")
        self.entry_productos.config(state="disabled")
        
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")
        
    def guardar_Datos(self):
        if self.nombre.get()=="":
            titulo= "Crear Registro"
            mensaje = "Coloque un nombre"
            messagebox.showerror(titulo, mensaje)
            return
        if self.direccion.get()=="":
            titulo= "Crear Registro"
            mensaje = "Coloque una dirección"
            messagebox.showerror(titulo, mensaje)
            return
        if self.productos.get()=="":
            titulo= "Crear Registro"
            mensaje = "Coloque los productos"
            messagebox.showerror(titulo, mensaje)
            return
        cita =Cita(
            self.nombre.get(),
            self.direccion.get(),
            self.productos.get()
        )
        
        if self.idCita==None:
            guardar(cita)
        else:
            editar(cita, self.idCita)
        self.tabla_citas()
        self.deshabilitar_campos()
        
    def tabla_citas(self):
        #Recuperar lista
        self.listaCitas=listar()
        self.listaCitas.reverse()
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", self.allFont, "bold"), )
        treeFont=int(self.anchoPantalla*0.0075757575757576)
        style.configure("Treeview", bd=0, font=('Arial', treeFont))
        #tabla
        tHeight=self.altoPantalla*0.0277777777777778
        self.tabla=ttk.Treeview(self, columns= ("Nombre", "Direccion", "Productos"), height=int(tHeight))
        self.tabla.grid(row =5, column=0, columnspan=4, sticky="nse")
        #scroll bar
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row =5, column=4, sticky="nse")
        self.tabla.configure(yscrollcommand= self.scroll.set)
        self.scroll2 = ttk.Scrollbar(self, orient="horizontal", command=self.tabla.xview)
        self.scroll2.grid(row =6, column=0, sticky="nse", columnspan=6)
        self.tabla.configure(xscrollcommand= self.scroll2.set)  
        wclm0=int(self.anchoPantalla)*0.0404040404040404
        wclm1=int(self.anchoPantalla)*0.2525252525252525
        wclm2=int(self.anchoPantalla)*0.3282828282828283
        wclm3=int(self.anchoPantalla)*0.3282828282828283
        self.tabla.column(column="#0",minwidth=int(wclm0),width=int(wclm0), stretch=False)
        self.tabla.column(column="#1",minwidth=int(wclm1),width=int(wclm1), stretch=False)
        self.tabla.column(column="#2",minwidth=int(wclm2),width=int(wclm2), stretch=False)
        self.tabla.column(column="#3",minwidth=int(wclm3),width=int(wclm3), stretch=False)
        
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Direccion")
        self.tabla.heading("#3", text="Productos")
        
        for p in self.listaCitas:
            self.tabla.insert("", 0, text=p[0], values=(p[1], p[2], p[3]))
        #botones de la tabla
        
        self.boton_editar=tk.Button(self, text="Editar", command= self.editarDatos)
        self.boton_editar.config(width=25, font=("Arial", self.allFont, "bold"), fg="white", bg="#28B463", cursor="hand2", activebackground="#48DC86")
        self.boton_editar.grid(row=7, column=0, padx=10, pady=10)
        
        self.boton_eliminar=tk.Button(self, text="Eliminar", command= self.eliminarDatos)
        self.boton_eliminar.config(width=25, font=("Arial", self.allFont, "bold"), fg="white", bg="#E60A0A", cursor="hand2", activebackground="#EA5555")
        self.boton_eliminar.grid(row=7, column=1, padx=10, pady=10)
        
    def editarDatos(self):
        try:
            selection = self.tabla.selection()
            item = self.tabla.item(selection[0])
            self.idCita=item["text"]
            self.nombre.set(item["values"][0])
            self.direccion.set(item["values"][1])
            self.productos.set(item["values"][2])
            
            self.habilitar_campos()
        except:
            titulo= "Conexion al Registro"
            mensaje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)
        
    def eliminarDatos(self):
        # Funcion que elimina la selección que se ha realizado en la tabla
        try:
            selection = self.tabla.selection()
            item = self.tabla.item(selection[0])
            self.idCita = item["text"]
            print(self.idCita)
            eliminar(int(self.idCita))
            self.tabla_citas()
            self.idCita=None
            self.deshabilitar_campos()
        except:
            titulo= "Gui"
            mensaje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)