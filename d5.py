def load_and_sort_ids(file_path: str) -> list[int]:
    with open(file_path) as f:
        ids = [int(line.strip()) for line in f]
    return sorted(ids)

def load_and_sort_ranges(file_path: str) -> list[tuple[int, int]]:
    with open(file_path) as f:
        ranges = []
        for line in f:
            start, end = map(int, line.strip().split('-'))
            ranges.append((start, end))
    return sorted(ranges, key=lambda x: x[0])

def main():
    ids = load_and_sort_ids("data/d5id.txt")
    ranges = load_and_sort_ranges("data/d5r.txt")

    res = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                print(f"ID {id} is within range {start}-{end}")
                res += 1
                break
            elif id < start:
                break

    print(f"Total IDs within ranges: {res}")


if __name__ == "__main__":
    main()

