"""Test cases for confirming that generated docker compose files are valid."""

import sys
import unittest
from os import unlink
from subprocess import check_call
from gen_docker_compose_by_variant import DockerComposer
from os.path import abspath, dirname, join, exists

here = dirname(abspath(__file__))
parent = dirname(here)
template_file = 'docker-compose.template'
nebra_indoor1_output_file = join(here, 'nebra-indoor1.yml')
nebra_outdoor1_output_file = join(here, 'nebra-outdoor1.yml')
nebra_indoor2_output_file = join(here, 'nebra-indoor2.yml')
nebra_outdoor2_output_file = join(here, 'nebra-outdoor2.yml')

sys.path.insert(1, parent)


class TestValidComposeFileOutput(unittest.TestCase):

    def setUp(self) -> None:
        self._remove_output_files()
        return super().setUp()

    def tearDown(self) -> None:
        self._remove_output_files()
        return super().tearDown()

    def _remove_output_files(self):
        for filename in (nebra_indoor1_output_file,
                         nebra_outdoor1_output_file,
                         nebra_indoor2_output_file,
                         nebra_outdoor2_output_file):
            if exists(filename):
                unlink(filename)

    def test_nebra_indoor1_compose_output_is_valid(self):
        # Uncomment line below if want to test custom templates.
        # dc = DockerComposer(templates_folder=templates_folder)
        dc = DockerComposer()
        dc.generate_compose_file('nebra-indoor1', template_file, nebra_indoor1_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {nebra_indoor1_output_file} config -q', shell=True)

    def test_nebra_outdoor1_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('nebra-outdoor1', template_file, nebra_outdoor1_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {nebra_outdoor1_output_file} config -q', shell=True)

    def test_nebra_indoor2_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('nebra-indoor2', template_file, nebra_indoor2_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {nebra_indoor2_output_file} config -q', shell=True)

    def test_nebra_outdoor2_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('nebra-outdoor2', template_file, nebra_outdoor2_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker-compose -f {nebra_outdoor2_output_file} config -q', shell=True)
