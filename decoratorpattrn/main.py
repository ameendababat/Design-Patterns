from authdecorator import AuthDecorator
from ratelimitdecorator import RateLimitDecorator
from loggingdecorator import LoggingDecorator 
from corehandler import CoreHandler

def main():
    """Allows behavior to be added to individual objects dynamically
        without affecting the behavior of other objects from the same class
    """
    handler = AuthDecorator(RateLimitDecorator(LoggingDecorator(CoreHandler()))) 
    handler.handle_request()



if __name__ == "__main__":
    main()