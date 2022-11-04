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
                search_string = ''
                view.search_menu()
                search_string, val_i = model.search(ph_book,view.input_value('Choose namber of search column '), view.input_value('Write to search '))
                view.print_empty()
                search_string = model.my_split(search_string)
                view.print_values(model.show_all(search_string))
            case '4': 
                search_string = ''
                view.change_menu()
                var_ch = view.input_value('Choose namber of search to change ')
                # view.search_menu()
                match var_ch:
                    case '1':
                        # view.search_menu()
                        search_string, val_i = model.search(ph_book,'1', view.input_value('Write to search '))
                    case '2':
                        view.search_menu()
                        search_string, val_i = model.search(ph_book,view.input_value('Choose namber of search column '), view.input_value('Write to search '))
                view.print_empty()
                search_string = model.my_split(search_string)
                view.print_values(model.show_all(search_string))
                # view.print_empty()
                ph_book[val_i][1]= view.change_value(ph_book, val_i, 1, 'Change name '+ '(' + ph_book[val_i][1]+ ')  ')
                ph_book[val_i][2]= view.change_value(ph_book, val_i, 2, 'Change second name '+ '(' + ph_book[val_i][2]+ ')  ')
                ph_book[val_i][3]= view.change_value(ph_book, val_i, 3, 'Change last name '+ '(' + ph_book[val_i][3]+ ')  ')
                ph_book[val_i][4]= view.change_value(ph_book, val_i, 4, 'Change phone  '+ '(' + ph_book[val_i][4]+ ')  ')
                ph_book[val_i][5]= (view.change_value(ph_book, val_i, 5, 'Change note  '+ '(' + ph_book[val_i][5]+ ')  '))+'\n'

                # view.print_values(model.show_all(ph_book[val_i]))
            case '5':
                print("удлить")
            case '6':
                print('сохранить')
            case '8':
                break
        # print(type(var), var)
        # view.print_empty()


