import tkinter as tk
from tkinter import font

def calcolatrice(operazione):
    num1 = float(entry1.get()) 
    num2 = float(entry2.get())
    
    risultato = ""
        
    if operazione == '+':
        risultato = f"{num1} + {num2} = {num1 + num2}"

    elif operazione == '-':
        risultato = f"{num1} - {num2} = {num1 - num2}"

    elif operazione == '*': 
        risultato = f"{num1} * {num2} = {num1 * num2}"

    elif operazione == '/':
        if (num2 != 0):
            risultato = f"{num1} / {num2} = {num1 / num2}"
        else:
            risultato = "Errore: divisione per zero non consentita."
        
    # Aggiornare la label con il risultato
    label_risultato.config(text="Risultato: " + risultato)

def resetta_campi():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_risultato.config(text="Risultato: ")
 
# Creazione della finestra principale 
window = tk.Tk() 
window.title("Calcolatrice Semplice") 
window.geometry("500x350") 
window.config(bg="#f0f0f0")  # Colore di sfondo

# Font personalizzato
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Casella di testo per il primo numero 
entry1 = tk.Entry(window, width=15, font=custom_font, bd=2, relief="groove") 
entry1.pack(pady=10) 

# Casella di testo per il secondo numero 
entry2 = tk.Entry(window, width=15, font=custom_font, bd=2, relief="groove") 
entry2.pack(pady=10) 

# Frame per contenere i pulsanti
frame_pulsanti = tk.Frame(window, bg="#f0f0f0")
frame_pulsanti.pack(pady=10)

# Stile per i pulsanti
button_style = {
    "font": custom_font, "bg": "#4caf50", "fg": "white", 
    "activebackground": "#45a049", "bd": 2, "relief": "raised",
    "width": 3, "height": 1
}

# Pulsanti per le operazioni
button_somma = tk.Button(frame_pulsanti, text="+", command=lambda: calcolatrice('+'), **button_style) 
button_somma.pack(side=tk.LEFT, padx=5)

button_sottrazione = tk.Button(frame_pulsanti, text="-", command=lambda: calcolatrice('-'), **button_style) 
button_sottrazione.pack(side=tk.LEFT, padx=5)

button_prodotto = tk.Button(frame_pulsanti, text="*", command=lambda: calcolatrice('*'), **button_style) 
button_prodotto.pack(side=tk.LEFT, padx=5)

button_divisione = tk.Button(frame_pulsanti, text="/", command=lambda: calcolatrice('/'), **button_style) 
button_divisione.pack(side=tk.LEFT, padx=5)

# Pulsante per resettare i campi di input
button_reset = tk.Button(window, text="Reset", command=resetta_campi, font=custom_font, bg="#f44336", fg="white", activebackground="#d32f2f", bd=2, relief="raised", width=9, height=1)
button_reset.pack(pady=10)

# Etichetta per mostrare il risultato 
label_risultato = tk.Label(window, text="Risultato: ", font=custom_font, bg="#f0f0f0") 
label_risultato.pack(pady=10)

if __name__ == "__main__":
    window.mainloop()