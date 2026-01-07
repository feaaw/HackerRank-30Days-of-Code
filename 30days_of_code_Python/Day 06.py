# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = int(input())

for i in range(test_case):
    test_string = input()
    even_indexed = ''
    odd_indexed = ''
     
    for j in range(len(test_string)):
        if j % 2 == 0:
            even_indexed += test_string[j]
        else:
            odd_indexed += test_string[j]
    print(even_indexed, odd_indexed)
