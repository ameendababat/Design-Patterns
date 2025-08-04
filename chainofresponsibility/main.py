from authhandler import AuthHandler
from ratelimithandler import RateLimitHandler
from virusscanhandler import VirusScanHandler


def build_validation_chain():
    return AuthHandler(RateLimitHandler(VirusScanHandler()))


def validate_request(req):
    chain = build_validation_chain()
    return chain.handle(req)


def main():
    """Allows an object to send a request to other objects without knowing who is going to handle it"""
    req1 = {"auth": True, "rate": 80, "content": "normal"}
    req2 = {"auth": True, "rate": 150, "content": "normal"}
    
    print(validate_request(req1))
    print(validate_request(req2))


if __name__ == "__main__":
    main()