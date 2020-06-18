'''
Create a log file in current working directory and write WARNING and higher level messages (i.e. WARNING, ERROR, CRITICAL)
By default logging level is WARNING
'''
import logging
logging.basicConfig(filename="log.txt", datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.WARNING)
print("Exception Logging Demo")
logging.info("A New request came")
try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("can not device by zero")
    logging.exception(msg)
except ValueError as msg:
    print("Enter only integer value")
    logging.exception(msg)
logging.info("Request Processed")