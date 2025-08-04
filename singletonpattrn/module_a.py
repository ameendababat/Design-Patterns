from configuration import load_config


def run_a():
    config = load_config()
    print("Module A running with:", config["name"])