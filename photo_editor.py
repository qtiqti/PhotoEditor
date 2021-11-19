from tkinter import *


class PyPhotoEditor:
    def __init__(self): # конструктор класса
        self.root = Tk()
        self.init()

    def init(self): # метод, который инициализирует окно
        self.root.title("Photo Editor") # Заголовок окна
        self.root.iconbitmap("resources/icon.jpg")

    def run(self): # метод, который запускает окно
        self.draw_menu() # метод для прориосовки меню
        self.draw_widgets()  # метод для прорисовки виджетов

        self.root.mainloop() # Основной цикл программы

    def draw_menu(self): # определяем два ранее описанных метода
        pass

    def draw_widgets(self):
        pass

