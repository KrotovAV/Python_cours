import model_equal
import view
import logger

def main_def():
    logger.logger('------------------')
    logger.logger('Start')
    view.empty_str()
    view.wor()
    view.empty_str()
    nam_a = model_equal.check_namber(view.get_namber())
    equ_c = model_equal.check_action(view.get_action())
    model_equal.init(nam_a, equ_c)
    strnameq, result = model_equal.do_it()
    view.view_data(strnameq, result)
    logger.logger('end')
    view.empty_str()
