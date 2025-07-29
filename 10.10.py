'''(Reverse a list) The reverse function in Section 10.8 reverses a list by copying it
to a new list. Rewrite the function that reverses the list passed in the argument and
returns this list. Write a test program that prompts the user to enter a list of num-
bers, invokes the function to reverse the numbers, and displays the numbers.'''

def reverse(list):
    list.reverse()
    return list

def main ():
    user_input = input("Enter a list of numbers separated by spaces:")
    nums =[float (x) for x in user_input.split()]
    reversed_list = reverse(nums)
    print("The reversed list is:",reversed_list)

main()

