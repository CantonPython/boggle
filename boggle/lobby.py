#
# Boggle game server lobby service
#

from proto.boggle.boggle_pb2_grpc import BoggleLobbyServicer
from proto.boggle.boggle_pb2 import Greeting

class Lobby(BoggleLobbyServicer):

    def __init__(self):
        pass

    def GetWelcomeMessage(self, context):
        greeting = Greeting(greeting='Welcome')
        return greeting
