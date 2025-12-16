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

def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping or adjacent ranges"""
    if not ranges:
        return []
    
    merged = [ranges[0]]
    
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        
        # If current range overlaps or is adjacent to last merged range
        if start <= last_end + 1:
            # Extend the last range
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged.append((start, end))
    
    return merged


def main():
    # ids = load_and_sort_ids("data/d5id.txt")
    ranges = load_and_sort_ranges("data/d5rt.txt")

    # part 1
    # res = 0
    # for id in ids:
    #     for start, end in ranges:
    #         if start <= id <= end:
    #             print(f"ID {id} is within range {start}-{end}")
    #             res += 1
    #             break
    #         elif id < start:
    #             break

    # print(f"Total IDs within ranges: {res}")
    ranges = load_and_sort_ranges("data/d5r.txt")

    # Part 2: Merge overlapping ranges and count total IDs
    merged = merge_ranges(ranges)
    
    total = 0
    for start, end in merged:
        total += (end - start + 1)  # +1 because ranges are inclusive
    
    print(f"Total fresh IDs: {total}")

    print(f"Total covered length: {total}")
if __name__ == "__main__":
    main()

