import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp
        }

class NotesApp:
    def __init__(self):
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as file:
                data = json.load(file)
                notes = []
                for note_data in data:
                    note = Note(**note_data)
                    notes.append(note)
                return notes
        return []

    def save_notes(self):
        data = [note.to_dict() for note in self.notes]
        with open(NOTES_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def add_note(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        next_id = self.get_next_id()

        new_note = Note(next_id, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()

        print("Заметка добавлена!")

    def get_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print(f"Дата/время: {note.timestamp}")
            print("-" * 30)

    def edit_note(self):
        id_to_edit = input("Введите ID заметки для редактирования: ")

        for note in self.notes:
            if note.id == id_to_edit:
                new_title = input("Введите новый заголовок заметки: ")
                new_body = input("Введите новый текст заметки: ")
                new_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                note.title = new_title
                note.body = new_body
                note.timestamp = new_timestamp

                self.save_notes()

                print("Заметка отредактирована!")
                return

        print("Заметка с таким ID не найдена.")

    def delete_note(self):
        id_to_delete = input("Введите ID заметки для удаления: ")

        self.notes = [note for note in self.notes if note.id != id_to_delete]
        self.save_notes()

        print("Заметка удалена!")

    def get_next_id(self):
        if not self.notes:
            return "1"

        last_id = int(self.notes[-1].id)
        return str(last_id + 1)

    def run(self):
        while True:
            print("1. Просмотреть заметки")
            print("2. Добавить заметку")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.get_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                self.edit_note()
            elif choice == "4":
                self.delete_note()
            elif choice == "5":
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    app = NotesApp()
    app.run()