import os

from database import FilmsDatabase
from tkinter import *
from tkinter import filedialog as fd

NUMBER_OF_FIELDS = 4
SEARCH_BY_NAME = 0
SEARCH_BY_YEAR = 1
SEARCH_BY_RATE = 2
SEARCH_BY_ID = 3


def add_buttons(root, entries, main_database, listboxes, search_type):
    '''btn_create_db = Button(root, text="Create database",
                           command=lambda: save_as(FilmsDatabase.create_db, 'Create database', main_database))
    btn_delete_db = Button(root, text="Delete database",
                           command=lambda: global_action(FilmsDatabase.del_db, 'Delete database', main_database))
    btn_open_db = Button(root, text="Open database",
                         command= lambda: open_db(FilmsDatabase.open_db, main_database))
    btn_save_db = Button(root, text="Save current database",
                         command=lambda: save_main_db(main_database))  # нажатие

    btn_create_db.place(relheight=0.05, relwidth=0.33)
    btn_delete_db.place(relheight=0.05, relwidth=0.33, relx=0.33)
    btn_open_db.place(relheight=0.05, relwidth=0.34, relx=0.66)
    btn_save_db.place(relheight=0.05, relwidth=0.25, relx=0.5, rely=0.92)'''

    btn_name_search = Button(root, text="Search",
                             command=lambda: print_data(search(search_type.get(), entries, main_database), listboxes))
    btn_insert = Button(root, text='Insert',
                        command=lambda: insert(main_database, entries))
    btn_drop = Button(root, text='Drop',
                      command=lambda: drop(search_type.get(), main_database, entries))
    btn_change = Button(root, text='Change',
                        command=lambda: change(main_database, entries))
    '''btn_make_backup = Button(root, text='Make backup file',
                             command=lambda: global_action(FilmsDatabase.make_backup, 'Make backup', main_database))
    btn_from_backup = Button(root, text='Extract from backup',
                             command=lambda: global_action(FilmsDatabase.from_backup, 'Extract DB', main_database))'''
    btn_save_excel = Button(root, text='Save to .xlsx',
                            command=main_database.save_to_xlsx)
    btn_name_search.place(relheight=0.05, relwidth=0.25, rely=0.05)
    btn_insert.place(relheight=0.05, relwidth=0.25, relx=0.25, rely=0.05)
    btn_drop.place(relheight=0.05, relwidth=0.25, relx=0.5, rely=0.05)
    btn_change.place(relheight=0.05, relwidth=0.25, relx=0.75, rely=0.05)
    # btn_make_backup.place(relheight=0.05, relwidth=0.15, rely=0.92)
    # btn_from_backup.place(relheight=0.05, relwidth=0.15, relx=0.16, rely=0.92)
    btn_save_excel.place(relheight=0.05, relwidth=0.15, relx=0.32, rely=0.92)


def drop(mode, main_database, entries):
    search_result = search(mode, entries, main_database)
    for node in search_result:
        main_database.delete_node(node[3])
    pass


def change(main_database, entries):
    if not main_database.change_node([entries[0].get(),
                                      entries[1].get(),
                                      entries[2].get(),
                                      entries[3].get()]):
        error_window = Toplevel()
        error_window.geometry('300x150+750+450')
        error_window.title('Error')
        label_error = Label(error_window, text='Node with this id is not exist')
        label_error.place(relheight=0.25, relwidth=1, rely=0.08)
        btn_ok = Button(error_window, text='Ok', command=lambda: error_window.destroy())
        btn_ok.place(relheight=0.3, relwidth=0.4, relx=0.3, rely=0.45)


def add_labels(root):
    enter_name_label = Label(root, text='Name:', font="Arial 12")
    enter_year_label = Label(root, text='Year:', font="Arial 12")
    enter_rate_label = Label(root, text='Rating:', font="Arial 12")
    enter_id_label = Label(root, text='Id:', font="Arial 12")

    enter_name_label.place(relheight=0.05, relwidth=0.25, rely=0.1)
    enter_year_label.place(relheight=0.05, relwidth=0.25, relx=0.25, rely=0.1)
    enter_rate_label.place(relheight=0.05, relwidth=0.25, relx=0.5, rely=0.1)
    enter_id_label.place(relheight=0.05, relwidth=0.25, relx=0.75, rely=0.1)


def add_entries(root, name_input, year_input, rate_input, id_input):
    entry_name = Entry(root, textvariable=name_input, font=12)
    entry_year = Entry(root, textvariable=year_input, font=12)
    entry_rate = Entry(root, textvariable=rate_input, font=12)
    entry_id = Entry(root, textvariable=id_input, font=12)

    entry_name.place(relheight=0.05, relwidth=0.25, rely=0.15)
    entry_year.place(relheight=0.05, relwidth=0.25, relx=0.25, rely=0.15)
    entry_rate.place(relheight=0.05, relwidth=0.25, relx=0.5, rely=0.15)
    entry_id.place(relheight=0.05, relwidth=0.25, relx=0.75, rely=0.15)
    return [name_input, year_input, rate_input, id_input]


def add_scroll_listboxes(root):
    def yview(*args):
        for i in range(0, len(listboxes)):
            listboxes[i].yview(*args)

    scrollbar = Scrollbar(root, command=yview)
    scrollbar.place(relheight=0.7, relwidth=0.02, relx=0.98, rely=0.2)

    name_listbox = Listbox(root, yscrollcommand=scrollbar.set)
    year_listbox = Listbox(root, yscrollcommand=scrollbar.set)
    rate_listbox = Listbox(root, yscrollcommand=scrollbar.set)
    id_listbox = Listbox(root, yscrollcommand=scrollbar.set)

    name_listbox.place(relheight=0.7, relwidth=0.25, rely=0.2)
    year_listbox.place(relheight=0.7, relwidth=0.25, relx=0.25, rely=0.2)
    rate_listbox.place(relheight=0.7, relwidth=0.25, relx=0.5, rely=0.2)
    id_listbox.place(relheight=0.7, relwidth=0.2, relx=0.75, rely=0.2)
    listboxes = [name_listbox, year_listbox, rate_listbox, id_listbox]
    return listboxes


def add_menu(root, main_database):
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Open", command=lambda: open_db(main_database))
    filemenu.add_command(label="New", command=lambda: create_db(main_database))
    filemenu.add_command(label="Save", command=lambda: main_database.save_db(main_database.filename))
    filemenu.add_command(label="Save as", command=lambda: save_as(main_database))
    filemenu.add_command(label="Save as excel", command=lambda: save_excel(main_database))

    backup_menu = Menu(mainmenu, tearoff=0)
    backup_menu.add_command(label="Make backup file", command=lambda: make_backup(main_database))
    backup_menu.add_command(label="Open from backup...", command=from_backup)

    select_field_menu = Menu(mainmenu, tearoff=0)
    search_type_var = IntVar()
    select_field_menu.add_radiobutton(label="name", value=0,
                            variable=search_type_var)
    select_field_menu.add_radiobutton(label="year", value=1,
                            variable=search_type_var)
    select_field_menu.add_radiobutton(label="rate", value=2,
                            variable=search_type_var)
    select_field_menu.add_radiobutton(label="id", value=3,
                            variable=search_type_var)

    mainmenu.add_cascade(label="File", menu=filemenu)
    mainmenu.add_cascade(label="Backup", menu=backup_menu)
    mainmenu.add_cascade(label='Select field', menu=select_field_menu)


    # select_field_menu.add_command(label='Select field', command=lambda: )


    #mb = Menubutton(mainmenu, text="Search by...", relief=RAISED)
    #mb.place(relheight=0.05, relwidth=0.2, relx=0.8, rely=0.92)
    #mb.menu = Menu(mb, tearoff=0)
    #mb["menu"] = mb.menu

    return search_type_var


def open_db(main_database):
    file_name = fd.askopenfilename()
    new_db = FilmsDatabase(file_name)
    if new_db:
        main_database.save_db(main_database.filename)
        main_database.change(new_db)


def create_db(main_database):
    os.chdir('Data')
    file_name = fd.asksaveasfilename(filetypes=(("HDB files", "*.hdb"),
                                                ("All files", "*.*")))
    os.chdir('..')
    new_db = FilmsDatabase(file_name)
    main_database.save_db(main_database.filename)
    main_database.change(new_db)


def save_as(main_database):
    os.chdir('Data')
    file_name = fd.asksaveasfilename(filetypes=(("HDB files", "*.hdb"),
                                                ("All files", "*.*")))
    os.chdir('..')
    main_database.save_db(file_name)


def make_backup(main_database):
    os.chdir('Backup')
    file_name = fd.asksaveasfilename(filetypes=(("ZIP files", "*.zip"),
                                                ("All files", "*.*")))
    os.chdir('..')
    main_database.make_backup(file_name)


def from_backup():
    file_name_zip = fd.askopenfilename(initialdir=os.getcwd() + '/Backup',
                                       title='Select file to unzip',
                                       filetypes=(("ZIP files", "*.zip"),
                                                  ("All files", "*.*")))
    FilmsDatabase.from_backup(file_name_zip, os.getcwd() + '/Data/')


def save_excel(main_database):
    os.chdir('Data')
    file_name = fd.asksaveasfilename(filetypes=(("XLSX files", "*.xlsx"),
                                                ("All files", "*.*")))
    os.chdir('..')
    main_database.save_to_xlsx(file_name)


'''def global_action(func, text, main_database):
    def command_action(main_database):

        if filename.get():
            returned_value = func(filename.get())
            if returned_value:
                if isinstance(returned_value, FilmsDatabase):
                    opener(main_database, returned_value)
                create_window.destroy()
        else:
            error_window = Toplevel()
            error_window.geometry('300x150+750+450')
            error_window.title('Error')
            label_error = Label(error_window, text='Filename is not specified')
            label_error.place(relheight=0.25, relwidth=1, rely=0.08)
            btn_ok = Button(error_window, text='Ok', command=lambda: error_window.destroy())
            btn_ok.place(relheight=0.3, relwidth=0.4, relx=0.3, rely=0.45)

    create_window = Toplevel()
    create_window.title(text)
    create_window.geometry('300x150+700+400')
    filename = StringVar()
    label_filename = Label(create_window, text='Enter filename:', font=14)
    label_filename.place(relheight=0.3, relwidth=0.8, relx=0.1)
    entry_filename = Entry(create_window, textvariable=filename, font=14)
    entry_filename.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.3)
    btn_create = Button(create_window, text=text, command=lambda: command_action(main_database))
    btn_create.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.7)'''


def search(mode, entries, main_database):
    """
    :param listboxes:
    :param entries:
    :param main_database:
    :param mode: mode of search:
                            0 - by name,
                            1 - by year,
                            2 - by rate,
                            3 - by id
    :return:
    """
    search_functions = [main_database.search_by_name, main_database.search_by_year,
                        main_database.search_by_rate, main_database.search_by_id]
    if entries[mode].get():
        search_result = search_functions[mode](entries[mode].get())
    else:
        search_result = []
    return search_result


def print_db(main_database, listboxes: list):
    print_data(main_database.db, listboxes)


def print_data(data, listboxes: list):
    for listbox in listboxes:
        listbox.delete(0, END)
    for row in data:
        for i in range(0, len(row)):
            listboxes[i].insert(END, row[i])


def insert(main_database: FilmsDatabase, entries: list):
    main_database.add([entries[0].get(), entries[1].get(),
                       entries[2].get(), entries[3].get()])


def delete():
    # TODO make
    pass


def start_create_db(window, main_database):
    os.chdir('Data')
    file_name = fd.asksaveasfilename(filetypes=(("HDB files", "*.hdb"),
                                                ("All files", "*.*")))
    os.chdir('..')
    new_db = FilmsDatabase(file_name, empty=True)
    main_database.change(new_db)
    window.destroy()


def start_open_db(window, main_database):
    os.chdir('Data')
    file_name = fd.askopenfilename()
    os.chdir('..')
    opened_db = FilmsDatabase.open_db(file_name)
    main_database.change(opened_db)
    window.destroy()


def main():
    main_database = FilmsDatabase('', empty=True)
    start_window = Tk()
    start_window.title('Open or create?')
    start_window.geometry('300x150+700+400')
    filename = StringVar()
    label_filename = Label(start_window, text='Select option:', font=14)
    label_filename.place(relheight=0.3, relwidth=0.8, relx=0.1)
    btn_create = Button(start_window, text='Create database',
                        command=lambda: start_create_db(start_window, main_database))
    btn_create.place(relheight=0.25, relwidth=0.5, relx=0.25, rely=0.7)
    btn_open = Button(start_window, text='Open database', command=lambda: start_open_db(start_window, main_database))
    btn_open.place(relheight=0.25, relwidth=0.5, relx=0.25, rely=0.3)
    start_window.mainloop()

    root = Tk()
    root.title('Interactive database')
    root.geometry('900x700+350+70')
    name_input = StringVar()
    year_input = StringVar()
    rate_input = StringVar()
    id_input = StringVar()
    entries = add_entries(root, name_input, year_input, rate_input, id_input)
    add_labels(root)
    listboxes = add_scroll_listboxes(root)
    search_type = add_menu(root, main_database)
    add_buttons(root, entries, main_database, listboxes, search_type)

    root.mainloop()


if __name__ == '__main__':
    main()
