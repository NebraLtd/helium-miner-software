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
syncrobit_output_file = join(here, 'syncrobit.yml')
pycom_output_file = join(here, 'pycom.yml')
controllino_output_file = join(here, 'controllino.yml')
rak_output_file = join(here, 'rak.yml')
bobcat_px30_output_file = join(here, 'bobcat-px30.yml')

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
                         nebra_outdoor2_output_file,
                         syncrobit_output_file,
                         pycom_output_file,
                         controllino_output_file,
                         rak_output_file,
                         bobcat_px30_output_file):
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
            f'docker compose -f {nebra_indoor1_output_file} config -q', shell=True)

    def test_nebra_outdoor1_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('nebra-outdoor1', template_file, nebra_outdoor1_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {nebra_outdoor1_output_file} config -q', shell=True)

    def test_nebra_indoor2_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('nebra-indoor2', template_file, nebra_indoor2_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {nebra_indoor2_output_file} config -q', shell=True)

    def test_nebra_outdoor2_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('nebra-outdoor2', template_file, nebra_outdoor2_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {nebra_outdoor2_output_file} config -q', shell=True)

    def test_syncrobit_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('syncrobit-fl1', template_file, syncrobit_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {syncrobit_output_file} config -q', shell=True)

    def test_pycom_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('pycom-fl1', template_file, pycom_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {pycom_output_file} config -q', shell=True)

    def test_controllino_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('controllino-fl1', template_file, controllino_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {controllino_output_file} config -q', shell=True)

    def test_rak_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('rak-fl1', template_file, rak_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {rak_output_file} config -q', shell=True)

    def test_bobcat_px30_compose_output_is_valid(self):
        dc = DockerComposer()
        dc.generate_compose_file('bobcat-px30', template_file, bobcat_px30_output_file)

        # On failure or non-zero return code this returns CalledProcessError
        # so if this runs without that, it's considered successful as
        # `docker-compose config -q` returns 1 on invalid config
        check_call(
            f'docker compose -f {bobcat_px30_output_file} config -q', shell=True)

    def test_variant_is_invalid(self):
        dc = DockerComposer()

        with self.assertRaises(KeyError) as context:
            dc.generate_compose_file('unknown-variant', template_file, rak_output_file)

        self.assertTrue('unknown-variant' in str(context.exception))
