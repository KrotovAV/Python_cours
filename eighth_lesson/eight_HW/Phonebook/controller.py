import model
import view

def start_prog():
    while True:
        view.show_menu()
        var = view.input_value('choose an action')
        view.print_empty()
        match var:
            case '0':
                view.print_values(model.show_all())
            case '1',:
                print("открыть")
            case '2':
                print("записать")
            case '3':
                print("добавить")
            case '4':
                print("изменить")
            case '5':
                print("удлить")
            case '6':
                print("поиск")
            case '7':
                break
        # print(type(var), var)
        view.print_empty()


