class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            while stack and stack[-1] > 0 and x < 0:
                if stack[-1] < -x:
                    stack.pop()
                    continue
                elif stack[-1] == -x:
                    stack.pop()
                break
            else:
                stack.append(x)

        return stack