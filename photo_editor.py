from tkinter import *
import tkinter.filedialog as fd
from PIL import Image, ImageTk
import os

class PyPhotoEditor:
    def __init__(self): # конструктор класса
        self.root = Tk()
        self.init()

    def init(self): # метод, который инициализирует окно
        self.root.title("Photo Editor") # Заголовок окна
        #self.root.iconphoto(True, PhotoImage(file="resources/icon.png"))

        self.root.bind("<Escape>",self._close)# команда: при нажатии на escapе закрытие программы

    def run(self): # метод, который запускает окно
        self.draw_menu() # метод для прориосовки меню
        self.draw_widgets()  # метод для прорисовки виджетов

        self.root.mainloop() # Основной цикл программы

    def draw_menu(self): # определяем два ранее описанных метода
        menu_bar = Menu(self.root) # каркас меню

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_new_image)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.root.configure(menu=menu_bar)

    def draw_widgets(self):
        pass

    def open_new_image(self):
        image_path = fd.askopenfilename(filetypes=(('png files', '*.png'),('jpeg files', '*.jpeg'),('jpg files', '*.jpg'), )) #запрос картинки

        image = ImageTk.PhotoImage(Image.open(image_path)) #сначала получаем путь до картинки, потом открываем картинку в формате библиотеки PIL, потом преобразуем в картинку, которую можно редактировать в Tkinter
        image_panel=Label(self.root, image=image)
        image_panel.image=image #сохраним картинку в панели, чтобы она сразу не закрывалась
        image_panel.pack()

    def _close(self, event): # метод отвечает за закрытие приложения
        self.root.quit()


if __name__=="__main__": #проверяет: является файл запускаемым или импортируемым(если запускаемый, то выполняется условие -->
    PyPhotoEditor().run()



