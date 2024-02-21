# Import the logging module
import logging

# Configure the basic settings for the logging module
# The basicConfig method sets up a simple, basic configuration for the logging module
logging.basicConfig(
    # Set the format of the log messages
    # The format string contains various placeholders that will be replaced with actual values when a log message is created
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',

    # Set the root logging level to INFO
    # This means that only messages with a level of INFO or higher will be logged
    level=logging.INFO,
)
