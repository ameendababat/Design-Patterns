from observer import Observer


class Logger(Observer):
    def update(self, user, filename):
        print(f"[LOG] {user} uploaded {filename}\n")