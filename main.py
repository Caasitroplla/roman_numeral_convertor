from convertor import convert_to_integer, convert_to_roman

def main():
    menu = '''
        Quit = Quit
        to roman = conver to roman numeral
        to integer - convert to integer
    '''

    choice = ""

    while choice != 'quit':
        print(menu)
        choice = input("Enter option  ")
        
        if choice == 'to roman':
            choice = int(input("Enter integer to convert to roman  "))
            print(convert_to_roman(choice))

        elif choice == 'to integer':
            choice = input("Enter roman numeral to convert to integer  ")
            print(convert_to_integer(choice))

if __name__ == '__main__':
    main()