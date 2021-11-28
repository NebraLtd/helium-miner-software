"""
Generate docker-compose.yml based on docker-compose.tempalte file.

Some how balena doesn't like output of:

 `docker-compose -f docker-compose.template  config > docker-compose.yml`

That's probably because output for `docker-compose config` does not retain the
order of the sections present in the file. So as a workaround this small file
tries to do the same thing but without re-arranging sections and just replacing
placeholder values.

In future if desired this can use a proper templating system like mako or jinja2.
For the time being to avoid adding dependencies to the project it just uses python
format strings.
"""

import sys
import os
import argparse
from configparser import ConfigParser

from jinja2 import Environment, select_autoescape, FileSystemLoader


prog_name = os.path.basename(os.path.abspath(__file__))
here = os.path.dirname(os.path.abspath(__file__))


class DockerComposer:
    """A class to facilitate generation of docker-compose.yml files from templates."""

    def __init__(self):
        self.jinja_env = Environment(
            loader=FileSystemLoader("templates"),
            autoescape=select_autoescape()
        )

        config = ConfigParser(strict=True)
        # Suppress default behavior of converting key names to lower-case.
        config.optionxform = lambda option: option
        config.read('settings.ini')
        self.config = config

    def generate_compose_file(
            self, template_file: str, output_file: str, arch: str) -> None:
        """generate_compose_file Render template_file to generate compose file.

        Args:
            template_file (str): Template file name without folder name.
                Should be present in the templates folder.
            output_file (str): Output filename. Can be a path. Otherwise
                file is created in current folder.
        """
        template = self.jinja_env.get_template(template_file)
        template_args = {'ARCH': arch}
        assert 'versions' in self.config
        for k, v in self.config['versions'].items():
            template_args[k] = v

        output = template.render(**template_args)
        open(output_file, 'w').write(output)



if __name__ == '__main__':

    parser = argparse.ArgumentParser("Generate docker-compose.yml.")
    parser.add_argument('--arch', '-a', default='arm64',
                        help="Target architecture.")
    parser.add_argument('--template', '-t', default='docker-compose.template',
                        help=("Input template file. Should be present in "
                              "templates folder."))
    parser.add_argument('--output', '-o', default='docker-compose.yml',
                        help="Output file. Created in current folder.")
    args = parser.parse_args()
    # print(args)

    composer = DockerComposer()
    composer.generate_compose_file(args.template, args.output, args.arch)
