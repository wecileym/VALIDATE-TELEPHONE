from tkinter import messagebox
import re
import tkinter as tk
import customtkinter as ctk




class Logon(ctk.CTk): 

    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.geometry("800x600")
        self.minsize(800, 600)
        self.title('Login')
        
        self.phone = ctk.CTkEntry(self, width=480, height=50, font=('Century Gothic', 20,'bold'))
        self.phone.pack(pady=5, padx=10)
        self.phone.bind("<FocusOut>", lambda event: self.validate_phone(event, self.phone))

        self.anything = ctk.CTkEntry(self, width=480, height=50, font=('Century Gothic', 20,'bold'))
        self.anything.pack(pady=5, padx=10)

    def validate_phone(self, event, Entry):
            phone = Entry.get()
            if not self.is_valid_phone(phone):
                messagebox.showerror("Erro de entrada", "Por favor, insira um número de celular válido.")
                Entry.delete(0, tk.END)
                return
            formatted_phone = self.format_phone(phone)
            Entry.delete(0, tk.END)
            Entry.insert(0, formatted_phone)

    def is_valid_phone(self, phone):
        # Permite dígitos, parênteses, espaço e hífen
        phone_digits = re.sub(r'\D', '', phone)  # Remove caracteres não numéricos
        return len(phone_digits) == 11

    def format_phone(self, phone):
        phone_digits = re.sub(r'\D', '', phone)  # Remove caracteres não numéricos
        if len(phone_digits) != 11:
            return phone  # Retorna o original se não houver 11 dígitos
        return f"({phone_digits[:2]}) {phone_digits[2:7]}-{phone_digits[7:]}"



if __name__ == "__main__":
    logon = Logon()
    logon.mainloop()
