from loggerstrategy import LoggerStrategy
import time


class InfoLogger(LoggerStrategy):
    
    def log(self, message):
        print(f"[INFO] {time.strftime('%H:%M:%S')}: {message}")