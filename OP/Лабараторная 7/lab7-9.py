def entry():
    f = open("input.txt","r")
    word = f.readline()
    f.close()
    return word


def actions(entry_word):
    if len(entry_word) != 0:
        return actions(entry_word[1:]) + entry_word[0]
    else:
        return ''


def output(final_word):
    f = open("output.txt","w")
    f.write(final_word)


def main():
    entry_word = entry()
    final_word = actions(entry_word)
    output(final_word)


if __name__ == "__main__":
    main()
