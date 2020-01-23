# Generates Primary Keys for each object in the database(animals, biomes, plants)

#no file that exists for uuid1
from uuid import uuid1


class Identifiable:

    def __init__(self):
      self.id = uuid1()
