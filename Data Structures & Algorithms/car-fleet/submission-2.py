class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [0] * len(speed)
        for i in range(len(speed)):
            mins = (target - position[i]) / speed[i]
            arr[i] = (position[i], speed[i], mins)
        
        arr.sort()
        arr.reverse()

        stack = []
        for n in arr:
            if len(stack) == 0:
                stack.append(n)
            elif (n[2] > stack[-1][2] or 
                (n[2] == stack[-1][2] and n[1] <= stack[-1][1])):
                stack.append(n)
        
        for n in arr:
            print("arr: ", n)
        
        for n in stack:
            print("stack: ", n)

        return len(stack)
                