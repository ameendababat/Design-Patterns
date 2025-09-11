from configuration import Configuration


def run_b():
    config = Configuration.load_config()
    print("Module B running with:", config["name"])