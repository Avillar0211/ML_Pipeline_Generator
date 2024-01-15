import os

class prueba:
    def __init__(self):
        self.cwd = os.getcwd()

    def muestra(self):
        print(self.cwd)
