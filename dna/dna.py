import csv
import sys


def main():

    # Ensure proper number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python individuals.csv dnastring.txt")

    # Read database file into a variable
    # Open CSV file
    # Extract the fieldnames into a list
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        fieldnamelst = reader.fieldnames[1:]

    # print(fieldnamelst)

    # Read DNA sequence file into a string variable
    file = open(sys.argv[2], "r")
    for line in file:
        dnasequence = line
    file.close()
    # print(dnasequence)

    # Find the longest matches of the short dna subsequences in the header
    matches = []
    for subsequence in fieldnamelst:
        lm = str(longest_match(dnasequence, subsequence))
        matches.append(lm)
    # print(f"Matches: {matches}")

    # Combine the header names with the longest match into a dictionary
    matchdict = {}
    for i, field in enumerate(fieldnamelst):
        matchdict[field] = matches[i]
    # print(f"Matchdict: {matchdict}")

    name = ""
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        matchdictvalues = list(matchdict.values())
        # compare sequence in each row of the person database to the dna sequences
        for row in reader:
            rowvals = list(row.values())
            if rowvals[1:] == matchdictvalues:
                print(row['name'])
                sys.exit(0)

        print("No match")

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