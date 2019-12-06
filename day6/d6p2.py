class planet:
    def __init__(self, name=None, parent=None):
        self.name = name
        self.parent = None

    def get_parent(self):
        return self.parent if self.parent is not None else None

    def __repr__(self):
        return self.name


def read_file():
    with open('input.txt', 'r') as f:
        return f.read()


def main():
    inp = [item.split(')') for item in read_file().split('\n')]
    planets = {'COM': planet(name='COM')}
    for i in inp:
        if (i[1] not in planets.keys()):
            planets.update({i[1]: planet(name=i[1])})

    for i in inp:
        planets[i[1]].parent = planets[i[0]]

    number = 0
    you_parents = []
    san_parents = []
    for i in planets.values():
        parent = i.get_parent()
        while(parent is not None):
            if i.name == 'YOU':
                you_parents.append(parent)
            elif i.name == 'SAN':
                san_parents.append(parent)
            number += 1
            parent = parent.get_parent()

    match = None
    transfer = 0
    for you_index, you_pos in enumerate(you_parents):
        for san_index, san_pos in enumerate(san_parents):
            if you_pos == san_pos and match is None:
                transfer = you_index + san_index
                match = you_pos

    print("Transfer:", transfer)
    print("Match Planet:", match)


if __name__ == "__main__":
    main()
