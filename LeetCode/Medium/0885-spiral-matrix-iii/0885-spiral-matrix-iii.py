class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0 
        steps = 1 
        current_steps = 0
        change_direction_count = 0 
        total_steps = 0
        result = []

        r, c = rStart, cStart
        result.append([r, c])
        total_steps += 1

        while total_steps < rows * cols:
            r += directions[current_direction][0]
            c += directions[current_direction][1]
            current_steps += 1

            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
                total_steps += 1

            if current_steps == steps:
                current_steps = 0
                current_direction = (current_direction + 1) % 4
                change_direction_count += 1

                if change_direction_count % 2 == 0:
                    steps += 1

        return result