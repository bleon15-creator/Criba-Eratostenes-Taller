import tkinter as tk
from tkinter import messagebox, Entry, Button, Label

class CribaEratostenes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Criba de Eratóstenes - Areadina")
        self.root.geometry("800x700")
        self.root.configure(bg='white')
        
        self.botones = {}
        self.colores_usados = set()
        self.numeros_ya_coloreados = set()
        
        self.colores = {
            1: '#0066CC',      # Azul para el 1
            2: '#FF0000',      # Rojo para el 2
            3: '#FF8C00',      # Naranaja para el 3
            5: '#FFFF00',      # Amarillo para el 5
            7: '#00FF00'       # Verde el 7
        }
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        titulo = tk.Label(self.root, text="CRIBA DE ERATÓSTENES - AREANDINA", 
                      font=('Arial', 16, 'bold'), bg='white', fg='black')
        titulo.pack(pady=10)
        
        frame_controles = tk.Frame(self.root, bg='white')
        frame_controles.pack(pady=10)
        
        tk.Label(frame_controles, text="Escriba un número 2, 3, 5, o 7", 
              font=('Arial', 12), bg='white').pack(side='left', padx=5)
        
        self.entrada = tk.Entry(frame_controles, font=('Arial', 12), width=10)
        self.entrada.pack(side='left', padx=5)
        
        self.btn_procesar = tk.Button(frame_controles, text="Colorear", 
                                  command=self.procesar_numero,
                                  font=('Arial', 12), bg='#4CAF50', fg='white')
        self.btn_procesar.pack(side='left', padx=5)
        
        self.btn_reiniciar = tk.Button(frame_controles, text="Reiniciar", 
                                     command=self.reiniciar,
                                     font=('Arial', 12), bg='#f44336', fg='white')
        self.btn_reiniciar.pack(side='left', padx=5)
        
        frame_cuadricula = tk.Frame(self.root, bg='white')
        frame_cuadricula.pack(pady=20)
        
        self.crear_cuadricula(frame_cuadricula)
        
        self.crear_leyenda()
        
        self.root.bind('<Return>', lambda event: self.procesar_numero())
    
    def crear_cuadricula(self, parent):
        for i in range(10):
            for j in range(10):
                numero = i * 10 + j + 1
                
                btn = tk.Button(parent, text=str(numero), 
                           width=4, height=2,
                           font=('Arial', 10, 'bold'),
                           bg='lightgray',
                           relief='raised',
                           borderwidth=1)
                
                btn.grid(row=i, column=j, padx=1, pady=1)
                self.botones[numero] = btn
                
        # COLOREAR EL 1 EN AZUL
        self.botones[1].configure(bg='#0066CC', fg='white')
        self.colores_usados.add(1)
        self.numeros_ya_coloreados.add(1)
    
    def crear_leyenda(self):
        frame_leyenda = tk.Frame(self.root, bg='white')
        frame_leyenda.pack(pady=10)
        
        tk.Label(frame_leyenda, text="LEYENDA:", font=('Arial', 12, 'bold'), 
              bg='white').pack()
        
        leyendas = [
            ("1", '#0066CC'),
            ("Multiplos de 2", '#FF0000'),
            ("Multiplos de 3", '#FF8C00'),
            ("Multiplos de 5", '#FFFF00'),
            ("Multiplos de 7", '#00FF00'),
            ("Números primos", 'lightgray')
        ]
        
        frame_colores = tk.Frame(frame_leyenda, bg='white')
        frame_colores.pack()
        
        for texto, color in leyendas:
            frame_item = tk.Frame(frame_colores, bg='white')
            frame_item.pack(side='left', padx=10)
            
            cuadro = tk.Label(frame_item, text="  ", bg=color, 
                          width=3, relief='solid', borderwidth=1)
            cuadro.pack(side='left')
            
            tk.Label(frame_item, text=texto, font=('Arial', 9), 
                  bg='white').pack(side='left', padx=2)
    
    def procesar_numero(self):
        try:
            numero = int(self.entrada.get())
            
            if numero not in [2, 3, 5, 7]:
                tk.messagebox.showwarning("Número no válido", 
                                     "Solo puedes ingresar 2, 3, 5, o 7")
                return
            
            if numero in self.colores_usados:
                tk.messagebox.showinfo("Ya procesado Coloreado", 
                                  f"El número {numero} ya fue Coloreado")
                return
            
            self.marcar_multiplos(numero)
            self.colores_usados.add(numero)
            
            self.entrada.delete(0, tk.END)
            
            tk.messagebox.showinfo("Coloreado", 
                                  f"Múltiplos de {numero} coloreados")
            
        except ValueError:
            tk.messagebox.showerror("Error", "no es un numero valido")
    
    def marcar_multiplos(self, numero):
        color = self.colores[numero]
        
        for i in range(numero * 2, 101, numero):  
            if i not in self.numeros_ya_coloreados:
                self.botones[i].configure(bg=color, fg='white')
                self.numeros_ya_coloreados.add(i)
                    
    def reiniciar(self):
        for numero in range(1, 101):
            self.botones[numero].configure(bg='lightgray', fg='black')
        
        self.botones[1].configure(bg='#0066CC', fg='white')
        
        self.colores_usados.clear()
        self.numeros_ya_coloreados.clear()
        self.colores_usados.add(1)
        self.numeros_ya_coloreados.add(1)
        
        self.entrada.delete(0, tk.END)
        
        tk.messagebox.showinfo("Limpiada", "La criba ha sido reiniciada")
    
    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CribaEratostenes()
    app.ejecutar()
