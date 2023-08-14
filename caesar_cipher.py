# Credit to Mariya Sha of Python Simplified 
# and her great python (unittest) TDD video 
# "Python TDD Workflow - Unit Testing Code Example for Beginners"
# https://www.youtube.com/watch?v=ibVSPVz2LAA

import string

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s : %(lineno)d : %(message)s')
file_handler = logging.FileHandler('caesar_cipher.log')
#file_handler.setLevel(logging.INFO) #An example of changing the logging on file handler rather than the logger
file_handler.setFormatter(formatter)


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# logging.basicConfig(filename='caesar_cipher.log', level=logging.DEBUG, 
#                    format='%(asctime)s : %(levelname)s : %(module)s : %(lineno)d : %(message)s')

# logger.basicConfig(filename='caesar_cipher.log', level=logging.DEBUG, 
#                   format='%(asctime)s : %(levelname)s : %(module)s : %(lineno)d : %(message)s')


def engine(operation, message, offset):
    # logging.debug(f"operation:{operation}, message: {message}, offset: {offset}")
    logger.debug(f"operation:{operation}, message: {message}, offset: {offset}")
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    output = "".join( [abc[abc.find(char) + 1] for index, char in enumerate(message)] )
    logger.debug(f"output = {output}")
    return output



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result =  x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result

if __name__ == '__main__':
    num_1 = 10
    num_2 = 0

    add_result = add(num_1, num_2)
    # logging.debug('Add: {} - {} = {}'.format(num_1, num_2, add_result))
    logger.debug('Add: {} - {} = {}'.format(num_1, num_2, add_result))

    sub_result = subtract(num_1, num_2)
    # logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
    logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

    mul_result = multiply(num_1, num_2)
    # logging.debug('Mul: {} - {} = {}'.format(num_1, num_2, mul_result))
    logger.debug('Mul: {} - {} = {}'.format(num_1, num_2, mul_result))

    div_result = divide(num_1, num_2)
    # logging.debug('Div: {} - {} = {}'.format(num_1, num_2, div_result))
    logger.debug('Div: {} - {} = {}'.format(num_1, num_2, div_result))
