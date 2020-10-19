class Dictionary:
    def __init__(self):
        self.items = 0
        self.n = 10
        self.values = [[] for _ in range(self.n)]

    def get(self, key):
        idx = hash(key)%self.n
        vals = self.values[idx]
        for val in vals:
            if val[0] == key:
                return val[1]
        raise KeyError(key)

    def put(self, key, value, doubling=False):
        if not doubling and self.items + 1 > self.n * .8:
            self.double_size()

        idx = hash(key)%self.n
        vals = self.values[idx]
        in_list = None
        for val in vals:
            if val[0] == key:
                in_list = val
        if in_list is not None:
            vals.remove(in_list)
        vals.append((key, value))
        if not doubling:
            self.items += 1

    def delete(self, key):
        idx = hash(key)%self.n
        vals = self.values[idx]
        in_list = None
        for val in vals:
            if val[0] == key:
                in_list = val
        if in_list is None:
            raise KeyError(key)
        vals.remove(in_list)
        self.items -= 1

    def double_size(self):
        old_n = self.n
        old_values = self.values

        self.n = self.n * 2
        self.values = [[] for _ in range(self.n)]

        for val_list in old_values:
            for val in val_list:
                self.put(val[0], val[1], True)

    def __repr__(self):
        return str(self.values)
