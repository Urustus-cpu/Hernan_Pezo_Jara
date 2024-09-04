import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from comprobador import *
from funciones import *
from datetime import *

def nuevo_envio():
    def guardar_envio():

        origen = comprobador_str(entry_origen)
        destino = comprobador_str(entry_destino)
        FechaEntregaPrevista = validaDatetime(entry_fecha)

        if origen != None and destino != None and FechaEntregaPrevista != None:
            Estado = "En tránsito"
            mensaje = agregar_envio(origen, destino, FechaEntregaPrevista, Estado)
            messagebox.showinfo("Información", mensaje)
            ventana_nuevo_envio.destroy()

    ventana_nuevo_envio = tk.Toplevel()
    ventana_nuevo_envio.title("Nuevo Envío")
    ventana_nuevo_envio.geometry("250x300")

    tk.Label(ventana_nuevo_envio, text="Numero de seguimiento se generara de manera\nautomatica despues de ingresar los datos").pack(pady=2)
    lbl_origen = tk.Label(ventana_nuevo_envio, text="Origen:")
    lbl_origen.pack(pady=5)
    entry_origen = tk.Entry(ventana_nuevo_envio)
    entry_origen.pack(pady=5)

    lbl_destino = tk.Label(ventana_nuevo_envio, text="Destino:")
    lbl_destino.pack(pady=5)
    entry_destino = tk.Entry(ventana_nuevo_envio)
    entry_destino.pack(pady=5)

    lbl_fecha = tk.Label(ventana_nuevo_envio, text="Fecha Prevista de entrega (YYYY-MM-DD):")
    lbl_fecha.pack(pady=5)
    entry_fecha = tk.Entry(ventana_nuevo_envio)
    entry_fecha.pack(pady=5)

    tk.Button(ventana_nuevo_envio, text="Guardar", command=guardar_envio).pack(pady=5)

def modificar_estado():
    def guardar_cambio_estado():
        seguimiento = comprobador_int(entry_numero)
        Estado = comprobador_str(entry_estado)

        if seguimiento != None and Estado != None:
            mensaje = modificar_envio(seguimiento, Estado)
            messagebox.showinfo("Información", mensaje)
            ventana_modificar_estado.destroy()

    ventana_modificar_estado = tk.Toplevel()
    ventana_modificar_estado.title("Modificar Estado")
    ventana_modificar_estado.geometry("250x300")

    lbl_numero = tk.Label(ventana_modificar_estado, text="Número de seguimiento:")
    lbl_numero.pack(pady=5)
    entry_numero = tk.Entry(ventana_modificar_estado)
    entry_numero.pack(pady=5)

    lbl_estado = tk.Label(ventana_modificar_estado, text="Nuevo Estado:")
    lbl_estado.pack(pady=5)
    entry_estado = tk.Entry(ventana_modificar_estado)
    entry_estado.pack(pady=5)

    tk.Button(ventana_modificar_estado, text="Guardar", command=guardar_cambio_estado).pack(pady=5)

def modificar_fecha():
    def guardar_cambio_fecha():
        seguimiento = comprobador_int(entry_numero)
        fecha = validaDatetime(entry_fecha)

        if seguimiento != None and fecha != None:
            mensaje = cambioFecha(seguimiento, fecha)
            messagebox.showinfo("Información", mensaje)
            ventana_modificar_fecha.destroy()

    ventana_modificar_fecha = tk.Toplevel()
    ventana_modificar_fecha.title("Modificar Fecha de Entrega")
    ventana_modificar_fecha.geometry("250x300")
    
    lbl_numero = tk.Label(ventana_modificar_fecha, text="Número de seguimiento:")
    lbl_numero.pack(pady=5)
    entry_numero = tk.Entry(ventana_modificar_fecha)
    entry_numero.pack(pady=5)

    lbl_fecha = tk.Label(ventana_modificar_fecha, text="Nueva Fecha (YYYY-MM-DD):")
    lbl_fecha.pack(pady=5)
    entry_fecha = tk.Entry(ventana_modificar_fecha)
    entry_fecha.pack(pady=5)

    tk.Button(ventana_modificar_fecha, text="Guardar", command=guardar_cambio_fecha).pack(pady=5)

def eliminar_columna():
    def eliminar_columna_ventana():
        numero = comprobador_int(entry_eliminar)
        if numero != None:
            mensaje = eliminar(numero)
            messagebox.showinfo("informacion", mensaje)
            ventana_eliminar.destroy()

    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Envio")
    ventana_eliminar.geometry("200x200")
    
    lbl_eliminar = tk.Label(ventana_eliminar, text="Numero de seguimiento: ")
    lbl_eliminar.pack(pady=5)
    entry_eliminar = tk.Entry(ventana_eliminar)
    entry_eliminar.pack(pady=5)
    
    tk.Button(ventana_eliminar, text="Borrar", command=eliminar_columna_ventana).pack(pady=5)
       
def mostrar_envios():
    envios = lista()
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Envíos")

    tree = ttk.Treeview(ventana_lista, columns=("ID", "NumeroSeguimiento", "Origen", "Destino", "FechaEntregaPrevista", "Estado"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("NumeroSeguimiento", text="Número de Seguimiento")
    tree.heading("Origen", text="Origen")
    tree.heading("Destino", text="Destino")
    tree.heading("FechaEntregaPrevista", text="Fecha de Entrega Prevista")
    tree.heading("Estado", text="Estado")

    tree.column("ID", width=50, anchor='center')
    tree.column("NumeroSeguimiento", width=150, anchor='center')
    tree.column("Origen", width=100, anchor='center')
    tree.column("Destino", width=100, anchor='center')
    tree.column("FechaEntregaPrevista", width=150, anchor='center')
    tree.column("Estado", width=100, anchor='center')

    for envio in envios:
        tree.insert("", tk.END, values=envio)

    tree.pack(fill=tk.BOTH, expand=True)
    
def cierre_programa():
    cierre()
    roots.destroy()

roots = tk.Tk()
roots.title("Evaluacion Final")
roots.geometry("250x350")

envio_nuevo = tk.Button(roots, text="Nuevo Envio",command=nuevo_envio)
envio_nuevo.pack(pady=15)
cambiar_estado = tk.Button(roots, text="Notificar Estado", command=modificar_estado)
cambiar_estado.pack(pady=15)
fecha_actualizada = tk.Button(roots, text= "Modificar Fecha de Entrega", command=modificar_fecha)
fecha_actualizada.pack(pady=15)
eliminar_envio = tk.Button(roots, text="Eliminar Envio", command=eliminar_columna)
eliminar_envio.pack(pady=15)
lista_completa = tk.Button(roots, text="Listado de pedidos", command=mostrar_envios)
lista_completa.pack(pady=15)
fin = tk.Button(roots, text="cerrar programa", command=cierre_programa)
fin.pack(pady=15)


roots.mainloop()