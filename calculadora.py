import tkinter as tk
from tkinter import messagebox

var = 0
# Funciones
# Suma
def sumar():
    global var
    try:
        num = float(entrada.get())
        var += num
        resultado.config(text=f"{var}")
    except:
       messagebox.showerror("Error", "Dato inválido")

# Resta
def restar():
    global var
    try:
        num = float(entrada.get())
        var -= num
        resultado.config(text=f"{var}")
    except:
        messagebox.showerror("Error", "Dato inválido")

#Multiplicar
def multiplicar():
    global var
    try:
        num = float(entrada.get())
        if var == 0:
            var = num
        else:
            var *= num
        resultado.config(text=f"{var}")
    except:
        messagebox.showerror("Error", "Dato inválido")
    
# Division
def dividir():
    global var
    try:
        num = float(entrada.get())
        if var == 0:
            var = num
        else:
            var /= num
        resultado.config(text=f"{var}")
    except:
         messagebox.showerror("Error", "Dato inválido")
        
        
# Porcentaje
def porcentaje():
    global var
    try:
        num = float(entrada.get())
        var = num / 100
        resultado.config(text=f"{var}")
    except:
        messagebox.showerror("Error", "Dato inválido")
    
# Borrar todos los datos
def borrartodo():
    global var
    var = 0
    resultado.config(text="")
    entrada.delete(0, tk.END)
    
# Borrar datos del labal resultado y entrada
def delate():    
    entrada.delete(0, tk.END)       

# Calcular
def calcular():
    try:
        resultado_final = eval(entrada.get())
        resultado.config(text=f"{resultado_final}")
    except:
        messagebox.showerror("Error", "Dato inválido")


# Crear ventana
ventana = tk.Tk()
ventana.geometry("350x400")
ventana.title("Calculadora colorida")

# Aviso "Ingrese valor"
aviso = tk.Label(ventana, text="Ingrese valor", font=("Arial", 10))
aviso.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Entry para ingresar número
entrada = tk.Entry(ventana, width=20, font=("Arial", 12), bg="#e0f7fa")
entrada.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Label para mostrar el resultado
resultado = tk.Label(ventana, text="", width=20, height=2, relief="sunken", anchor="e", bg="#fff9c4", font=("Arial", 12))
resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Botones de operaciones
suma = tk.Button(ventana, text="+", width=5, height=2, bg="#aed581", font=("Arial", 12), command=sumar)
suma.grid(row=3, column=0, padx=5, pady=5)

resta = tk.Button(ventana, text="-", width=5, height=2, bg="#aed581", font=("Arial", 12), command=restar)
resta.grid(row=3, column=1, padx=5, pady=5)

mult = tk.Button(ventana, text="x", width=5, height=2, bg="#81d4fa", font=("Arial", 12), command=multiplicar)
mult.grid(row=4, column=0, padx=5, pady=5)

division = tk.Button(ventana, text="/", width=5, height=2, bg="#81d4fa", font=("Arial", 12), command=dividir)
division.grid(row=4, column=1, padx=5, pady=5)

igual = tk.Button(ventana, text="%", width=5, height=2, bg="#ffb74d", font=("Arial", 12), command=porcentaje)
igual.grid(row=5, column=0, padx=5, pady=5)

borrar = tk.Button(ventana, text="C", width=5, height=2, bg="#e57373", font=("Arial", 12), command=borrartodo)
borrar.grid(row=5, column=1, padx=5, pady=5)

borrar_entrada = tk.Button(ventana, text="E", width=5, height=2, bg="green", font=("Arial", 12), command=delate)
borrar_entrada.grid(row=5, column=2, padx=5, pady=5)

#igual = tk.Button(ventana, text="=", width=5, height=2, bg="green", font=("Arial", 12), command=calcular)
#igual.grid(row=5, column=2, padx=5, pady=5)

ventana.mainloop()
