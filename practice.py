def sum(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

while True:
    print("1. ADD")
    print("2. SUB")
    print("3. MULTI")
    print("x. EXIT")
    choice = input("Enter your choice (1/2/3/x): ")
    
    if choice == 'x':
        print("Exiting...")
        break
    
    if choice in ['1', '2', '3']:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        
        if choice == '1':
            result = sum(n1, n2)
            print("Sum:", result)
        elif choice == '2':
            result = sub(n1, n2)
            print("Difference:", result)
        elif choice == '3':
            result = multi(n1, n2)
            print("Product:", result)
    else:
        print("Invalid choice, please try again.")
