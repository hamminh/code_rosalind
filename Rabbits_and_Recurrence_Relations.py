def rabbit_pairs(n, k):
    # Initialize variables for the first two months
    prev_month = 1
    current_month = 1

    # Iterate over remaining months
    for i in range(2, n):
        # Calculate the number of rabbit pairs in the current month
        new_pairs = prev_month * k
        total_pairs = current_month + new_pairs

        # Update variables for the next iteration
        prev_month = current_month
        current_month = total_pairs

    return current_month

#input
n = 5
k = 3
result = rabbit_pairs(n, k)
print(result)
