import click
from src.aba_plus_g_parse import generate_aba_plus_g_framework_from_file
from src.labelling_algorithms import construct_grounded_labelling
from src.extensions import get_extensions, dump_extensions

@click.command()
@click.option('--file',
              help='Path to file defining the DSS json data.')


def compute_extensions(file):
    abapf = generate_aba_plus_g_framework_from_file(file)
    extensions = get_extensions(abapf)
    click.echo("--------------------------Extensions-----------------------")
    click.echo(extensions)
    click.echo("--------------------------Extensions-----------------------")
    dump_extensions(extensions, file)


if __name__ == "__main__":
	compute_extensions()
