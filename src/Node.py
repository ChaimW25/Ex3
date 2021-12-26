class Node:

    def __init__(self, id: int, pos: tuple = None):
        self.pos = pos
        self.id = id
        self.weight: float = 0
        self.tag: int = 0
        self.info: str = ""

    def getId(self) -> int:
        return self.id

    def getPos(self) -> tuple:
        return self.pos

    def setPos(self, pos: tuple):
        self.pos = pos

    def getWeight(self) -> float:
        return self.weight

    def setWeight(self, weight: float):
        self.weight = weight

    def getInfo(self) -> str:
        return self.info

    def setInfo(self, info: str):
        self.info = info

    def getTag(self) -> int:
        return self.tag

    def setTag(self, tag: int):
        self.tag = tag

    def __lt__(self, node):
        return self.weight < node.weight

    def __str__(self) -> str:
        return "{key: " + str(self.id) + ", " + "pos: " + str(self.pos) + "}"

    def __repr__(self) -> str:
        return "{key: " + str(self.id) + ", " + "pos: " + str(self.pos) + "}"