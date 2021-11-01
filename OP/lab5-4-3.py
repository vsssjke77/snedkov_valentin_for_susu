def entry():
    penny = int(input())
    return penny


def conversion(penny):
    rubles = penny // 100
    penny = penny % 100
    return rubles, penny


def record1(rubles):
    global r_penny, r_rubles
    if rubles != 0:
        e_r = rubles % 10
        d_r = rubles % 100 // 10
        if d_r != 1:
            if e_r == 1:
                r_rubles = 'РУБЛЬ'
            elif e_r == 2 or e_r == 3 or e_r == 4:
                r_rubles = 'РУБЛЯ'
            else:
                r_rubles = 'РУБЛЕЙ'
        elif d_r == 1:
            r_rubles = 'РУБЛЕЙ'
        if d_r == 2 and e_r == 0:
            r_rubles = 'РУБЛЕЙ'
    return r_rubles


def record2(penny):
    global r_penny
    if penny != 0:
        e_p = penny % 10
        d_p = penny % 100 // 10
        if d_p != 1:
            if e_p == 1:
                r_penny = 'КОПЕЙКА'
            elif e_p == 2 or e_p == 3 or e_p == 4:
                r_penny = 'КОПЕЙКИ'
            else:
                r_penny = 'КОПЕЕК'
        if d_p == 1:
            r_penny = 'КОПЕЕК'
        if d_p == 2 and e_p == 0:
            r_penny = 'КОПЕЕК'
        return r_penny


def main():
    penny = entry()
    rubles, penny = conversion(penny)
    r_rubles = record1(rubles)
    r_penny = record2(penny)
    if rubles != 0:
        print(f"{rubles} {r_rubles}")
    if penny != 0:
        print(f"{penny} {r_penny}")


r_rubles = ''
r_penny = ''
if __name__ == "__main__":
    main()