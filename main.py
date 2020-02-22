from database import FilmsDatabase
from tkinter import *
from tkinter import messagebox

NUMBER_OF_FIELDS = 4
SEARCH_BY_NAME = 0
SEARCH_BY_YEAR = 1
SEARCH_BY_RATE = 2
SEARCH_BY_ID = 3


def main():
    def search_by_name():
        search(SEARCH_BY_NAME)

    def search_by_year():
        search(SEARCH_BY_YEAR)

    def search_by_rate():
        search(SEARCH_BY_RATE)

    def search_by_id():
        search(SEARCH_BY_ID)

    def search(mode):
        """
        :param mode: mode of search:
                                0 - by name,
                                1 - by year,
                                2 - by rate,
                                3 - by id
        :return:
        """
        entries = [name_input, year_input, rate_input, id_input]
        search_functions = [film_db.search_by_name, film_db.search_by_year,
                            film_db.search_by_rate, film_db.search_by_id]
        search_result = search_functions[mode](entries[mode].get())
        print_data(search_result)

    def print_db():
        print_data(film_db.db)

    def print_data(data):
        field_values_to_show = []
        for i in range(0, NUMBER_OF_FIELDS):
            field_values_to_show.append('\n'.join([str(val[i]) for val in data]))

        if data:
            for i in range(0, NUMBER_OF_FIELDS):
                field_labels[i].config(text=field_values_to_show[i])
        else:
            for i in range(0, NUMBER_OF_FIELDS):
                field_labels[i].config(text="")


    def add():
        film_db.add([name_input.get(), year_input.get(),
                     rate_input.get(), id_input.get()])

    def delete():
        print('delete')

    root = Tk()
    root.title('Interactive database')
    root.geometry('600x500+350+70')

    film_db = FilmsDatabase('Data/films.hdb', 'Data/films.hdbd')
    btn_print = Button(text="print db", command=print_db)  # нажатие
    btn_search = Button(text="search", command=search)  # нажатие
    btn_add = Button(text="add element", command=add)  # нажатие
    btn_delete = Button(text="delete element", command=delete)  # нажатие

    btn_print.grid(column=0, row=0)
    btn_add.grid(column=1, row=0)
    btn_delete.grid(column=2, row=0)
    btn_search.grid(column=3, row=0)

    name_input = StringVar()
    year_input = StringVar()
    rate_input = StringVar()
    id_input = StringVar()
    entry_name = Entry(textvariable=name_input, font=12)
    entry_year = Entry(textvariable=year_input, font=12)
    entry_rate = Entry(textvariable=rate_input, font=12)
    entry_id = Entry(textvariable=id_input, font=12)

    entry_name.grid(row=1, column=1, columnspan=3)
    entry_year.grid(row=2, column=1, columnspan=3)
    entry_rate.grid(row=3, column=1, columnspan=3)
    entry_id.grid(row=4, column=1, columnspan=3)

    name_label = Label(text="", font='Arial 14')
    year_label = Label(text="", font='Arial 14')
    rate_label = Label(text="", font='Arial 14')
    id_label = Label(text="", font='Arial 14')
    field_labels = [name_label, year_label, rate_label, id_label]

    btn_name_search = Button(text="Search by name", command=search_by_name)
    btn_year_search = Button(text="Search by year", command=search_by_year)
    btn_rate_search = Button(text="Search by rate", command=search_by_rate)
    btn_id_search = Button(text="Search by id", command=search_by_id)

    btn_name_search.grid(column=4, row=1)
    btn_year_search.grid(column=4, row=2)
    btn_rate_search.grid(column=4, row=3)
    btn_id_search.grid(column=4, row=4)

    enter_name_label = Label(text='Name:', font="Arial 12")
    enter_year_label = Label(text='Year:', font="Arial 12")
    enter_rate_label = Label(text='Rating:', font="Arial 12")
    enter_id_label = Label(text='Id:', font="Arial 12")

    enter_name_label.grid(row=1, column=0, padx=10, pady=10, sticky=N+S+W+E)
    enter_year_label.grid(row=2, column=0, padx=10, pady=10, sticky=N+S+W+E)
    enter_rate_label.grid(row=3, column=0, padx=10, pady=10, sticky=N+S+W+E)
    enter_id_label.grid(row=4, column=0, padx=10, pady=10, sticky=N+S+W+E)

    name_title_label = Label(text='Name:', font="Arial 12")
    year_title_label = Label(text='Year:', font="Arial 12")
    rate_title_label = Label(text='Rating:', font="Arial 12")
    id_title_label = Label(text='Id:', font="Arial 12")

    name_title_label.grid(row=5, column=0, padx=10, pady=10, sticky=N+S+W+E)
    year_title_label.grid(row=5, column=1, padx=10, pady=10, sticky=N+S+W+E)
    rate_title_label.grid(row=5, column=2, padx=10, pady=10, sticky=N+S+W+E)
    id_title_label.grid(row=5, column=3, padx=10, pady=10, sticky=N+S+W+E)

    name_label.grid(row=6, column=0, rowspan=4)
    year_label.grid(row=6, column=1, rowspan=4)
    rate_label.grid(row=6, column=2, rowspan=4)
    id_label.grid(row=6, column=3, rowspan=4)

    root.mainloop()

if __name__ == '__main__':
    main()