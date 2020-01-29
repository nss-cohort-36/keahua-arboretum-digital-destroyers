# Generates Primary Keys for each object in the database(animals, biomes, plants)

import uuid


class Identifiable:

    def __init__(self):
      self.id = uuid.uuid1()

