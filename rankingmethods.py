import statistics

methodids = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14"
    ]

reversethese = [
    "2",
    "5"
    ]

def r_1(positions, size):
    runningtotal = 0
    for i in positions:
        if i < 10:
            runningtotal += [13, 10, 8, 7, 6, 5, 4, 3, 2][i - 1]
        elif i == size:
            runningtotal -= 1
    return runningtotal

def r_2(positions, size):
    return sum(positions)/len(positions)

def r_3(positions, size):
    runningtotal = 0
    for i in positions:
        if i <= 10:
            runningtotal += [12, 10, 8, 7, 6, 5, 4, 3, 2, 1][i - 1]
    return runningtotal

def r_4(positions, size):
    return positions.count(1)

def r_5(positions, size):
    return positions.count(size)

def r_6(positions, size):
    return sum([0.827 ** i for i in positions])

def r_7(positions, size):
    runningtotal = 0
    for i in positions:
        if i <= 3:
            runningtotal += [5, 3, 1][i - 1]
    return runningtotal

def r_8(positions, size):
    runningtotal = 0
    for i in positions:
        if i <= 3:
            runningtotal += [3, 2, 1][i - 1]
    return runningtotal

def r_9(positions, size):
    runningtotal = 0
    for i in positions:
        if i <= 5:
            runningtotal += [5, 4, 3, 2, 1][i - 1]
    return runningtotal


def r_10(positions, size):
    runningtotal = 0
    for i in positions:
        if i <= 10:
            runningtotal += [10, 9, 8, 7, 6, 5, 4, 3, 2, 1][i - 1]
    return runningtotal

def r_11(positions, size):
    return 100 * len([i for i in positions if i <= 10])/len(positions)

def r_12(positions, size):
    return statistics.stdev(positions)

def r_13(positions, size):
    runningtotal = 0
    for i in positions:
        if i <= 4:
            runningtotal += [13, 10, 7, 4][i - 1]
    return runningtotal

def r_14(positions, size):
    runningtotal = 0
    for i in positions:
        if i in ["", 3, 2, 1]:
            runningtotal += ["", 3, 2, 1].index(i)
        if size - i in ["", 2, 1, 0]:
            runningtotal -= ["", 2, 1, 0].index(size - i)
    return runningtotal
        

methods = [
    r_1,
    r_2,
    r_3,
    r_4,
    r_5,
    r_6,
    r_7,
    r_8,
    r_9,
    r_10,
    r_11,
    r_12,
    r_13,
    r_14
    ]

def usemethod(positions, size, method):
    p = 0
    p = methods[methodids.index(method)](positions, size)
    return p

description = """
r-1 | badvision points system (13, 10, 8-2, -1 for last)
r-2 | average placement
r-3 | eurovision points system (12, 10, 8-1)
r-4 | favorite count
r-5 | wooden spoon count
r-6 | modern eurovision jury ranking combination system
r-7 | 1964-1966 coting system (5, 3, 1)
r-8 | 1962 voting system (3-1)
r-9 | 1963 voting system (5-1)
r-10 | top 10 gets 10-1
r-11 | percentage of top 10s
r-12 | standard deviation
r-13 | fdcth voting system
r-14 | worsevision 1 voting system"""[1:]
