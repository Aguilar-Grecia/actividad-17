import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Numero 1:")
etiqueta.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

etiqueta = tk.Label(ventana, text="Numero 2:")
etiqueta.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

def sumar():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        result = numero1 + numero2
        resultado.config(text=f"Resultado: {result}")
    except ValueError:
        resultado.config(text=f"Ingresa solo números")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.config(text="Resultado:")

boton_sumar = tk.Button(ventana, text="SUMAR", command=sumar)
boton_sumar.pack(pady=5)

botono_limpiar = tk.Button(ventana, text="LIMPIAR", command=limpiar)
botono_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="SALIR", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()