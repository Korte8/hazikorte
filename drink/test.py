import model
import sys


def main():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Nem megfelelő parancssori argumentum.", file=sys.stderr)
        return
    n = int(sys.argv[1])
    italok_l = []
    for i in range(n):
        line = input()
        tokens = line.split(";")
        if len(tokens) == 3:
            ital = model.Ital(tokens[0], tokens[1], int(tokens[2]))
            italok_l.append(ital)
        else:
            szeszesital = model.Szeszesital(tokens[0], tokens[1], int(tokens[2]), float(tokens[3]))
            italok_l.append(szeszesital)
    for ital in sorted(italok_l, key=lambda ital: (ital.name, ital._packaging)):
        print(ital)


if __name__ == "__main__":
    main()
