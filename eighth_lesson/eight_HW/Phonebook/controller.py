import model
import view

def start_prog():
    view.print_empty()
    ph_book = model.my_split(model.main())
    while True:
        view.show_menu()
        var = view.input_value('choose an action ')
        view.print_empty()
        match var:
            case '1':
                view.print_values(model.show_all(ph_book))
            case '2':
                ph_book = model.add_kontact(ph_book)
                i = 1
                ph_book[len(ph_book)-1].insert(i+1, view.input_value('write name '))
                ph_book[len(ph_book)-1].insert(i+2, view.input_value('write second name '))
                ph_book[len(ph_book)-1].insert(i+3, view.input_value('write last name '))
                ph_book[len(ph_book)-1].insert(i+4, view.input_value('write phone '))
                ph_book[len(ph_book)-1].insert(i+5, view.input_value('write note ')+'\n')
                # ph_book[len(ph_book)-1].insert(i+5, view.input_value('write note '))
                view.print_empty()
                view.print_values(model.show_all(ph_book))
            case '3':
                view.search_menu()
                search_string = model.search(ph_book,view.input_value('Choose namber of search column '), view.input_value('Write to search '))
                view.print_empty()
                search_string = model.my_split(search_string)
                view.print_values(model.show_all(search_string))
            case '4': 
                print("изменить")
            case '5':
                print("удлить")
            case '6':
                print('сохранить')
            case '8':
                break
        # print(type(var), var)
        # view.print_empty()


