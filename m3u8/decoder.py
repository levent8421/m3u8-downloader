def decode(file):
    f = open(file)
    with f:
        lines = f.readlines()

    for line in lines:
        print(line)
