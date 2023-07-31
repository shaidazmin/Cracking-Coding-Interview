#Assignment on Introduction


class CalculateSum:
    def sum_of_natural_numbers(n):
        total_sum = 0
        for i in range(1, n + 1):
            total_sum += i
        return total_sum
    
print(CalculateSum.sum_of_natural_numbers(int(input("Give an integer: "))))    

# Time Complexity: O(n)
# Space Complexity: O(1)