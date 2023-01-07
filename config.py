import os

class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_server"
    #secret_server stands for a very long string which can be used to encryp
    #any string which can be like "helloartemisiwanttogotothemoon"
    #secret_key is used so that the hackers cannot hack or use the data inside the server