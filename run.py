import pandas as pd
import random
import os

# Определите путь к файлу в той же папке, что и программа
file_path = os.path.join(os.path.dirname(__file__), 'data.xlsx')

# Загрузите Excel файл
data = pd.read_excel(file_path)

# Цвета для вывода
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Перемешайте индексы вопросов
indices = list(data.index)
random.shuffle(indices)

# Задавайте вопросы по одному в цикле
for i in indices:
    question = data.iloc[i, 0]  # Вопрос из первой колонки
    correct_answer = data.iloc[i, 1]  # Правильный ответ из второй колонки

    # Отобразите вопрос и запросите ответ у пользователя
    print(f"Вопрос: {question}")
    user_answer = input("Ваш ответ: ")

    # Проверьте ответ
    if user_answer.strip().lower() == str(correct_answer).strip().lower():
        print(f"{GREEN}Правильно!{RESET}")
    else:
        print(f"{RED}Неправильно. Правильный ответ: {correct_answer}{RESET}")

print("Все вопросы заданы!")
