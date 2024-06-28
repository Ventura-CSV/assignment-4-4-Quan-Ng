def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    for i in range(5):
        while True:
            try:
                num = int(input(f"Enter Value {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid Input")
                
    minval = numbers[0]
    maxval = numbers[0]
    
    for num in numbers[0:1]:
        if num < minval:
            minval = num
        if num > maxval:
            maxval = num
            
            
    

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
