from tkinter import *


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
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.root.configure(menu=menu_bar)

    def draw_widgets(self):
        pass

    def _close(self, event): # метод отвечает за закрытие приложения
        self.root.quit()


if __name__=="__main__": #проверяет: является файл запускаемым или импортируемым(если запускаемый, то выполняется условие -->
    PyPhotoEditor().run()




