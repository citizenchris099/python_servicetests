import logging
import os

logger = logging.getLogger('testlogger')
fn = os.path.join(os.path.dirname(__file__), 'testlogs.log')
hdlr = logging.FileHandler(fn)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)