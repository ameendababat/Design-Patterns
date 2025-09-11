from loggerstrategy import LoggerStrategy
import time


class DebugLogger(LoggerStrategy):
    def log(self, message):
        print(f"[DEBUG] {time.strftime('%H:%M:%S')}: {message}")