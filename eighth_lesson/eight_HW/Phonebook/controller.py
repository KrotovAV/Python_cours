import model
import view

def start_prog():
    ph_book = model.main()
    while True:
        view.show_menu()
        var = view.input_value('choose an action ')
        view.print_empty()
        match var:
            case '1':
                view.print_values(model.show_all(ph_book))
            case '2':
                # print(ph_book)
                ph_book = model.add_kontact(ph_book)
                i = 1
                ph_book[len(ph_book)-1].insert(i+1, view.input_value('write name '))
                ph_book[len(ph_book)-1].insert(i+2, view.input_value('write second name '))
                ph_book[len(ph_book)-1].insert(i+3, view.input_value('write last name '))
                ph_book[len(ph_book)-1].insert(i+4, view.input_value('write phone '))
                ph_book[len(ph_book)-1].insert(i+5, view.input_value('write note '))
                ph_book[len(ph_book)-1].insert(i+6, '\n')
                ph_book = model.replace(ph_book)
                view.print_empty()
                # print(ph_book)
                view.print_values(model.show_all(ph_book))
                view.print_empty()
            case '3':
                print("изменить")
            case '4':
                print("удлить")
            case '5':
                print("поиск")
            case '6':
                print('сохранить')
            case '7':
                break
        # print(type(var), var)
        # view.print_empty()


