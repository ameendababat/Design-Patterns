from observer import Observer


class DashboardUpdate(Observer):
    
    def update(self, user, filename):
        
        print(f"Dashboard updated for {user}\n")