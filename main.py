import json
import os
import time
from datetime import datetime

file_path = "notes.json"

def read_notes_file():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            notes = json.load(f)
        return notes
    else:
        return []

def save_notes(notes):
    with open(file_path, "w") as f:
        json.dump(notes, f)

def add_note():
    notes = read_notes_file()
    id = len(notes) + 1
    title = input("🧾 Введите заголовок заметки: ")
    body = input("📝 Введите текст заметки: ")
    created_at = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
    notes.append({"id": id, "title": title, "body": body, "created_at": created_at})
    save_notes(notes)
    print("✔️  Заметка успешно создана.")

def edit_note():
    notes = read_notes_file()
    id = int(input("🔑 Введите идентификатор заметки: "))
    for note in notes:
        if note["id"] == id:
            note["title"] = input("🧾 Введите новый заголовок заметки: ")
            note["body"] = input("📝 Введите новый текст заметки: ")
            note["updated_at"] = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
            save_notes(notes)
            print("✔️  Заметка успешно изменена.")
            return
    print("❌ Заметка с таким идентификатором не найдена.")

def delete_note():
    notes = read_notes_file()
    id = int(input("🔑 Введите идентификатор заметки: "))
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            save_notes(notes)
            print("✔️  Заметка успешно удалена.")
            return
    print("❌ Заметка с таким идентификатором не найдена.")

def read_note():
    notes = read_notes_file()
    id = int(input("🔑 Введите идентификатор заметки: "))
    for note in notes:
        if note["id"] == id:
            print(f"Заметка №{id}: ")
            print(f"{note['title']}\n{note['body']}\n{note['created_at']}")
            return
    print("❌ Заметка с таким идентификатором не найдена.")

def notes_list():
    notes = read_notes_file()
    if not notes:
        print("❌ Список заметок пуст.")
    else:
        date_filter = input("📆✏️  Для фильтрации по дате введите дату в формате ДД.ММ.ГГГГ или оставьте поле пустым: ")
        if date_filter:
            try:
                print(f"Список заметок за {date_filter}: ")
                date_filter = datetime.strptime(date_filter, "%d.%m.%Y")
                filtered_notes = [note for note in notes if datetime.strptime(note["created_at"], "%d.%m.%Y %H:%M:%S").date() == date_filter.date()]
            except ValueError:
                print("❌ Некорректный формат даты.")
                return
        else:
            print("Список всех заметок: ")
            filtered_notes = notes
        for note in filtered_notes:
            print(f"{note['id']}. {note['title']} ({note['created_at']})")

while True:
    print("""
        Выберите действие:
        1. Добавить заметку
        2. Редактировать заметку
        3. Удалить заметку
        4. Просмотреть заметку
        5. Вывести список заметок
        6. Выйти из приложения
    """)
    choice = input("⚙️ ✏️  Введите номер действия: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        read_note()
    elif choice == "5":
        notes_list()
    elif choice == "6":
        break
    else:
        print("❌ Неверный выбор.")