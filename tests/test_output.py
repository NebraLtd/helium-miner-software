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
rpi_output_file = join(here, 'rpi.yml')
rockpi_output_file = join(here, 'rockpi.yml')
pycom_output_file = join(here, 'pycom.yml')
pisces_output_file = join(here, 'pisces.yml')

sys.path.insert(1, parent)


class TestValidComposeFileOutput(unittest.TestCase):

    def setUp(self) -> None:
        self._remove_output_files()
        return super().setUp()

    def tearDown(self) -> None:
        self._remove_output_files()
        return super().tearDown()

    def _remove_output_files(self):
        for filename in (rpi_output_file, rockpi_output_file, pycom_output_file, pisces_output_file):
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

    def test_pycom_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('pycom', template_file, pycom_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {pycom_output_file} config -q', shell=True)

    def test_pisces_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('pisces', template_file, pisces_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {pisces_output_file} config -q', shell=True)
