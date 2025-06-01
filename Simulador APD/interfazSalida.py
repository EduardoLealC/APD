import tkinter as tk
from tkinter import simpledialog

def mostrarResultado(palabra, aceptada, transiciones):
    resultado = {'nueva_palabra': None}

    def preguntar_otra_palabra():
        # Crear un campo de entrada para la nueva palabra
        entrada_label = tk.Label(ventana, text="Ingrese otra palabra:")
        entrada_label.pack(pady=(20, 0))

        entrada = tk.Entry(ventana)
        entrada.pack()

        def confirmar():
            resultado['nueva_palabra'] = entrada.get()
            ventana.destroy()

        boton_confirmar = tk.Button(ventana, text="Confirmar", command=confirmar)
        boton_confirmar.pack(pady=10)

        # Deshabilitar el botón de nueva palabra para evitar múltiples entradas
        boton_otra_palabra.config(state=tk.DISABLED)

    ventana = tk.Tk()
    ventana.title("Resultado de la Evaluación")
    ventana.geometry("500x500")

    estado_msg = "Aceptada" if aceptada else "Rechazada"
    texto = f"La palabra '{''.join(palabra)}' es {estado_msg}"
    label_msg = tk.Label(ventana, text=texto, font=("Arial", 14, "bold"))
    label_msg.pack(pady=10)

    # Mostrar transiciones
    frame_trans = tk.Frame(ventana)
    frame_trans.pack(pady=10)

    tk.Label(frame_trans, text="Transiciones:", font=("Arial", 12, "underline")).pack()

    for t in transiciones:
        simbolo_entrada = t[1] if t[1] != "" else 'ε'
        tope_pila = t[2] if t[2] != "" else 'ε'
        nuevo_estado = t[3]
        apilar = t[4] if t[4] != "" else 'ε'

        left = f"({t[0]}, {simbolo_entrada}, {tope_pila})"
        right = f"({nuevo_estado}, {apilar})"
        texto_t = f"{left} = {right}"
        label = tk.Label(frame_trans, text=texto_t, font=("Consolas", 11))
        label.pack(anchor="w")

    # Botón para preguntar si desea ingresar otra palabra
    boton_otra_palabra = tk.Button(ventana, text="¿Desea probar otra palabra?", command=preguntar_otra_palabra)
    boton_otra_palabra.pack(pady=20)

    ventana.mainloop()

    return resultado['nueva_palabra']
