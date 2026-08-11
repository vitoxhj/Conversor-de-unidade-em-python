import functions

def main():
    functions.create_json('history_conversor.json', [])
    while True:
        option = functions.interface()
        if option == 1:
            functions.temperature()
        elif option == 2:
            functions.distance()
        elif option == 3:
            functions.weight()
        elif option == 4:
            functions.time()
        elif option == 5:
            functions.speed()

if __name__ == '__main__':
    main()