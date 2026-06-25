class Planet():
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str):
            raise TypeError("name, planet type, and star must be strings")