while 1:
    print()
    print("What gender are you?")
    print("1. Male")
    print("2. Female")
    print("3. Prefer not to answer")
    print("4. Choice other than 1,2 and 3")
    choice =input("Enter a choice 1/2/3/4: ")
    if choice == '1':
        print("You are male.")
    elif choice == '2':
        print("You are female")
    elif choice == '3':
        print("You prefer not to answer")
    elif choice == '4':
        print("Choice other than 1,2 and 3")
    break;
