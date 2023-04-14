import random

winningnumbers = []
stat ={}

def dict():
    for i in range(1, 46):
        stats[i]=0

def lotto():
    numbers = [*range(1,46, 1)]
    winningnumbers.clear()
    for i in range(6):
        rnumber = random.choice(numbers)
        winningnumbers.append(rnumber)
        numbers.remove(rnumber)
    return winningnumbers

def stats():
    for i in range(100):
        numbers = lotto()
        for a in range(6):
            for key, value in stat.items():
                if numbers[a] == key:
                    stat[key] = stat[key] + 1
    return stat

def main():
    dict()
    print("Lottoziehung " + str(lotto()))
    print("Statistik für 100 Mal: " + str(stats()))

if __name__ == '__main__':
    main()
