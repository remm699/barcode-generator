#!/usr/bin/env python3
"""
Barcode Generator Tool
Generates 12-digit barcodes (EAN/UPC style) with a simple GUI interface.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk
import io
import os

class BarcodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Codes Barres 12 chiffres")
        self.root.geometry("500x400")
        self.root.resizable(True, True)
        
        # Variables
        self.barcode_image = None
        self.barcode_photo = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Générateur de Codes Barres EAN-13", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Input section
        ttk.Label(main_frame, text="Entrez 12 chiffres:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.digits_var = tk.StringVar()
        self.digits_entry = ttk.Entry(main_frame, textvariable=self.digits_var, width=20, font=("Arial", 12))
        self.digits_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.digits_entry.focus()
        
        # Bind Enter key to generate
        self.digits_entry.bind('<Return>', lambda e: self.generate_barcode())
        
        # Generate button
        self.generate_btn = ttk.Button(main_frame, text="Générer le code barre", 
                                      command=self.generate_barcode)
        self.generate_btn.grid(row=1, column=2, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_var.set("Prêt à générer un code barre")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, 
                                foreground="blue")
        status_label.grid(row=2, column=0, columnspan=3, pady=(10, 5))
        
        # Image display frame
        image_frame = ttk.LabelFrame(main_frame, text="Aperçu du code barre", padding="10")
        image_frame.grid(row=3, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        image_frame.columnconfigure(0, weight=1)
        image_frame.rowconfigure(0, weight=1)
        
        # Canvas for barcode display
        self.canvas = tk.Canvas(image_frame, width=300, height=100, bg="white", relief="sunken", bd=2)
        self.canvas.grid(row=0, column=0, pady=10)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Save button
        self.save_btn = ttk.Button(buttons_frame, text="Enregistrer l'image", 
                                  command=self.save_barcode, state="disabled")
        self.save_btn.grid(row=0, column=0, padx=5)
        
        # Clear button
        clear_btn = ttk.Button(buttons_frame, text="Effacer", command=self.clear_all)
        clear_btn.grid(row=0, column=1, padx=5)
        
        # Configure grid weights for resizing
        main_frame.rowconfigure(3, weight=1)
        
    def validate_input(self):
        """Validate that input is exactly 12 digits"""
        digits = self.digits_var.get().strip()
        
        if not digits:
            messagebox.showerror("Erreur", "Veuillez entrer 12 chiffres")
            return None
           
        if not digits.isdigit():
            messagebox.showerror("Erreur", "Veuillez entrer uniquement des chiffres")
            return None
           
        if len(digits) != 12:
            messagebox.showerror("Erreur", f"Veuillez entrer exactement 12 chiffres (actuellement: {len(digits)})")
            return None
           
        return digits
    
    def generate_barcode(self):
        """Generate barcode from input digits"""
        digits = self.validate_input()
        if not digits:
            return
            
        try:
            # Update status
            self.status_var.set("Génération du code barre en cours...")
            self.root.update()
            
            # Disable button during generation
            self.generate_btn.config(state="disabled")
            
            # Generate barcode using EAN13 (which uses 12 digits + calculates checksum)
            # We'll use the first 12 digits and let the library calculate the 13th (checksum)
            code12 = digits[:12]  # Ensure we only use first 12 digits
            
            # Create EAN13 barcode object
            ean = barcode.get('ean13', code12, writer=ImageWriter())
            
            # Generate barcode image in memory
            buffer = io.BytesIO()
            ean.write(buffer)
            buffer.seek(0)
            
            # Open with PIL
            pil_image = Image.open(buffer)
            
            # Resize for display (maintain aspect ratio)
            display_width = 300
            w_percent = (display_width / float(pil_image.size[0]))
            h_size = int((float(pil_image.size[1]) * float(w_percent)))
            display_image = pil_image.resize((display_width, h_size), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage for tkinter
            self.barcode_photo = ImageTk.PhotoImage(display_image)
            self.barcode_image = pil_image  # Keep original for saving
            
            # Display on canvas
            self.canvas.delete("all")
            self.canvas.create_image(display_width//2, h_size//2, image=self.barcode_photo)
            
            # Update status
            self.status_var.set(f"Code barre généré! (Code complet: {ean})")
            self.save_btn.config(state="normal")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la génération du code barre:\n{str(e)}")
            self.status_var.set("Erreur lors de la génération")
        finally:
            self.generate_btn.config(state="normal")
    
    def save_barcode(self):
        """Save the barcode image to file"""
        if not self.barcode_image:
            messagebox.showwarning("Attention", "Aucun code barre à enregistrer")
            return
            
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
                title="Enregistrer le code barre"
            )
            
            if file_path:
                self.barcode_image.save(file_path)
                messagebox.showinfo("Succès", f"Code barre enregistré avec succès:\n{file_path}")
                self.status_var.set(f"Code barre enregistré: {os.path.basename(file_path)}")
                
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement:\n{str(e)}")
    
    def clear_all(self):
        """Clear all fields and reset"""
        self.digits_var.set("")
        self.canvas.delete("all")
        self.barcode_image = None
        self.barcode_photo = None
        self.status_var.set("Prêt à générer un code barre")
        self.save_btn.config(state="disabled")
        self.digits_entry.focus()

def main():
    root = tk.Tk()
    app = BarcodeGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()