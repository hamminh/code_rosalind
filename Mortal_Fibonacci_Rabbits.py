# https://math.stackexchange.com/questions/511565/fibonacci-with-mortal-bunnies
# List the number of rabbits alive for each month
def fib(passed_month:int, max_age:int, mature_month:int = 2):
    current_generation = [1] + [0] * (max_age-1)
    for i in range(passed_month-1):
        current_generation = [sum(current_generation[mature_month-1:])] + current_generation[:-1]
    return(current_generation)

print(fib(6,3))
print(sum(fib(6,3)))