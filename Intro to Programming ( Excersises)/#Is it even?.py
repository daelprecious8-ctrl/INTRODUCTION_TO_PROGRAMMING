#Is it even?
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
   
    num = int(input("Please enter a number: "))
    
   
    result = check_even_odd(num)
    
    
    print(result)


if __name__ == "__main__":
    main()