import model_equal
import view
import logger

def main_def():
    logger.logger('Start')
    view.empty_str()
    view.wor()
    view.empty_str()
    value_a = view.get_value()
    if not value_a.isdigit():
            view.err_value()
            value_a = view.get_value()
    value_c = view.get_action()
    if value_c not in ['+', '-', '*', '/', '=']:
            view.err_action()
            value_c = view.get_action()
    model_equal.init(value_a, value_c)
    strnameq, result = model_equal.do_it()
    view.view_data(strnameq, result)
    logger.logger('end')
    view.empty_str()
