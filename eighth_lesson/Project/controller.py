import view, model



def set_value():
    a = view.input_value('Whrite a namber')
    b = view.input_value('Whrite a namber')
    model.set_value_a(a)
    model.set_value_b(b)

def print_values():
    view.print_values(model.get_value_a())
    view.print_values(model.get_value_b())