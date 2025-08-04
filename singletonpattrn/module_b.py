from configuration import load_config


def run_b():
    config = load_config()
    print("Module B running with:", config["name"])