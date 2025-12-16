import numpy as np
from dataclasses import dataclass

@dataclass
class Solution:
    grid: np.ndarray | None

    def count_adjacent(self, row: int, col: int) -> int:
        if self.grid[row, col] == 0:
            return 0
        count = 0
        # Check all 8 possible directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.grid.shape[0] and 0 <= c < self.grid.shape[1]:
                count += self.grid[r, c]
        if count > 3:
            return 0
        else:
            return 1

    def load_grid_from_file(self, file_path: str):
        with open(file_path) as f:
            self.grid = np.array([[1 if c == '@' else 0 for c in line.strip()] 
                              for line in f])

    def run(self):
        total = 0
        for i,value in np.ndenumerate(self.grid):
            total+=self.count_adjacent(i[0],i[1])
        return total
        




def main():
    solution = Solution(grid=None)
    solution.load_grid_from_file("data/d4.txt")
    print(solution.grid)
    result = solution.run()
    print(f"Result: {result}")


if __name__ == "__main__":
    main()