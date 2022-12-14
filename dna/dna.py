import csv
import sys

def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py [DATA].csv [SEQUENCE].txt")

    # TODO: Read database file into a variable
    filename = sys.argv[1]
    data = []

    with open(filename) as file:
        reader = csv.reader(file)
        data = list(reader) #reads the database into a list (comma separated values).
                            #name and STRs are included in the list as the first list in the array of lists.

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as f:
        dna_sequence = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    longest_sequence = []
    for i in range (1, len(data[0])):
        x = longest_match(dna_sequence, data[0][i])
        longest_sequence.append(x)

    # TODO: Check database for matching profiles and print name
    counter = 0
    suspect = "No Match"

    for i in range(1, len(data)):            #gives # of rows
        for j in range(len(data[0]) - 1):    #gives # of elements in row, excluding name (aka colomns)
            if longest_sequence[j] == int(data[i][j + 1]):   #j + 1 is so that the name at the front is skipped
                counter += 1

        if counter == len(longest_sequence):
            suspect = data[i][0]
            break

        else:
            counter = 0

    print(suspect)
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

main()
