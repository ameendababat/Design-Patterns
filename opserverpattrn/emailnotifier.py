from observer import Observer


class EmailNotifier(Observer):
    
    def update(self, user, filename):
        
        print(f"Email sent to {user} confirming upload of {filename} \n")

    