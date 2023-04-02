import tkinter as tk
from tkinter import messagebox, scrolledtext
import base64

root = tk.Tk()
root.title("Cryptonize")
root.geometry("400x600")
root.config(bg="#121212")

label = tk.Label(root, text="Entrez le texte à encoder ou décoder", fg="#ffffff", bg="#121212", font=("Arial", 14))
label.pack(pady=20)

text_area = scrolledtext.ScrolledText(root, width=40, height=10, font=("Arial", 12), bg="#262626", fg="#ffffff")
text_area.pack(padx=20, pady=10)

def encode_text():
    input_text = text_area.get("1.0", "end-1c")
    encoded_text = base64.b64encode(input_text.encode()).decode()
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, encoded_text)

def decode_text():
    input_text = text_area.get("1.0", "end-1c")
    try:
        decoded_text = base64.b64decode(input_text.encode()).decode()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, decoded_text)
    except Exception as e:
        messagebox.showerror("Erreur", "Le texte fourni n'est pas encodé en base64.")

encode_button = tk.Button(root, text="Encoder", fg="#ffffff", bg="#262626", font=("Arial", 12), command=encode_text)
encode_button.pack(pady=10)

decode_button = tk.Button(root, text="Décoder", fg="#ffffff", bg="#262626", font=("Arial", 12), command=decode_text)
decode_button.pack(pady=10)

root.mainloop()
