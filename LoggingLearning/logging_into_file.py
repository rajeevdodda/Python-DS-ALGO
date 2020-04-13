import logging

logging.basicConfig(filename='simple_logging.log', level=logging.DEBUG)
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
# ==> The output will be the same as before, but the log file is no longer appended to,
# so the messages from earlier runs are lost.
logging.debug("It's a DEBUG log")
logging.info("It's a INFO log")
logging.warning("It's a WARNING log")
getattr()