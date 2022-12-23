#!/usr/bin/env python

from game import Game

def main() -> int:

    game = Game();

    while not game.quit:

        game.show();
        game.play();

    else:
        game.show();

    return 0;

if __name__ == '__main__':
    exit(main());
