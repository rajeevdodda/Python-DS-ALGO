import logging
from LoggingLearning import mylib


def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='myapp.log', filemode='w', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished, %s', "mylib done")


if __name__ == '__main__':
    main()
