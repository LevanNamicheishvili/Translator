import tkinter as tk
from googletrans import Translator

def translate_text():
    text = text_input.get("1.0", "end-1c")
    translator = Translator()
    translated_text = translator.translate(text, dest='en') 
    text_output.delete("1.0", "end") 
    text_output.insert("1.0", translated_text.text)  


window = tk.Tk()
window.title("Language Translator")


input_label = tk.Label(window, text="Enter text:")
input_label.pack()
text_input = tk.Text(window, height=5, width=50)
text_input.pack()


translate_button = tk.Button(window, text="Translate", command=translate_text)
translate_button.pack()


output_label = tk.Label(window, text="Translated text:")
output_label.pack()
text_output = tk.Text(window, height=5, width=50)
text_output.pack()


window.mainloop()
