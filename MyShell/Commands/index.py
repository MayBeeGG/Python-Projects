class Command:
    name: str
    description: str

    def __init__(self, name: str, description: str,suggestions: list[str]) -> None:
        self.name = name
        self.description = description
        self.suggestions = suggestions # add suggestion logic

