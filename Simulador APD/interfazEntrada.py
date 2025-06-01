import tkinter as tk
from tkinter import messagebox

def datosEntrada():
    resultado = {}

    #----------------------------- Funciones -----------------------------
    #Funcion para agregar transiciones
    def agregar_transicion():
        fila_widgets = []
        row = len(transiciones_entries) + 1  # +1 por encabezados
        # Creamos una nueva fila de entradas 
        for col in range(5):
            entry = tk.Entry(frame_transiciones, width=12)
            entry.grid(row=row, column=col, padx=5, pady=2)
            fila_widgets.append(entry)

        # Botón eliminar para eliminar transición
        btn_eliminar = tk.Button(frame_transiciones, text="Eliminar")
        btn_eliminar.grid(row=row, column=5, padx=5)
        fila_widgets.append(btn_eliminar)
        transiciones_entries.append(fila_widgets)
        btn_eliminar.config(command=lambda w=fila_widgets: eliminar_transicion(w))

    #Funcion para eliminar transiciones
    def eliminar_transicion(fila_widgets):
        # Quitamos los widgets de la fila
        for widget in fila_widgets:
            widget.grid_forget()
            widget.destroy()

        transiciones_entries.remove(fila_widgets)

        # Reorganizamos las filas restantes para que tengan filas contiguas
        for idx, widgets in enumerate(transiciones_entries, start=1):
            for col_idx, widget in enumerate(widgets):
                widget.grid(row=idx, column=col_idx)

            # Actualizamos el botón eliminar para que apunte al widget correcto
            btn = widgets[-1]  # último widget es botón eliminar
            btn.config(command=lambda w=widgets: eliminar_transicion(w))

    # Actualizar opciones de aceptación 
    def actualizar_opciones(*args):
        if acepta_por_var.get() == "estado_final":
            entry_estados_finales.config(state="normal")
        else:
            entry_estados_finales.config(state="disabled")

    # Enviar datos y cerrar ventana
    def enviar_datos():
        transiciones = []
        for fila in transiciones_entries:
            valores = [campo.get().strip() for campo in fila[:5]]  
            if not valores[0] or not valores[3]:
                messagebox.showerror("Error", "Las transiciones deben incluir al menos estado y nuevo estado.")
                return
            transiciones.append(tuple(valores))

        estado_inicial = entry_estado_inicial.get().strip()
        acepta_por = acepta_por_var.get()

        if acepta_por == "estado_final":
            estados_finales = set(entry_estados_finales.get().strip().split(","))
        else:
            estados_finales = set()

        palabra = list(entry_palabra.get().strip())

        if not estado_inicial or not acepta_por or (acepta_por == "estado_final" and not estados_finales):
            messagebox.showerror("Error", "Faltan datos obligatorios.")
            return

        resultado['transiciones'] = transiciones
        resultado['estado_inicial'] = estado_inicial
        resultado['acepta_por'] = acepta_por
        resultado['estados_finales'] = estados_finales
        resultado['palabra'] = palabra

        ventana.destroy()


    #----------------------------- Interfaz -----------------------------
    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Ingreso de Datos")
    ventana.geometry("700x650")

    # --- Transiciones ---
    tk.Label(ventana, text="R es el símbolo inicial de la pila\nPara representar ε el espacio se deja en blanco").pack()

    frame_transiciones = tk.Frame(ventana)
    frame_transiciones.pack()

    # Encabezados
    encabezados = ["Estado", "Símb. Entrada", "Tope Pila", "Nuevo Estado", "Apilar", ""]
    for i, encabezado in enumerate(encabezados):
        label = tk.Label(frame_transiciones, text=encabezado, font=("Arial", 10, "bold"))
        label.grid(row=0, column=i, padx=5, pady=5)

    transiciones_entries = []
    agregar_transicion()

    btn_add_trans = tk.Button(ventana, text="Añadir transición", command=agregar_transicion)
    btn_add_trans.pack(pady=5)

    # --- Otros campos ---
    tk.Label(ventana, text="Estado inicial:").pack()
    entry_estado_inicial = tk.Entry(ventana)
    entry_estado_inicial.pack()

    tk.Label(ventana, text="¿Acepta por?").pack()
    acepta_por_var = tk.StringVar(value="estado_final")
    acepta_por_menu = tk.OptionMenu(ventana, acepta_por_var, "estado_final", "pila_vacia", command=actualizar_opciones)
    acepta_por_menu.pack()

    tk.Label(ventana, text="Estados finales (separados por comas):").pack()
    entry_estados_finales = tk.Entry(ventana)
    entry_estados_finales.pack()

    tk.Label(ventana, text="Palabra a evaluar:").pack()
    entry_palabra = tk.Entry(ventana)
    entry_palabra.pack()

    # --- Enviar ---
    btn_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
    btn_enviar.pack(pady=15)

    ventana.mainloop()

    if resultado:
        return (resultado['transiciones'], resultado['estado_inicial'], resultado['acepta_por'],
                resultado['estados_finales'], resultado['palabra'])
