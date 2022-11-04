import model
import view

def start_prog():
    view.print_empty()
    # ph_book = model.my_split(model.main())
    ph_book = '1 | Choose | action ( 1 ) |to |open |file'
    ph_book = model.my_split(ph_book)
    while True:
        view.show_menu()
        var = view.input_value('choose an action ')
        view.print_empty()
        match var:
            case '2':
                view.print_values(model.show_all(ph_book))
            case '3':
                ph_book = model.add_kontact(ph_book)
                i = 1
                ph_book[len(ph_book)-1].insert(i+1, view.input_value('write name '))
                ph_book[len(ph_book)-1].insert(i+2, view.input_value('write second name '))
                ph_book[len(ph_book)-1].insert(i+3, view.input_value('write last name '))
                ph_book[len(ph_book)-1].insert(i+4, view.input_value('write phone '))
                ph_book[len(ph_book)-1].insert(i+5, view.input_value('write note ')+'\n')
                view.print_empty()
                # view.print_values(model.show_all(ph_book))
            case '4':
                search_string = ''
                view.search_menu()
                search_string, val_i = model.search(ph_book,view.input_value('Choose namber of search column '), view.input_value('Write to search '))
                view.print_empty()
                search_string = model.my_split(search_string)
                view.print_values(model.show_all(search_string))
            case '5': 
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

                change = view.input_value('Write "y" to change ')
                if change == 'y':
                    ph_book[val_i][1] = view.change_value(ph_book, val_i, 1, 'Change name '+ '(' + ph_book[val_i][1]+ ')  ')
                    ph_book[val_i][2] = view.change_value(ph_book, val_i, 2, 'Change second name '+ '(' + ph_book[val_i][2]+ ')  ')
                    ph_book[val_i][3] = view.change_value(ph_book, val_i, 3, 'Change last name '+ '(' + ph_book[val_i][3]+ ')  ')
                    ph_book[val_i][4] = view.change_value(ph_book, val_i, 4, 'Change phone  '+ '(' + ph_book[val_i][4]+ ')  ')
                    ph_book[val_i][5] = ph_book[val_i][5][:-1]
                    ph_book[val_i][5] = (view.change_value(ph_book, val_i, 5, 'Change note  '+ '(' + ph_book[val_i][5]+ ')  ')) + '\n'
                view.print_empty()
                # view.print_values(model.show_all(ph_book))
            case '6':
                del_string = ''
                view.change_menu()
                var_ch_del = view.input_value('Choose namber of search to delite ')
                match var_ch_del:
                    case '1':
                        del_string, val_i_del = model.search(ph_book,'1', view.input_value('Write to search '))
                    case '2':
                        view.search_menu()
                        del_string, val_i_del = model.search(ph_book,view.input_value('Choose namber of search column '), view.input_value('Write to search '))
                view.print_empty()
                del_string = model.my_split(del_string)
                view.print_values(model.show_all(del_string))
                delite = view.input_value('Write " d " to delite ')
                view.print_empty()
                if delite == 'd':
                    ph_book.pop(val_i_del)
                view.print_empty()
                ph_book = model.renumerate(ph_book)
                # view.print_values(model.show_all(ph_book))
            case '1':
                view.op_menu()
                view.print_empty()
                open_ch  = view.input_value('Choose namber of action to open file ')
                match open_ch:
                    case '1':
                        view.print_values('Default path  ' + view.default_ope_path)
                        ph_book = model.my_split(model.main(view.default_ope_path))
                    case '2':
                        ph_book = model.my_split(model.main(view.input_value('Write path to open ')))
                    case '3':
                        view.default_ope_path = view.input_value('Write path to default open ')
                        ph_book = model.my_split(model.main(view.default_ope_path))
                view.print_empty()
            case '7':
                view.rec_menu()
                record_ch = view.input_value('Choose namber of action to record in file ')
                match record_ch:
                    case '1':
                        view.print_values('Default path : ' + view.default_rec_path)
                        model.record(ph_book, view.default_rec_path)
                    case '2':
                        model.record(ph_book, view.default_rec_path(view.input_value('Write path to record ')))
                    case '3':
                        view.default_rec_path = view.input_value('Write path to default record ')
                        model.record(ph_book, view.default_rec_path)
                view.print_empty()
            case '8':
                break



