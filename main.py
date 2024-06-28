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
                
            
            
    

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
