from tkinter import *

class EnhanceSliderWindow(Toplevel):
    def __init__(self, root, name, enhance, image, current_tab, update_method): # создаем конструктор
        super().__init__(root)


        # сохраним переданные данные в наш класс
        self.name = name
        self.enhancer= enhance(image) # сoздали объект класса enhance, который принял картинку
        self.original = image
        self.image = image.copy() # будет редактироваться
        self.current_tab = current_tab
        self.update_method = update_method

        self.init()

           # добавляем виджеты
        self.factor = DoubleVar(value=1.0) # сила применения фильтра : 1-фильтр ни на сколько не применен

        self.scroll = Scale(
            self, label = self.name,
            from_=0.0, to=2.0, resolution=0.1,
            orient='horizontal',
            variable=self.factor, command=self.value_changed
        )
        self.apply = Button(self, text="Apply", command= self.close)
        self.cancel = Button(self, text="Cancel", command= self.cancel)

        self.draw_widgets()

    def init(self): # метод для инициализации окна
        self.title(f"Enhance {self.name}")
        self.grab_focus()

    def grab_focus(self): # метод, который фокусирует внимание на окошке
        self.grab_set()
        self.focus_force()

    def draw_widgets(self):
        self.scroll.pack(fill="x", expand=1, pady=5, padx=5)
        self.apply.pack(side="left", pady=5, padx=5, expand=1)
        self.cancel.pack(side="left", pady=5, padx=5,expand=1 )

    def value_changed(self, value):
        self.image = self.enhancer.enhance(self.factor.get())
        self.update_method(self.current_tab, self.image)

    def cancel(self):
        self.update_method(self.current_tab, self.original)
        self.close()

    def close(self):
        self.destroy()
