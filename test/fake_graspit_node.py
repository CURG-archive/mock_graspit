#!/usr/bin/env python

from gen_proto import run_recognition_pb2
from gen_proto import run_recognition_rpcz
from gen_proto import graspable_object_pb2
from gen_proto import check_grasp_reachability_pb2
from gen_proto import check_grasp_reachability_rpcz
from gen_proto import execute_grasp_rpcz
from gen_proto import get_camera_origin_pb2
from gen_proto import get_camera_origin_rpcz

import math

import rpcz
import unittest
import rostest
import rospy
import mock_request_builder



class TestFullPipeline(unittest.TestCase):

    def test_all(self):
        rospy.loginfo("starting TestFullPipeline")

        app = rpcz.Application()
        run_recognition_request_stub = run_recognition_rpcz.ObjectRecognitionService_Stub(app.create_rpc_channel("tcp://localhost:5561"))
        check_grasp_reachability_request_stub = check_grasp_reachability_rpcz.CheckGraspReachabilityService_Stub(app.create_rpc_channel("tcp://localhost:5561"))
        execute_grasp_request_stub = execute_grasp_rpcz.ExecuteGraspService_Stub(app.create_rpc_channel("tcp://localhost:5561"))
        camera_origin_request_stub = get_camera_origin_rpcz.CameraOriginService_Stub(app.create_rpc_channel("tcp://localhost:5561"))

        #test camera origin request
        rospy.loginfo("testing camera origin request")
        request = mock_request_builder.build_mock_get_camera_origin_request()
        response = camera_origin_request_stub.run(request, deadline_ms=10000)

        px = math.floor(response.cameraOrigin.position.x)
        py = math.floor(response.cameraOrigin.position.y)
        pz = math.floor(response.cameraOrigin.position.z)

        expected_px = 419
        expected_py = -566
        expected_pz = 490

        valid_px = px > expected_px -3 and px < expected_px + 3
        valid_py = py > expected_py -3 and py < expected_py + 3
        valid_pz = pz > expected_pz -3 and pz < expected_pz + 3

        self.assertTrue(valid_px, "py:" + str(py) + " != expected: " + str(expected_py))
        self.assertTrue(valid_py, "py:" + str(py) + " != expected: " + str(expected_py))
        self.assertTrue(valid_pz, "pz:" + str(pz) + " != expected: " + str(expected_pz))


        #test object recognition
        request = mock_request_builder.build_mock_object_recognition_request()
        response = run_recognition_request_stub.run(request, deadline_ms=1000)

        names = []
        for found_object in response.foundObjects:
            names.append(found_object.name)

        # self.assertTrue("gillette_shaving_gel" in names)
        # self.assertTrue("all" in names)
        self.assertTrue("garnier_shampoo_bottle" in names)

        #test reachable check_grasp_reachability request 1:
        request = mock_request_builder.build_valid_check_grasp_reachability_request()
        response = check_grasp_reachability_request_stub.run(request, deadline_ms=10000)
        print "response:" + str(response)
        self.assertEqual(response.graspStatus, 1, "expected: 1, got: " + str(response.graspStatus))

        #test unreachable check_grasp_reachability request 2:
        # request = mock_request_builder.build_invalid_check_grasp_reachability_request()
        # response = check_grasp_reachability_request_stub.run(request, deadline_ms=10000)
        # print "response:" + str(response)
        # self.assertEqual(response.graspStatus, 0, "expected: 0, got: " + str(response.graspStatus))

        # #test execute grasp request
        # request = mock_request_builder.build_mock_execute_grasp_request()
        # response = execute_grasp_request_stub.run(request, deadline_ms=10000)
        # self.assertEqual(response, response)


if __name__ == '__main__':

    PKG = 'mock_graspit'
    rostest.rosrun(PKG, 'test_bare_bones', TestFullPipeline)

