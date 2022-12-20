"""
Generate docker-compose.yml based on docker-compose.template file.

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
from typing import Union
from configparser import ConfigParser

from jinja2 import Environment, select_autoescape, FileSystemLoader


prog_name = os.path.basename(os.path.abspath(__file__))
here = os.path.dirname(os.path.abspath(__file__))


class DockerComposer:
    """
    A class to facilitate generation of docker-compose.yml files
    from templates.
    """

    def __init__(self, templates_folder: Union[str, None] = None):
        if templates_folder is None:
            templates_folder = os.path.join(here, 'templates')

        self.jinja_env = Environment(
            loader=FileSystemLoader(templates_folder),
            autoescape=select_autoescape()
        )

        config = ConfigParser(strict=True)
        # Suppress default behavior of converting key names to lower-case.
        config.optionxform = lambda option: option
        config.read('settings.ini')
        self.config = config

    def generate_compose_file(
            self,
            device_type: str,
            template_file: str,
            output_file: str
    ) -> None:
        """generate_compose_file Render template_file to generate compose file.

        Args:
            device_type (str): The target device for the docker compose file.
                This device should have a section in settings.ini.
            template_file (str): Template file name without folder name.
                Should be present in the templates folder.
            output_file (str): Output filename. Can be a path. Otherwise
                file is created in current folder.
        """
        template = self.jinja_env.get_template(template_file)
        if not self.config.has_section(f'device_{device_type}'):
            print(f"Error: Unknown device type: {device_type}. "
                  "No matching config section found in settings.ini")
            sys.exit(1)

        template_args = {}

        if 'versions' not in self.config:
            raise RuntimeError("Bad config, no [versions] section found")

        for k, v in self.config['versions'].items():
            template_args[k] = v

        template_args["ENV"] = os.environ

        for k, v in self.config['quectel_modem'].items():
            template_args[k] = v

        for k, v in self.config[f'device_{device_type}'].items():
            template_args[k] = v

        output = template.render(**template_args)
        with open(output_file, 'w') as template_output:
            template_output.write(output)


if __name__ == '__main__':

    parser = argparse.ArgumentParser("Generate docker-compose.yml.")
    parser.add_argument('device_type',
                        help="Target device. Must have a section in "
                             "settings.ini.")
    parser.add_argument('--template', '-t', default='docker-compose.template',
                        help="Input template file. Should be present in "
                             "templates folder.")
    parser.add_argument('--output', '-o', default='docker-compose.yml',
                        help="Output file. Created in current folder.")
    args = parser.parse_args()
    # print(args)

    composer = DockerComposer()
    composer.generate_compose_file(
        args.device_type, args.template, args.output)
