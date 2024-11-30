import tkinter as tk # disegnare finestre di sistema (GUI)

def calcolatrice():
    num1 = float(entry1.get()) 
    num2 = float(entry2.get())
    operazione = (operatore.get())
    
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
    else:
        risultato = "Operazione non valida."
        
    # Aggiornare la label con il risultato
    label_risultato.config(text="Risultato: " + risultato)

 
# Creazione della window principale 
window = tk.Tk() 
window.title("Calcolatrice Semplice") 
window.geometry("500x350") 
 
# Casella di testo per il primo numero 
entry1 = tk.Entry(window, width=15) 
entry1.pack(pady=5) 

# Casella di testo per il secondo numero 
entry2 = tk.Entry(window, width=15) 
entry2.pack(pady=5) 

# Casella di testo per l'operatore 
operatore = tk.Entry(window, width=15) 
operatore.pack(pady=5) 

# Bottone per eseguire l'operazione
button_calcola = tk.Button(window, text="Calcola", command=calcolatrice) 
button_calcola.pack(pady=10) 


# Etichetta per mostrare il risultato 
label_risultato = tk.Label(window, text="Risultato: ") 
label_risultato.pack(pady=10)


if __name__ == "__main__":
    window.mainloop()