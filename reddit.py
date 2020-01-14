import tkinter as tk
import json
import random
import os


class StudySets():
    def __init__(self):

        #These sets are normally stored as json files, and i append the names of my json files into a list

        self.study_sets = ['set1','set2','set3']
        self.current_set = ''

studyset_obj = StudySets()


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class SelectionPage(Page):
    def __init__(self, controller, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Selection page')
        label.pack()
        

        listbox = tk.Listbox(self)
        listbox.pack()


        for study_set in studyset_obj.study_sets:
            listbox.insert(tk.END, study_set)

        def study_button():
            studypage = controller.pages['StudyPage']
            studypage.show()

            studyset_obj.current_set = listbox.get(tk.ACTIVE)

        studybutton = tk.Button(self, text="Study", command=study_button)
        studybutton.pack()


class StudyPage(Page):
    def __init__(self, controller, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        

        label = tk.Label(self, text = 'This is the study page')
        label.pack()

        def testprint():
            print(studyset_obj.current_set)

        testbutton = tk.Button(self, text="return selected set", command=testprint)
        testbutton.pack()


class ModifyPage(Page):
    def __init__(self, controller, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='This is the modify page')
        label.pack()


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Create dictionary of Page subclasses.
        self.pages = {}
        for Subclass in (StudyPage, SelectionPage, ModifyPage):
            self.pages[Subclass.__name__] = Subclass(self)

        studypage, selectionpage, modifypage = self.pages.values()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        studypage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        selectionpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        modifypage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        selectionpage.show()



if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()