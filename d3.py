def main():
    with open("data/d3.txt") as f:
        lines = f.readlines()

    res = 0
    for line in lines:
        bank = line.strip()

        # First Battery
        b1 = '1'
        b1index = 0
        for i in range(len(bank)-1):
            if bank[i]>b1:
                b1 = bank[i]
                b1index = i
                if b1 == '9':
                    break

        # Second Battery
        b2 = '1'
        for i in range(1,len(bank)):
            if bank[i]>b2 and i>b1index:
                b2 = bank[i]
                if b2 == '9':
                    break

        label = f"{b1}{b2}"
        # print(label)
        res += int(label)

    print(res)



if __name__ == "__main__":
    main()