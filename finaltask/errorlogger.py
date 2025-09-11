from loggerstrategy import LoggerStrategy
import time


class ErrorLogger(LoggerStrategy):
    def log(self, message):
        print(f"[ERROR] {time.strftime('%H:%M:%S')}: {message}")