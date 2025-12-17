from typing import NamedTuple

Minion=NamedTuple("Minion",[("name",str),
                            ("hunger",int),
                            ("motivation",int),
                            ("size",str)])

def line_to_minion(line:str)->Minion:
    data=line.strip("\n").split(";")
    return Minion(data[0],int(data[1]),int(data[2]),data[3])

minion=line_to_minion("Bob;13;79;XL")
def minion_to_line(line:(minion))->str:
    #return f"{minion.name} {minion.hunger} {minion.size}"
    return "{0} {1} {2}".format(minion.name, minion.hunger, minion.size)

def sort_minions(minions):
    minions.sort(key=lambda minion:
    (-minion.motivation, minion.name))

    return minions