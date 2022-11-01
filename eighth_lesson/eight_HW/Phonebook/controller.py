import model
import view

def start_prog():
    while True:
        view.show_menu()
        var = view.input_value('choose an action ')
        # view.print_empty()
        match var:
            case '1':
                view.print_values(model.show_all())
            case '2':
                print("добавить")
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


