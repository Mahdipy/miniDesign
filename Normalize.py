class ToGribach:
    test = 'abcdefghijklmnopqrstuvwxyz'
    c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

    def landa_normalize(self, rules):
        for g in rules:
            if '?' in g:
                g.remove('?')
                for x in rules:
                    for i in range(1, len(x)):
                        if g[0] in x[i]:
                            x.append(x[i].replace(g[0], ''))
        # print(f'?: {rules}')
        return rules

    def unit_normalize(self, rules):
        for g in rules:
            for a in rules:
                for i in range(1, len(a)):
                    if g[0] == a[i]:
                        a.remove(a[i])
                        for l in range(1, len(g)):
                            if g[l] != a[0]:
                                a.append(g[l])
        # print(f'Unit: {rules}')
        return rules

    def useless_normalize(self, rules, captal, small):
        return self.useless_normalize2(self.useless_normalize1(rules, captal, small), captal)

    def useless_normalize1(self, rules, captal, test):
        x = []
        for g in rules:
            for i in range(1, len(g)):
                if g[i].islower():
                    x.append(g[0])
                    test += g[0]
                    break
        # print(x)
        for g in rules:
            for i in range(1, len(g)):
                if not set(g[i]).difference(test):
                    x.append(g[0])
                    test += g[0]
                    break
        # print(x)
        x = list(set(x))
        for g in rules:
            z = g[0]
            if z not in x:
                # print(z)
                rules.remove(g)
        for l in rules:
            for i in l:
                if set(i).difference(test):
                    l.remove(i)
        # print(f'Useless1 : {rules}')
        return rules

    def useless_normalize2(self, rules, captal):
        x = [rules[0][0]]
        i = 0
        while (i != len(x)):
            for g in rules:
                if x[i] == g[0]:
                    for j in range(1, len(g)):
                        for l in captal:
                            if l in g[j]:
                                x.append(l)
                                x = list(set(x))
            i += 1
        for g in rules:
            if g[0] not in x:
                rules.remove(g)
        # print(f'Useless2: {rules}')
        return rules

    def remove_dr(self, rules):
        x = []
        y = []
        for g in rules:
            for i in range(1, len(g)):
                if g[i][0] == g[0]:
                    x.append(g[i])
            if len(x) > 0:
                for l in x:
                    for i in g:
                        if l == i:
                            y.append(i[1:])
                            g.remove(i)
                y.insert(0, 'X')
                for i in range(1, len(g)):
                    g.append(g[i] + 'X')
                for i in range(1, len(y)):
                    y.append(y[i] + 'X')
                if len(g) == 1:
                    rules.remove(g)
                rules.append(y)
            x = []
            y = []
        # print(f'Left: {rules}')
        return rules

    def gribach(self, rules):
        rules = self.landa_normalize(rules)
        rules = self.unit_normalize(rules)
        rules = self.useless_normalize1(rules, self.c, self.test)
        rules = self.useless_normalize2(rules, self.c)
        rules = self.remove_dr(rules)
        a = True
        while a:
            a = False
            for g in rules:
                for i in range(1, len(g)):
                    if g[i][0].isupper() and g[i][0] != g[0]:
                        a = True
                        z = g[i][1:]
                        for j in rules:
                            if g[i][0] == j[0]:
                                for k in range(1, len(j)):
                                    g.append(j[k] + z)
                        g.remove(g[i])
                    elif g[i][0].isupper() and g[i][0] == g[0]:
                        rules = self.remove_dr(rules)

        print(rules)


test = 'abcdefghijklmnopqrstuvwxyz'
c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
     'W', 'X', 'Y', 'Z']
rule = []

a = input('Enter your cfg (use ? as landa and finish grammar by typing end):\n')

while a != 'end':
    b = a.replace('->', '|')
    a = input()
    rule.append(b.split('|'))
m = ToGribach()
m.gribach(rule)
