while True:
    name =input("Enter a name: ")
    if name == name[::-1]:
        print(name.capitalize())
        print ("Palindrome")

    else:
        print(name[::-1].capitalize())

#
