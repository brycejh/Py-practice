import argparse

parser = argparse.ArgumentParser(description="Process CSV file.")
parser.add_argument("filename", help="CSV file to be parsed")
parser.add_argument(
    "-c", "--columns", type=int, action="append", help="columns to select from CSV file"
)
parser.add_argument(
    "-v", "--verbose", help="print logging messages", action="store_true"
)

args = parser.parse_args()
# print(args)

print("")
if args.verbose:
    print(
        "Now priniting Column(s): " + str(args.columns)
        if args.columns is not None
        else "Printing all columns:",
    )
print("")
with open(args.filename) as CSV:
    for line in CSV:
        stuff = line.split(",")
        if args.columns is not None:
            for i in args.columns:
                print(stuff[i], end=" ")
            print("")
        else:
            print(line, end="")
    if args.columns is None:
        print("")
