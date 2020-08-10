name = input('Enter your name: ')

letter =list(name)

while letter:
    r_letter = letter.pop()
    if letter == r_letter:
        print('Palindrome')
        print(letter)
    else:
        print(r_letter, end='')
#I am so close on this and cannot figure out why it is skipping my if statement.
