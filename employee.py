import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')


file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info('Created employee: {} - {}'.format(self.fullname, self.email))
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Malcolm', 'Anderson')
emp_3 = Employee('Joe', 'Evans')