import logging
import sys

logging.basicConfig(filename='logging.log',filemode='w',level=logging.DEBUG,format='%(asctime)s %(message)s')

logger = logging.getLogger()


logger.setLevel(logging.DEBUG)


logger.debug('Added different types')

logger.info('Everything working fine')

logger.warning('Don\'t use class with no initializer')

#logger.exception('divide by zero')

logger.error('Internet is not connected')

logger.log(logging.ERROR,'divide by zero')

logger.critical('Service is shut down')


def error_msg():
    return '{0} is caused as {1} on line {2}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno)


try:
   x = 1/0

except Exception as e :
    logger.log(logging.ERROR,error_msg())
