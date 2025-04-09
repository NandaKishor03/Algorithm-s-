def trap(self, height: List[int]) -> int:
    N = len(height)
    if N == 0:
        return 0

    # Arrays to store the max height to the left and right of each index
    left = [0] * N
    right = [0] * N

    # Initialize the first value of left max and last value of right max
    left[0] = height[0]
    right[N - 1] = height[N - 1]

    # Fill the left max array
    for i in range(1, N):
        left[i] = max(left[i - 1], height[i])

    # Fill the right max array
    for i in range(N - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    # Calculate the trapped water at each index
    total_water = 0
    for i in range(N):
        water_at_i = min(left[i], right[i]) - height[i]
        total_water += water_at_i

    return total_water

# Example usage
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Trapped water:", trap(height))  # Output: 6



# Step 1: Build left[] array:
# Stores max height from the left up to each index:
# left =  [0,1,1,2,2,2,2,3,3,3,3,3]

# Step 2: Build right[] array:
# Stores max height from the right up to each index:
# right = [3,3,3,3,3,3,3,3,2,2,2,1]

# Step 3: Calculate Water at Each Index:
# For each index i, water trapped = min(left[i], right[i]) - height[i]
# Add this value to total_water