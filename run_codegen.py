from grpc_tools import protoc
protoc.main(('', '-I.', '--python_out=.', '--grpc_python_out=.', 'proto/boggle/boggle.proto'))
