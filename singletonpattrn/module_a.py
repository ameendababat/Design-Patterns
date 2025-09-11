from configuration import Configuration


def run_a():
    config = Configuration.load_config()
    print("Module A running with:", config["name"])