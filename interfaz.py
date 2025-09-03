import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="CALCULADORA", font=("Arial", 22, "bold"), fg="red")
etiqueta.pack(pady=5)

etiqueta = tk.Label(ventana, text="Ingresa el primer número:", fg="blue" )
etiqueta.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

etiqueta = tk.Label(ventana, text="Ingresa el segundo número:", fg="blue")
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
        resultado.config(text=f"Resultado: {result}", font=("Arial", 9, "bold"), fg="red")
    except ValueError:
        resultado.config(text=f"Ingresa solo numeros.")

def restar():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        result = numero1 - numero2
        resultado.config(text=f"Resultado: {result}")
    except ValueError:
        resultado.config(text=f"Ingresa solo numeros.")

def multiplicar():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        result = numero1 * numero2
        resultado.config(text=f"Resultado: {result}")
    except ValueError:
        resultado.config(text=f"Ingresa solo numeros.")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.config(text="Resultado:")

boton_sumar = tk.Button(ventana, text="SUMAR", command=sumar, activeforeground="Yellow", activebackground="Red")
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="RESTAR", command=restar)
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="MULTIPLICAR", command=multiplicar)
boton_multiplicar.pack(pady=5)

botono_limpiar = tk.Button(ventana, text="LIMPIAR", command=limpiar)
botono_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="SALIR", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()