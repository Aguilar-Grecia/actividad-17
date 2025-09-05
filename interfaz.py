import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("800x500")
ventana.configure(bg= "beige")

etiqueta = tk.Label(ventana, text="CALCULADORA", font=("Arial", 55, "bold"), fg="dark blue", bg= "beige")
etiqueta.pack(pady=5)

etiqueta = tk.Label(ventana, text="Ingresa el primer número:", font=("georgia", 12, "italic"), fg="purple", bg= "beige")
etiqueta.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

etiqueta = tk.Label(ventana, text="Ingresa el segundo número:", font=("georgia", 12, "italic"), fg="purple", bg= "beige")
etiqueta.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="Resultado:", font=("georgia", 13, "underline"), fg="red", bg= "beige" )
resultado.pack(pady=5)

def sumar():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        result = numero1 + numero2
        resultado.config(text=f"Resultado: {result}" )
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

boton_sumar = tk.Button(ventana, text="SUMAR", command=sumar, activeforeground="Yellow", activebackground="Red", bd ="5", bg = "gray")
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="RESTAR", command=restar, bd ="5", bg = "gray")
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="MULTIPLICAR", command=multiplicar, bd ="5", bg = "gray")
boton_multiplicar.pack(pady=5)

botono_limpiar = tk.Button(ventana, text="LIMPIAR", command=limpiar, bd ="5", bg = "gray")
botono_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="SALIR", command=ventana.quit, bd ="5", bg = "gray")
boton_salir.pack(pady=5)

ventana.mainloop()