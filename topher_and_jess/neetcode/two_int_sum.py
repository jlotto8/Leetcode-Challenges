"""
Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000
"""
def two_sum_sorted(numbers):
        # Step 1: Initialize two pointers
        left = 0                      # Start of the array
        right = len(numbers) - 1     # End of the array

        # Step 2: Use a while loop to move the pointers
        while left < right:
            # Step 3: Calculate the sum of the two numbers
            current_sum = numbers[left] + numbers[right]

            # Step 4: Check if this sum is equal to the target
            if current_sum == target:
                # Found the correct pair, return their indices (1-indexed)
                return [left + 1, right + 1]

            # Step 5: If the sum is too small, move the left pointer right
            elif current_sum < target:
                left += 1

            # Step 6: If the sum is too big, move the right pointer left
            else:
                right -= 1

        # This line should never be reached because the problem guarantees one solution
        return []