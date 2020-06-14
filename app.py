import random
import click

from utils import Play2048

@click.group()
def cli():
    pass

@cli.command()
def play():

    game = Play2048()
    game.print_board()
    game.playing()

if __name__ == '__main__':
    cli()
