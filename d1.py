def dial_to_number(turn: str):
    sgn = 1 if turn[0]=="R" else -1
    value = int(turn[1:].strip())
    return sgn*value

def main():
    with open("data/d1.txt") as f:
        lines = f.readlines()
    total = 50
    pwd = 0
    for line in lines:
        total += dial_to_number(line)
        total = total % 100
        if total == 0:
            pwd+=1
    print(pwd)

if __name__=="__main__":
    main()