import copy


def entry():
    f = open("input.txt", 'r')
    i = f.readlines()
    M, N = list(map(int, i[0].split()))
    X, Y = list(map(int, i[1].split()))
    f.close()
    return M, N, X, Y


def start(M, N, X, Y):
    matrix = [[0 for _ in range(N)] for _ in range(M)]
    matrix[X][Y] = 1
    actions(M, N, X, Y, matrix, 1)
    return matrix


def actions(M, N, X, Y, map, k):
    map[X][Y] = k
    if k == N ** 2:
        return True
    ways = way(M, N, X, Y, map)
    if len(ways) == 0:
        return 'Не может быть'
    values = []
    for new_position in ways:
        map_test = copy.deepcopy(map)
        values.append((len(way(M, N, new_position[0], new_position[1], map_test)), new_position))
    values.sort()
    position = values[0][1]
    actions(M, N, position[0], position[1], map, k + 1)


def way(M, N, X, Y, map):
    acceptable_moves = [(X + 1, Y + 2), (X + 2, Y - 1), (X + 1, Y - 2), (X + 2, Y + 1), (X - 1, Y + 2), (X - 2, Y + 1),
                        (X - 1, Y - 2), (X - 2, Y - 1)]
    for i in range(len(acceptable_moves)):
        move = acceptable_moves[i]
        if (0 <= move[0] < M and 0 <= move[1] < N) and map[move[0]][move[1]] == 0:
            pass
        else:
            acceptable_moves[i] = ()
    while () in acceptable_moves:
        acceptable_moves.remove(())
    return acceptable_moves


def output(array):
    f = open("output.txt", 'w')
    for i in range(len(array) - 1, -1, -1):
        for j in range(len(array[i])):
            f.write(f"{array[i][j]:4}", )
        f.write('\n')
    f.close()


def output_else(answer):
    f = open("output.txt", "w")
    f.write(answer)
    f.close()


def main():
    M, N, X, Y = entry()
    answer = start(M, N, X - 1, Y - 1)
    flag = True
    for i in answer:
        if 0 in i:
            flag = False
            break
    if flag:
        output(answer)
    else:
        answer = 'Маршрут не найден'
        output_else(answer)


if __name__ == "__main__":
    main()
