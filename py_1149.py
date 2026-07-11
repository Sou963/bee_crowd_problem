def main():
    values = list(map(int, input().split())) 
    A = values[0]
    N = 0
    for i in range(1, len(values)):
        if values[i] > 0:
            N = values[i]
            break
            
    total_sum = sum(range(A, A + N))
    print(total_sum)

if __name__ == "__main__":
    main()