import sys

from tests.main import Game


def main():
    game = Game()
    while True:
        strip = sys.stdin.readline().strip()
        if not strip:
            break
        output = game.run(strip)
        sys.stdout.write(output + "\n")


if __name__ == '__main__':
    main()
