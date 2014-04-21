
from gen_proto import run_recognition_pb2
from gen_proto import run_recognition_rpcz
from gen_proto import graspable_object_pb2
from gen_proto import check_grasp_reachability_pb2
from gen_proto import check_grasp_reachability_rpcz

import rpcz
import unittest
import rostest
import mock_request_builder


class TestFullPipeline(unittest.TestCase):

    def test_all(self):

        app = rpcz.Application()
        run_recognition_request_stub = run_recognition_rpcz.ObjectRecognitionService_Stub(app.create_rpc_channel("tcp://localhost:5561"))
        check_grasp_reachability_request_stub = check_grasp_reachability_rpcz.CheckGraspReachabilityService_Stub(app.create_rpc_channel("tcp://localhost:5561"))

        #test object recognition
        request = mock_request_builder.build_mock_object_recognition_request()
        response = run_recognition_request_stub.run(request, deadline_ms=60000)
        self.assertEqual(response, response)

        #test reachable check_grasp_reachability request 1:
        request = mock_request_builder.build_mock_check_grasp_reachability_request()
        response = check_grasp_reachability_request_stub.run(request, deadline_ms=10000)
        self.assertEqual(response, response)

        #test unreachable check_grasp_reachability request 2:
        request = mock_request_builder.build_mock_check_grasp_reachability_request()
        response = check_grasp_reachability_request_stub.run(request, deadline_ms=10000)
        self.assertEqual(response, response)



if __name__ == '__main__':

    PKG = 'mock_graspit'
    rostest.rosrun(PKG, 'test_bare_bones', TestFullPipeline)

