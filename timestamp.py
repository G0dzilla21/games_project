# -*- coding: utf-8 -*-

'''
This function will fetch the timestamp in the correct format and return it
'''
def timestamp():
    from datetime import datetime
    # datetime object containing current date and time
    now = datetime.now()
    # mm/dd/YY H:M:S
    timestamp = now.strftime("%m/%d/%Y %H:%M:%S")
    return timestamp;
