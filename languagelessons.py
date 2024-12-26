import tkinter as tk
from tkinter import messagebox

# Классы из предыдущего примера
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.progress = {}

    def update_progress(self, language, progress):
        self.progress[language] = progress

    def get_progress(self, language):
        return self.progress.get(language, 0)

class Flashcard:
    def __init__(self, word, translation, image=None, audio=None):
        self.word = word
        self.translation = translation
        self.image = image
        self.audio = audio

class FlashcardSet:
    def __init__(self, title):
        self.title = title
        self.flashcards = []

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def get_flashcards(self):
        return self.flashcards

# Создание набора карточек для урока
spanish_flashcards = FlashcardSet("Испанский - Основы")
spanish_flashcards.add_flashcard(Flashcard(word="Hola", translation="Привет"))
spanish_flashcards.add_flashcard(Flashcard(word="Adiós", translation="До свидания"))
spanish_flashcards.add_flashcard(Flashcard(word="Gracias", translation="Спасибо"))

# GUI
class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")

        # Главный экран
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.main_frame, text="Выберите урок", font=("Arial", 16)).pack(pady=10)
        
        self.lesson_listbox = tk.Listbox(self.main_frame, height=5)
        self.lesson_listbox.pack(padx=20, pady=10)
        self.lesson_listbox.insert(0, "Испанский - Основы")
        self.lesson_listbox.insert(1, "Французский - Основы")
        self.lesson_listbox.insert(2, "Немецкий - Основы")

        tk.Button(self.main_frame, text="Выбрать урок", command=self.select_lesson).pack(pady=10)

    def select_lesson(self):
        selected_lesson = self.lesson_listbox.curselection()
        if not selected_lesson:
            messagebox.showwarning("Ошибка", "Выберите урок из списка")
            return

        # Очистка главного экрана
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.display_tasks()

    def display_tasks(self):
        tk.Label(self.main_frame, text="Выберите задание", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="Карточки", command=self.start_flashcards).pack(pady=5)
        tk.Button(self.main_frame, text="Аудиотренировка", command=self.start_audio_training).pack(pady=5)
        tk.Button(self.main_frame, text="Мини-игра", command=self.start_mini_game).pack(pady=5)

    def start_flashcards(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Карточки: Испанский - Основы", font=("Arial", 16)).pack(pady=10)

        flashcards = spanish_flashcards.get_flashcards()
        self.flashcard_index = 0

        self.word_label = tk.Label(self.main_frame, text=flashcards[self.flashcard_index].word, font=("Arial", 14))
        self.word_label.pack(pady=10)

        tk.Button(self.main_frame, text="Показать перевод", command=self.show_translation).pack(pady=5)
        tk.Button(self.main_frame, text="Следующая карточка", command=self.next_flashcard).pack(pady=5)

    def show_translation(self):
        flashcards = spanish_flashcards.get_flashcards()
        translation = flashcards[self.flashcard_index].translation
        messagebox.showinfo("Перевод", translation)

    def next_flashcard(self):
        flashcards = spanish_flashcards.get_flashcards()
        self.flashcard_index = (self.flashcard_index + 1) % len(flashcards)
        self.word_label.config(text=flashcards[self.flashcard_index].word)

    def start_audio_training(self):
        messagebox.showinfo("Аудиотренировка", "Здесь будет функционал аудиотренировок.")

    def start_mini_game(self):
        messagebox.showinfo("Мини-игра", "Здесь будет функционал мини-игр.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
