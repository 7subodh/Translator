import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip
from gtts import gTTS
import os

# Function to translate text
def translate_text():
    input_text = text_input.get("1.0", tk.END).strip()
    src_lang = src_lang_combo.get()
    dest_lang = dest_lang_combo.get()

    if not input_text:
        messagebox.showerror("Error", "Please enter text to translate.")
        return
    
    try:
        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(input_text)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function for Text-to-Speech
def text_to_speech():
    text = text_output.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "No translated text to convert to speech.")
        return

    try:
        tts = gTTS(text, lang=dest_lang_combo.get())
        tts.save("speech.mp3")
        os.system("start speech.mp3")  # For Windows, use "start", for Linux/macOS use "mpg321 speech.mp3"
    except Exception as e:
        messagebox.showerror("TTS Error", str(e))

# Function to copy translated text
def copy_text():
    translated_text = text_output.get("1.0", tk.END).strip()
    if translated_text:
        pyperclip.copy(translated_text)
        messagebox.showinfo("Copied", "Text copied to clipboard.")
    else:
        messagebox.showerror("Error", "No text to copy.")

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x450")
root.configure(bg="lightgray")

# Language List
languages = ["auto"] + GoogleTranslator().get_supported_languages()

# Labels and Dropdowns
tk.Label(root, text="Source Language:", bg="lightgray", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
src_lang_combo = ttk.Combobox(root, values=languages, width=20)
src_lang_combo.grid(row=0, column=1, padx=10, pady=5)
src_lang_combo.set("english")

tk.Label(root, text="Target Language:", bg="lightgray", font=("Arial", 10)).grid(row=0, column=2, padx=10, pady=5, sticky="w")
dest_lang_combo = ttk.Combobox(root, values=languages, width=20)
dest_lang_combo.grid(row=0, column=3, padx=10, pady=5)
dest_lang_combo.set("french")

# Input Text
tk.Label(root, text="Enter Text:", bg="lightgray", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
text_input = tk.Text(root, height=5, width=60, font=("Arial", 10))
text_input.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

# Translate Button
translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="blue", fg="white", font=("Arial", 12, "bold"))
translate_btn.grid(row=3, column=1, columnspan=2, pady=10)

# Output Text
tk.Label(root, text="Translated Text:", bg="lightgray", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
text_output = tk.Text(root, height=5, width=60, font=("Arial", 10))
text_output.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

# Buttons for Copy and Text-to-Speech
copy_btn = tk.Button(root, text="Copy", command=copy_text, bg="green", fg="white", font=("Arial", 12, "bold"))
copy_btn.grid(row=6, column=0, pady=10, padx=10)

tts_btn = tk.Button(root, text="Text-to-Speech", command=text_to_speech, bg="purple", fg="white", font=("Arial", 12, "bold"))
tts_btn.grid(row=6, column=1, pady=10, padx=10)

exit_btn = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", font=("Arial", 12, "bold"))
exit_btn.grid(row=6, column=2, pady=10, padx=10)

root.mainloop()
