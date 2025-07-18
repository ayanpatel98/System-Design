from ExternalButton import ExternalButton

class Floor:
    def __init__(self, number: int):
        self.number = number
        self.externalButton = ExternalButton(number)