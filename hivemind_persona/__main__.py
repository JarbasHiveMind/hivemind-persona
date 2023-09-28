import argparse

from hivemind_core.service import HiveMindService
from ovos_utils.messagebus import FakeBus

from hivemind_persona import FakeCroftPersonaProtocol


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--persona", help="path to persona .json file", required=True)
    args = parser.parse_args()
    FakeCroftPersonaProtocol.set_persona(args.persona)
    service = HiveMindService(protocol=FakeCroftPersonaProtocol,
                              bus=FakeBus())
    service.run()


if __name__ == "__main__":
    run()
