import customtkinter as ctk
from tkinter import messagebox
def caesar_cipher(text, shift, mode):
    
    if mode == 'decrypt':
        shift = -shift
    result = ''
    for char in text:
        if char.isalpha():
            char_code = ord(char)
            base = ord('A') if char.isupper() else ord('a')
            new_char_code = (char_code - base + shift + 26) % 26 + base
            result += chr(new_char_code)
        else:
            result += char
    return result

# --- Impostazioni dell'App ---
ctk.set_appearance_mode("dark")  # Imposta il tema scuro (può essere "light" o "system")
ctk.set_default_color_theme("blue") # Imposta il colore "accent"

class CaesarApp(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        # --- Configurazione della finestra ---
        self.title("Cifrario di Cesare (CustomTkinter)")
        self.geometry("500x600")
        self.resizable(False, False)
        
        # Configura la griglia principale per centrare il contenuto
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Frame Principale ---
        # Usiamo un frame con angoli arrotondati
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.grid(row=0, column=0, padx=25, pady=25, sticky="nsew") # MODIFICA: padding
        
        # Configura la griglia interna del frame
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1) # L'area di input cresce
        main_frame.grid_rowconfigure(5, weight=1) # L'area di output cresce

        # --- Creazione dei Widget ---
        
        # 1. Titolo
        title_label = ctk.CTkLabel(
            main_frame, 
            text="Cifrario di Cesare",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 25)) # MODIFICA: padding

        # 2. Area di Input
        input_label = ctk.CTkLabel(main_frame, text="Testo (input):", font=ctk.CTkFont(size=14))
        input_label.grid(row=1, column=0, columnspan=2, padx=25, pady=(10, 5), sticky="w") # MODIFICA: padding
        
        self.input_text = ctk.CTkTextbox(
            main_frame,
            height=120,
            border_width=2,
            corner_radius=10
        )
        self.input_text.grid(row=2, column=0, columnspan=2, padx=25, pady=5, sticky="nsew") # MODIFICA: padding

        # 3. Controlli (Spostamento e Pulsanti)
        controls_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        controls_frame.grid(row=3, column=0, columnspan=2, padx=25, pady=20, sticky="ew") # MODIFICA: padding
        controls_frame.grid_columnconfigure(1, weight=1) # Lo slider si espande

        # MODIFICA: Salvato come self.shift_label per un reset sicuro
        self.shift_label = ctk.CTkLabel(controls_frame, text="Spostamento: 3")
        self.shift_label.grid(row=0, column=0, padx=(0, 10))

        # Slider per lo spostamento
        def update_shift_label(value):
            # MODIFICA: Riferimento a self.shift_label
            self.shift_label.configure(text=f"Spostamento: {int(value)}")
        
        self.shift_slider = ctk.CTkSlider(
            controls_frame,
            from_=1,
            to=25,
            number_of_steps=24,
            command=update_shift_label
        )
        self.shift_slider.set(3) # Valore di default
        self.shift_slider.grid(row=0, column=1, padx=10, sticky="ew")

        # 4. Pulsanti Cifra/Decifra
        encrypt_btn = ctk.CTkButton(
            main_frame,
            text="Cifra",
            command=self.handle_encrypt,
            font=ctk.CTkFont(weight="bold")
        )
        encrypt_btn.grid(row=4, column=0, padx=(25, 10), pady=5, sticky="ew") # MODIFICA: padding
        
        decrypt_btn = ctk.CTkButton(
            main_frame,
            text="Decifra",
            command=self.handle_decrypt,
            fg_color="gray50", # Colore diverso
            hover_color="gray30",
            font=ctk.CTkFont(weight="bold") # MODIFICA: font
        )
        decrypt_btn.grid(row=4, column=1, padx=(10, 25), pady=5, sticky="ew") # MODIFICA: padding

        # 5. Area di Output
        output_label = ctk.CTkLabel(main_frame, text="Risultato (output):", font=ctk.CTkFont(size=14))
        output_label.grid(row=5, column=0, columnspan=2, padx=25, pady=(20, 5), sticky="w") # MODIFICA: padding
        
        self.output_text = ctk.CTkTextbox(
            main_frame,
            height=120,
            border_width=2,
            corner_radius=10,
            state="disabled" # Inizia disabilitato
        )
        self.output_text.grid(row=6, column=0, columnspan=2, padx=25, pady=5, sticky="nsew") # MODIFICA: padding
        
        # 6. Pulsanti Utility (Copia/Resetta)
        copy_btn = ctk.CTkButton(
            main_frame,
            text="Copia Risultato",
            command=self.handle_copy,
            fg_color="#008000", # MODIFICA: Colore verde
            hover_color="#006400", # MODIFICA: Hover verde scuro
            font=ctk.CTkFont(weight="bold") # MODIFICA: font
        )
        copy_btn.grid(row=7, column=0, padx=(25, 10), pady=(20, 25), sticky="ew") # MODIFICA: padding
        
        reset_btn = ctk.CTkButton(
            main_frame,
            text="Resetta",
            command=self.handle_reset,
            fg_color="#B22222", # MODIFICA: Colore rosso (Firebrick)
            hover_color="#8B0000", # MODIFICA: Hover rosso scuro
            font=ctk.CTkFont(weight="bold") # MODIFICA: font
        )
        reset_btn.grid(row=7, column=1, padx=(10, 25), pady=(20, 25), sticky="ew") # MODIFICA: padding

    # --- Funzioni Handler ---
    
    def handle_encrypt(self):
        try:
            text = self.input_text.get("1.0", "end-1c")
            shift = int(self.shift_slider.get())
            result = caesar_cipher(text, shift, 'encrypt')
            
            self.output_text.configure(state="normal") # Abilita scrittura
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.output_text.configure(state="disabled") # Disabilita scrittura
            
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

    def handle_decrypt(self):
        try:
            text = self.input_text.get("1.0", "end-1c")
            shift = int(self.shift_slider.get())
            result = caesar_cipher(text, shift, 'decrypt')
            
            self.output_text.configure(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.output_text.configure(state="disabled")
            
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

    def handle_copy(self):
        text_to_copy = self.output_text.get("1.0", "end-1c")
        if text_to_copy:
            self.clipboard_clear()
            self.clipboard_append(text_to_copy)
            messagebox.showinfo("Copiato", "Testo copiato negli appunti!")
        else:
            messagebox.showwarning("Attenzione", "Nessun risultato da copiare.")
            
    def handle_reset(self):
        self.input_text.delete("1.0", "end")
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")
        self.shift_slider.set(3)
        # MODIFICA: Modo più sicuro e pulito per resettare l'etichetta
        self.shift_label.configure(text="Spostamento: 3")


# --- Avvio dell'applicazione ---
if __name__ == "__main__":
    app = CaesarApp()
    app.mainloop()

