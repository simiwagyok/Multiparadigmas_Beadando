from functools import reduce
from typing import List
from .schemas import AutoJobResponse

def szamol_bevetel(munkak: List[AutoJobResponse]) -> float:
    kesz_munkak = filter(lambda x: x.statusz == "Kész", munkak)
    arak = map(lambda x: x.ar, kesz_munkak)
    return reduce(lambda a, b: a + b, arak, 0.0)

def szamol_statusz(munkak: List[AutoJobResponse]) -> dict:
    return {
        "Várakozás": len([x for x in munkak if x.statusz == "Várakozás"]),
        "Mosás": len([x for x in munkak if x.statusz == "Mosás"]),
        "Kész": len([x for x in munkak if x.statusz == "Kész"]),
    }
