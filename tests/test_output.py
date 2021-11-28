"""Test cases for confirming that generated docker compose files are valid."""

import unittest
from subprocess import check_call
from os.path import abspath, dirname, join, exists
from os import unlink
import sys

here = dirname(abspath(__file__))
parent = dirname(here)
templates_folder = join(here, 'data')
template_file = 'docker-compose.template'
rpi_output_file = join(here, 'data', 'rpi.yml')
rockpi_output_file = join(here, 'data', 'rockpi.yml')

sys.path.insert(1, parent)

from gen_docker_compose import DockerComposer


class TestValidComposeFileOutput(unittest.TestCase):

    def setUp(self) -> None:
        self._remove_output_files()
        return super().setUp()

    def tearDown(self) -> None:
        self._remove_output_files()
        return super().tearDown()

    def _remove_output_files(self):
        for filename in (rpi_output_file, rockpi_output_file):
            if exists(filename):
                unlink(filename)

    def test_rpi_compose_output_is_valid(self):
        # Uncomment line below if want to test custom templates.
        # dc = DockerComposer(templates_folder=templates_folder)
        dc = DockerComposer()
        dc.generate_compose_file('rpi', template_file, rpi_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {rpi_output_file} config -q', shell=True)

    def test_rockpi_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('rockpi', template_file, rockpi_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {rockpi_output_file} config -q', shell=True)
