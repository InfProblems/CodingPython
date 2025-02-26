import tkinter as tk
from tkinter import ttk
import random

def shuffle_words_and_add_slash():
    text = input_text.get("1.0", tk.END).strip()
    words = text.split()
    random.shuffle(words)
    result = "/".join(words)
    result = result.rstrip()  # Удаляем пробелы справа
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.insert("1.0", result)
    output_text.config(state=tk.DISABLED)


# Создание основного окна
root = tk.Tk()
root.title("Word Shuffler - Scalable")

# Настройка масштабируемости окна
root.grid_rowconfigure(0, weight=0)  # Лейбл ввода (фиксированный)
root.grid_rowconfigure(1, weight=1)  # Текстовое поле ввода - растягивается по вертикали
root.grid_rowconfigure(2, weight=0)  # Кнопка (фиксированная)
root.grid_rowconfigure(3, weight=0)  # Лейбл вывода (фиксированный)
root.grid_rowconfigure(4, weight=1)  # Текстовое поле вывода - растягивается по вертикали

root.grid_columnconfigure(0, weight=1)  # Колонка - растягивается по горизонтали
root.grid_columnconfigure(1, weight=1)  # Колонка - растягивается по горизонтали (если есть)


style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

# Ввод текста
input_label = ttk.Label(root, text="Enter sentence:", font=('Arial', 12))
input_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)  # Располагаем лейбл слева

input_text = tk.Text(root, height=10, width=40, font=('Arial', 12))  # Увеличили высоту
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew") # sticky="nsew" - растягивание во всех направлениях

# Кнопка
shuffle_button = ttk.Button(root, text="Shuffle Words", command=shuffle_words_and_add_slash)
shuffle_button.grid(row=2, column=0, columnspan=2, pady=10)


# Вывод результата
output_label = ttk.Label(root, text="Shuffled Sentence:", font=('Arial', 12))
output_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

output_text = tk.Text(root, height=10, width=40, font=('Arial', 12), state=tk.DISABLED)  # Увеличили высоту
output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew") # sticky="nsew" - растягивание во всех направлениях

root.mainloop()