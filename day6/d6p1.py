class planet:
    def __init__(self, name=None, parent=None):
        self.name = name
        self.parent = None

    def get_parent(self):
        return self.parent if self.parent is not None else None


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
    for i in planets.values():
        parent = i.get_parent()
        while(parent is not None):
            number += 1
            parent = parent.get_parent()

    print(number)


if __name__ == "__main__":
    main()
