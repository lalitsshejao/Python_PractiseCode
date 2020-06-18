'''
Create a log file in current working directory and write WARNING and higher level messages (i.e. WARNING, ERROR, CRITICAL)
By default logging level is WARNING
'''
import logging
logging.basicConfig(filename="log.txt", format='%(asctime)s : %(message)s', level=logging.WARNING, datefmt='%m/%d/%Y %I:%M:%S %p')
print("Logging Demo")
logging.debug("This is debug Message")
logging.info("This is info Message")
logging.warning("This is warning Message")
logging.error("This is error Message")
logging.critical("This is critical Message")