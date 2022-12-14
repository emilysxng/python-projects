def main():
    while True:
        height = int(input("Height: "))
        if height > 0 and height < 9:
            break

    for y in range(height):
        for x in range(height):

            if x + y < (height - 1):
                print(" ", end="")
            else:
                print("#", end="")

        print("  ", end="")

        for x in range(y + 1):
            print("#", end="")

        print()

main()