# defines the Arboretum class object 
class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = []
        self.grasslands = []

    

    # def list_instructors(self): 
    # for instructor in self.instructors:
    #     print(instructor.firstName)

    # def listRivers(self):
    #     for river in self.rivers:
    #         # return f"string interp{river}"
    #         return river

    def listRivers(self):
        for river in self.rivers:
            return f"{river}"
            # return river

        # TODO: missing forest, swamp, mountains
