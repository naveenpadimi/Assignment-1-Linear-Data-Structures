# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?


def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = list(map(int, input("Enter an array of integers separated by space: ").split()))
target_sum = int(input("Enter the target sum: "))
pairs = find_pairs(arr, target_sum)
print(pairs)

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.


def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


arr = list(map(int, input("Enter an array of integers separated by space: ").split()))
reverse_array(arr)
print("The reversed Array : ",arr)  

# Q3. Write a program to check if two strings are a rotation of each other?

def is_rotation(string1, string2):
    if len(string1) != len(string2):
        print("error ! Please Enter the same length of strings! ")
    else:
        sorted(string1) == sorted(string2)
        return True


string1 = "waterbottle"
string2 = "erbottlewat"
result = is_rotation(string1, string2)
print(result)  

# Q4. Write a program to print the first non-repeated character from a string?


def first_non_repeated_char(string):
    
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    
    for char in string:
        if char_count[char] == 1:
            return char
    return None

string = str(input("Enter the Characters :"))
result = first_non_repeated_char(string)
if result:
    print("The first non-repeated character is:", result)
else:
    print("There are no non-repeated characters in the string")

# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# Q6. Write a program to convert prefix expression to infix expression.

def prefix_to_infix(prefix_expr):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for i in range(len(prefix_expr)-1, -1, -1):
        if prefix_expr[i] in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append('(' + op1 + prefix_expr[i] + op2 + ')')
        else:
            stack.append(prefix_expr[i])

    return stack.pop()


prefix_expr = '*+AB-CD'
infix_expr = prefix_to_infix(prefix_expr)
print(infix_expr) 


# Q7. Write a program to check if all the brackets are closed in a given code snippet.
def check_brackets(code):
    stack = []
    for char in code:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    return not stack

code =input("Enter the brackets with space :") 
if check_brackets(code):
    print("All brackets are closed.")
else:
    print("Brackets are not closed.")

# Q8. Write a program to reverse a stack.

def reverse_stack(stack):
    aux_stack = []
    while stack:
        aux_stack.append(stack.pop())
    while aux_stack:
        stack.append(aux_stack.pop())

# example usage
stack = []
lst = list(map(int, input("Enter an array of integers separated by space: ").split()))
stack.append(lst)
print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)

# Q9. Write a program to find the smallest number using a stack.


class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

s = Stack()

numbers = input("Enter some numbers separated by spaces: ")

numbers = list(map(int, numbers.split()))


for number in numbers:
    s.push(number)


smallest = s.pop()

while not s.is_empty():
    number = s.pop()
    if number < smallest:
        smallest = number

print("The smallest number is:", smallest)

 