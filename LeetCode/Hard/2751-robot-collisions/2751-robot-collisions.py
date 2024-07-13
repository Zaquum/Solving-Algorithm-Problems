class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []

        for pos, health, direction, idx in robots:
            if direction == 'R':
                stack.append((pos, health, direction, idx))
            else:
                while stack and stack[-1][2] == 'R':
                    r_pos, r_health, r_direction, r_idx = stack.pop()
                    if r_health > health:
                        r_health -= 1
                        stack.append((r_pos, r_health, r_direction, r_idx))
                        health = 0
                        break
                    elif r_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                if health > 0:
                    stack.append((pos, health, direction, idx))


        surviving_robots = sorted(stack, key=lambda x: x[3])
        result = [health for _, health, _, _ in surviving_robots]
        return result