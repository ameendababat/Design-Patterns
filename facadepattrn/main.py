from datafacade import DataFacade


def main():
    """Hides the internal details of the system
    Clients become less reliant on the internal workings and complex
    """
    data = DataFacade()
    data.get_cache(200)
    data.get_db("students")
    data.get_api()


if __name__ == "__main__":
    main()