from observer import Observer

class Subject:
    
    def add_subscribers(self, observer:Observer):pass
    def remove_subscribers(self, observer:Observer):pass
    def notify_subscribers(self, user,filename):pass
    