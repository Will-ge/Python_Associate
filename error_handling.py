"""
error handling outside function:
first check if input is a valid integer
then check if input is in the specified range
if both good, print the number; if not, continuously ask for inputs
"""

def read_int(prompt, min, max):
    assert prompt in range(min,max+1)
    return prompt

while True:
    try:
        prompt=int(input("Enter a number:"))
        print("the number is:",read_int(prompt,-10,10))
        break
    except ValueError:
        print("Error: wrong input")
    except:
        print("Error: the value is not within permitted range")

