"""
Generate docker-compose.yml based on docker-compose.tempalte file.

Some how balena doesn't like output of:

 `docker-compose -f docker-compose.template  config > docker-compose.yml`

That's probably because output for `docker-compose config` does not retain the
order of the sections present in the file. So as a workaround this small file
tries to do the same thing but without re-arranging sections and just replacing
placeholder values.
"""

import sys
import os
import argparse
from typing import Union
from configparser import ConfigParser
from hm_pyhelper.hardware_definitions import variant_definitions

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
            variant_type: str,
            template_file: str,
            output_file: str,
            generate_all: str,
            output_folder: str,
    ) -> None:
        """generate_compose_file Render template_file to generate compose file.

        Args:
            variant (str): The target variant for the docker compose file.
                This variant has to have a definition in hm-pyhelper hardware-definitions.
            template_file (str): Template file name without folder name.
                Should be present in the templates folder.
            output_file (str): Output filename. Can be a path. Otherwise
                file is created in current folder.
            generate_all (bool): Indicates whether a bulk generation has been requested or not
            output_folder (str): Output folder for bulk generation. Relevant if
                generate_all is true.
        """
        template = self.jinja_env.get_template(template_file)

        if 'versions' not in self.config:
            raise RuntimeError("Bad config, no [versions] section found")

        if generate_all is False:
            if variant_type is None:
                print("Error: Variant parameter is required.")
                sys.exit(1)

            try:
                variant_params = variant_definitions[variant_type]
            except Exception:
                print(f"Error: Unknown variant type: {variant_type}. "
                      "No matching variant definition found in hm-pyhelper/hardware_definitions.")
                sys.exit(2)

            template_args = {}

            for k, v in self.config['versions'].items():
                template_args[k] = v

            template_args["ENV"] = os.environ

            for k, v in self.config['quectel_modem'].items():
                template_args[k] = v

            try:
                template_args['I2C_DEVICE'] = variant_params['KEY_STORAGE_BUS']
            except Exception:
                print("Error: Variant does not have a KEY_STORAGE_BUS information.")
                sys.exit(3)

            try:
                template_args['ARCH'] = variant_params['CPU_ARCH']
            except Exception:
                print("Error: Variant does not have a CPU_ARCH information.")
                sys.exit(4)

            output = template.render(**template_args)
            with open(output_file, 'w') as template_output:
                template_output.write(output)

            print(f"Docker compose file for {variant_type} has been generated successfully.")

        else:
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)

            new_style_variants = \
                [variant_type for variant_type in variant_definitions if variant_type.islower()]

            for variant_type in new_style_variants:
                variant_params = variant_definitions[variant_type]
                template_args = {}

                for k, v in self.config['versions'].items():
                    template_args[k] = v

                template_args["ENV"] = os.environ

                for k, v in self.config['quectel_modem'].items():
                    template_args[k] = v

                try:
                    template_args['I2C_DEVICE'] = variant_params['KEY_STORAGE_BUS']
                except Exception:
                    print("Error: Variant does not have a KEY_STORAGE_BUS information.")
                    sys.exit(5)

                try:
                    template_args['ARCH'] = variant_params['CPU_ARCH']
                except Exception:
                    print("Error: Variant does not have a CPU_ARCH information.")
                    sys.exit(6)

                output = template.render(**template_args)
                output_file = f"{output_folder}/docker-compose-{variant_type}.yml"
                with open(output_file, 'w') as template_output:
                    template_output.write(output)

            print("Docker compose files for all variants have been generated successfully.")


if __name__ == '__main__':

    parser = argparse.ArgumentParser("Generate docker-compose.yml.")
    parser.add_argument('--variant', '-v',
                        help="Target variant. Must have been defined in hm-pyhelper.")
    parser.add_argument('--template', '-t', default='docker-compose.template',
                        help="Input template file. Should be present in templates folder.")
    parser.add_argument('--output', '-o', default='docker-compose.yml',
                        help="Output file. Created in current folder.")
    parser.add_argument('--all', '-a', action='store_true',
                        help="Generate compose files for all variants.")
    parser.add_argument('--folder', '-f', default='device-compose-files',
                        help="Output folder for the new compose files of all variants.")
    args = parser.parse_args()

    composer = DockerComposer()
    composer.generate_compose_file(
        args.variant, args.template, args.output, args.all, args.folder)
