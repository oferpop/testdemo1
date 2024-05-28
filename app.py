# app.py

from tools.numbers.simp import add, subtract
from tools.numbers.comp import sumofdigits, ispal

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Sum of digits")
        print("4. Check if a number is a palindrome")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"The result of adding {a} and {b} is {add(a, b)}")

        elif choice == '2':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"The result of subtracting {b} from {a} is {subtract(a, b)}")

        elif choice == '3':
            n = int(input("Enter a number: "))
            print(f"The sum of the digits of {n} is {sumofdigits(n)}")

        elif choice == '4':
            n = int(input("Enter a number: "))
            if ispal(n):
                print(f"{n} is a palindrome")
            else:
                print(f"{n} is not a palindrome")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
