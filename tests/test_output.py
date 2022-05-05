"""Test cases for confirming that generated docker compose files are valid."""

import sys
import unittest
from os import unlink
from subprocess import check_call
from gen_docker_compose import DockerComposer
from os.path import abspath, dirname, join, exists

here = dirname(abspath(__file__))
parent = dirname(here)
template_file = 'docker-compose.template'
output_file = join(here, 'dc.yml')

sys.path.insert(1, parent)


class TestValidComposeFileOutput(unittest.TestCase):

    def setUp(self) -> None:
        self._remove_output_files()
        return super().setUp()

    def tearDown(self) -> None:
        self._remove_output_files()
        return super().tearDown()

    def _remove_output_files(self):
        if exists(output_file):
            unlink(output_file)

    def test_compose_output_is_valid(self):
        # Uncomment line below if want to test custom templates.
        # dc = DockerComposer(templates_folder=templates_folder)
        dc = DockerComposer()
        dc.generate_compose_file(template_file, output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {output_file} config -q', shell=True)
