print('P Q f')
for P in range(2):
    for Q in range(2):
        if bool(not P):
            f = not Q
            f = int(f)
            print(P, Q, f)