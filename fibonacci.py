def fibonacci(terms):
    first = 0
    second = 1
    answer = 0
    
    for i in range(1, terms):
        answer = first + second;
        print(answer)
        first = second
        second = answer
        

fibonacci(1000)       



