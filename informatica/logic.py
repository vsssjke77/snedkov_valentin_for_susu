print('a b c f1 f2 f3 f4 f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = int(not ((a or not b) and c) or (a == b))   # под импликацией можно использовать знак <=, вместо not до((a or not b) and c) и or после
            f1 = int(not b)
            f2 = int(a or not b)
            f3 = int(((a or not b) and c))
            f4 = int(a == b)
            print(a, b, c, f1, f2, f3, f4, f)