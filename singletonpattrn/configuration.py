import json 


class Configuration:
    __instance = None
    __config_data = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Configuration, cls).__new__(cls)
            with open("config.json", "r") as f:
                print("Loading config…")
                cls.__config_data =  json.load(f)
        return cls.__instance    


    def __init__(self):
        pass


    def get_config(self):
        return self.__config_data


    @staticmethod
    def load_config():
        return Configuration().get_config()