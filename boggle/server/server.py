#
# Boggle game server
#

import argparse
import concurrent.futures
import logging
import sys

import grpc
from boggle.lobby import Lobby
from proto.boggle.boggle_pb2_grpc import add_BoggleLobbyServicer_to_server

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--port', type=int, help='port number', default=50050)
    parser.add_argument('--threads', type=int, help='number of worker threads', default=10)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=args.threads)
    server = grpc.server(executor)

    lobby = Lobby()
    add_BoggleLobbyServicer_to_server(lobby, server)

    addr = '[::]:{0}'.format(args.port)
    logging.info('listening on port {0}'.format(args.port))
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    sys.exit(main())
