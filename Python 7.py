import random

# Словарь с русскими и английскими словами
words = {
    'кот': 'cat',
    'собака': 'dog',
    'дерево': 'tree',
    'машина': 'car',
    'дом': 'house',
    'солнце': 'sun',
    'луна': 'moon',
    'река': 'river',
    'гора': 'mountain',
    'цветок': 'flower'
}

def guess_the_word():
    # Количество попыток
    max_attempts = 3
    attempts = 0

    # Выбираем случайное слово
    russian_word, english_word = random.choice(list(words.items()))

    print(f"Угадайте слово на английском: {russian_word}")

    while attempts < max_attempts:
        user_guess = input("Ваш ответ: ").strip().lower()

        if user_guess == english_word:
            print("Поздравляем! Вы угадали слово.")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Неправильно! Осталось попыток: {remaining_attempts}")

            if remaining_attempts == 0:
                print(f"Игра окончена! Правильный ответ: {english_word}")

if __name__ == "__main__":
    guess_the_word()

#2 задание

import tkinter as tk
from tkinter import filedialog, messagebox

def save_file():
    # Получаем введенный текст
    text = text_area.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите текст.")
        return
    
    # Получаем тип файла из выпадающего меню
    file_type = file_type_var.get()
    
    # Определяем расширение файла
    if file_type == "Текстовый файл (.txt)":
        extension = ".txt"
    elif file_type == "HTML файл (.html)":
        extension = ".html"
    
    # Открываем диалог для выбора места сохранения файла
    file_path = filedialog.asksaveasfilename(defaultextension=extension,
                                               filetypes=[(file_type, f"*{extension}")])
    
    if not file_path:
        return  # Если пользователь отменил сохранение
    
    try:
        # Сохраняем текст в файл
        if extension == ".html":
            # Если сохраняем в HTML, добавляем базовую структуру HTML
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("<html>\n<head>\n<title>Document</title>\n</head>\n<body>\n")
                f.write(f"<p>{text}</p>\n")
                f.write("</body>\n</html>")
        else:
            # Сохраняем как текстовый файл
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
        
        messagebox.showinfo("Успех", "Файл успешно сохранен.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

# Создаем главное окно
root = tk.Tk()
root.title("Сохранение текста")

# Создаем текстовую область
text_area = tk.Text(root, wrap=tk.WORD, width=50, height=20)
text_area.pack(pady=10)

# Создаем выпадающее меню для выбора типа файла
file_type_var = tk.StringVar(value="Текстовый файл (.txt)")
file_type_menu = tk.OptionMenu(root, file_type_var, "Текстовый файл (.txt)", "HTML файл (.html)")
file_type_menu.pack(pady=5)

# Создаем кнопку для сохранения файла
save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack(pady=10)

# Запускаем главный цикл приложения
root.mainloop()
