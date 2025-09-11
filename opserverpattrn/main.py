from system import System
from emailnotifier import EmailNotifier
from logger import Logger
from dashboardupdate import DashboardUpdate


def upload_file(user, filename, event_manager:System):
    print(f"{user} uploaded {filename} \n")
    event_manager.notify_subscribers(user, filename)


def main():
    """
    one to many between objects
    Need one object to notify multiple others about changes
    """
    manager = System()
    manager.add_subscribers(EmailNotifier())
    manager.add_subscribers(Logger())
    manager.add_subscribers(DashboardUpdate())
    upload_file("ameen", "report.pdf", manager)


if __name__ == "__main__":
    main()