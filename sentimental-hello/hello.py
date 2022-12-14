def main():
    while True:
        name = input("What is your name? ")
        if len(name) > 0:
            break

    print(f"Hello, {name}")

main()