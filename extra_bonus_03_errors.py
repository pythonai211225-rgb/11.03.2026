
#######################################################
#######################################################
####################### BONUS
#######################################################
#######################################################

# ADVANCED CODE , beware!

import logging

class OutOfPitaError(Exception):
    """The kitchen is officially flat out of bread."""
    pass

pita = 0

logging.basicConfig(filename='restaurant.log',
                    level=logging.DEBUG, format='[%(asctime)s]  %(levelname)s: %(message)s',
                    datefmt='%d-%m-%Y %H:%M',)

def kitchen(order: str):
    logging.info(f'kitchen got order of {order}')
    if order == 'humus':
        if pita == 0:
            logging.error(f"Kitchen ran out of dough for Pita")
            raise OutOfPitaError(f"Kitchen ran out of dough for Pita")
    print ("new humus is ready...")

def kitchen_manager(order: str):
    logging.info(f'kitchen_manager got order of {order}')
    print("manager passing order")
    kitchen(order)
    # try:
    #     kitchen(order)
    # except:
    #     print('no pita you are getting hamburger')


def waiter(order: str):
    logging.info(f'waiter got order of {order}')
    print("waiter passing order")
    kitchen_manager(order)

try:
    waiter('humus')
except:
    print('unknown error code 553. contact support')
