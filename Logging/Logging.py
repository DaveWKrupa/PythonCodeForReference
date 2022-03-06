# https://docs.python.org/3/library/logging.html
import logging
# for basic configuration information
# https://docs.python.org/3/library/logging.html?highlight=basicconfig#logging.basicConfig
# this both sets the config for the DEBUG logger and also forces it to print
# otherwise only warning, error and critical print
# this sets config for DEBUG and above
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')


# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")


# handlers for logging can be created as follows
logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('logfile.log')

# level and format
stream_h.setLevel(logging.WARNING)  # logs warnings and above
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)


# now trigger the logging actions

# logger.warning("This is a warning")
# logger.error("This is an error")
#
# __main__ - WARNING - This is a warning
# 03/01/2022 17:21:21 - __main__ - WARNING - This is a warning
# __main__ - ERROR - This is an error
# 03/01/2022 17:21:21 - __main__ - ERROR - This is an error


# for stack trace
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

# 03/01/2022 17:23:38 - root - ERROR - list index out of range
# Traceback (most recent call last):
#   File "C:\Users\dave_\PycharmProjects\SimplePyCharmTests\Logging.py", line 52, in <module>
#     val = a[4]
# IndexError: list index out of range