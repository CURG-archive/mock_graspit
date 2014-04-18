
from gen_proto import run_recognition_pb2
from gen_proto import run_recognition_rpcz
from gen_proto import graspable_object_pb2

import rpcz
import unittest
import rostest


class TestRunRecognitionService(unittest.TestCase):

    is_setup = False

    def setUp(self):
        if not self.is_setup:
            self.is_setup = True
            app = rpcz.Application()
            self.run_recognition_request_stub = gen_proto.run_recognition_rpcz.ObjectRecognitionService_Stub(app.create_rpc_channel("tcp://127.0.0.1:5561"))

    def test_run_recognition_request(self):

        request = gen_proto.run_recognition_pb2.ObjectRecognitionRequest()
        response = self.run_recognition_request_stub.run(request, deadline_ms=3000)

        #now assert things about the response
        self.assertEqual(response, response)

if __name__ == '__main__':

    PKG = 'mock_graspit'
    rostest.rosrun(PKG, 'test_bare_bones', TestRunRecognitionService)
