class Solution:
    def solve(self, weights, values, capacity):
        res = 0
        # Create pairs of (weight, value) and sort them by value-to-weight ratio in descending order.
        sorted_items = sorted(zip(weights, values), key=lambda x: -x[1] / x[0])

        for pair in sorted_items:
            if not bool(capacity):
                break
            if pair[0] > capacity:
                # If the item can't be fully added, add a fraction of it based on capacity.
                res += int(pair[1] * (capacity / pair[0]))
                capacity = 0
            else:
                # If the entire item can be added, add it and subtract its weight from capacity.
                res += pair[1]
                capacity -= pair[0]

        return int(res)


ob = Solution()
weights = [6, 7, 3]
values = [110, 120, 2]
capacity = 10
print(ob.solve(weights, values, capacity))
