#!/usr/bin/python
import click

from commands.send import send_vectors
from commands.keys import generate_keys_command


@click.group()
def cli():
    pass


@cli.command('generate-keys')
@click.option('--filename', prompt='Filename for keys', help='The name of the file to save the keys')
def get_keys(filename):
    """Generates public and private keys"""
    generate_keys_command(filename)


@cli.command()
@click.option('--v', help='Send query to verification endpoint', is_flag=True)
@click.option('--gene', prompt='Lookup gene', help='The gene you want to query.')
@click.option('--row', prompt='Database row to write', type=int,
              help='This is the row where your query will be found in the database.')
@click.option('--pub-key', prompt='Public key',
              help='')
def query(v, gene, row, pub_key):
    """Sends an anonymous query"""
    send_vectors(row, gene, pub_key, v)

if __name__ == '__main__':
    cli()