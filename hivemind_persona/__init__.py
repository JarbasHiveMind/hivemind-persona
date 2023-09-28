import json
import os

from hivemind_bus_client.message import HiveMessage, HiveMessageType
from hivemind_core.protocol import HiveMindListenerProtocol
from ovos_persona import Persona
from ovos_utils.messagebus import Message


class FakeCroftPersonaProtocol(HiveMindListenerProtocol):
    """"""
    persona = None

    @classmethod
    def set_persona(cls, persona_json: str):
        with open(persona_json) as f:
            persona = json.load(f)
        name = persona.get("name") or os.path.basename(persona_json)
        cls.persona = Persona(name=name, config=persona)

    def handle_inject_mycroft_msg(self, message: Message, client):
        """
        message (Message): mycroft bus message object
        """
        if message.msg_type == "recognizer_loop:utterance":
            utt = message.data["utterances"][0]
            answer = response = self.persona.complete(utt)
            payload = HiveMessage(HiveMessageType.BUS,
                                  message.reply("speak", {"utterance": answer}))
            client.send(payload)
