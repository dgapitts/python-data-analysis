import timeit
# creating array within the sum() function call implicitly - apparently a more efficient form - save Memory and CPU !?
code_format1 = """
for j in range(10000):
    sum(i**2 for i in range(10))
"""
code_format2 = """
for j in range(10000):
    sum([i**2 for i in range(10)])
"""
elapsed_time = timeit.timeit(code_format1, number=100)/100
print(elapsed_time)
elapsed_time = timeit.timeit(code_format2, number=100)/100
print(elapsed_time)


