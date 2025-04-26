import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import os

ZBAR_PATH = r"C:\Program Files (x86)\ZBar\bin\zbarimg.exe"

def select_qr_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="QR Kod Dosyasını Seçin",
        filetypes=[("PNG Dosyaları", "*.png"), ("Tüm Dosyalar", "*.*")]
    )
    root.destroy()
    return file_path

def extract_secret(file_path):
    try:
        result = subprocess.run(
            [ZBAR_PATH, "-q", "--raw", file_path],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.returncode != 0:
            return None
        
        uri = result.stdout.strip()
        return uri.split('secret=')[1].split('&')[0] if 'secret=' in uri else None
    
    except Exception as e:
        messagebox.showerror("Hata", f"Okuma hatası: {str(e)}")
        return None

def save_secret(secret):
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Metin Dosyaları", "*.txt")],
        title="Secret Kaydetme Konumu Seçin"
    )
    root.destroy()
    
    if save_path:
        with open(save_path, 'w') as f:
            f.write(secret)
        return save_path
    return None

def main():
    qr_path = select_qr_file()
    if not qr_path: 
        return
    
    secret = extract_secret(qr_path)
    if not secret:
        messagebox.showwarning("Uyarı", "Secret bulunamadı!")
        return
    
    print(f"\n══════════════════════════════\nTOTP Secret: {secret}\n══════════════════════════════\n")
    
    root = tk.Tk()
    root.withdraw()
    
    if messagebox.askyesno("Kayıt", "Secret'ı kaydetmek istiyor musunuz?"):
        save_path = save_secret(secret)
        if save_path:
            messagebox.showinfo("Başarılı", f"Secret kaydedildi:\n{save_path}")
    
    if messagebox.askyesno("Çıkış", "Pencereyi kapatmak istiyor musunuz?"):
        root.destroy()
    else:
        root.mainloop()

if __name__ == "__main__":
    main()