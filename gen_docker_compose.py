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

prog_name = os.path.basename(os.path.abspath(__file__))
here = os.path.dirname(os.path.abspath(__file__))

def load_file_config(file_path: str):
    file_config_dict = {}
    if os.path.isfile(file_path):
        lines = [l.strip() for l in open(file_path, 'r').read().split('\n')]
        for line in lines:
            if line.startswith('#'):
                # Ignore comment lines
                continue

            parts = line.split("=", maxsplit=1)
            if len(parts) != 2:
                # Ignore lines that don't follow key=value format
                continue

            key = parts[0].strip()
            value = parts[1].strip().strip('"')
            file_config_dict[key] = value

    return file_config_dict


if __name__ == '__main__':
    usage = f"""
    {prog_name} [docker-template_file]

    If no template file name is given then docker-compose.template is assumed as default.
    """

    template_file = 'docker-compose.template'

    if len(sys.argv) == 2:
        if '-h' == sys.argv[1]:
            print(usage)
            sys.exit(0)

        template_file = sys.argv[1]

    data = open(template_file, 'r').read()


    env_path = os.path.join(here, '.env')
    env_args = load_file_config(env_path)

    print(data.format(**env_args))
