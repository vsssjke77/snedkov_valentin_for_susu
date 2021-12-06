def entry():
    f = open("input.txt", "r")
    line = f.readline()
    f.close()
    return line


def actions(line, a):
    if line[0] == '{' or line[0] == '[' or line[0] == '<' or line[0] == '(' or line[0] == '}' or line[0] == ']' or \
            line[0] == '>' or line[0] == ')':
        if line[0] == '{' or line[0] == '[' or line[0] == '<' or line[0] == '(':
            a = a + line[0]
            return actions(line[1:], a)
        else:
            if line[0] == ')' and a[-1] == '(' or line[0] == '}' and a[-1] == '{' or line[0] == ']' and a[-1] == '[' or \
                    line[0] == '>' and a[-1] == '<':
                a = a[0:-1]
                return actions(line[1:], a)
            else:
                return actions('NO', a)
    elif line[0] == '.':
        return 'YES'
    else:
        return 'NO'


def output(result):
    f = open("output.txt", 'w')
    f.write(result)
    f.close()


def main():
    line = entry()
    result = actions(line, a='')
    output(result)


if __name__ == "__main__":
    main()
