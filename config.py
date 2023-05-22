import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xf5\xa2\x965\xed\x9d\xfbRV\xc4m\xe6Z\xa9>\x96'

    MONGODB_SETTINGS = { 'db' : 'SPS_Enrolment' }
