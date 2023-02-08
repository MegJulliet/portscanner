import sys
arguments = sys.argv
raw_range = arguments[1]


starting_range = int(raw_range.split('-')[0])
end_range = int(raw_range.split('-')[1])


def hello(port):
    print(f"port {port}")


for i in range(starting_range, end_range):
    hello(i)
