

from gen_proto import check_grasp_reachability_pb2
from gen_proto import run_recognition_pb2

import roslib.packages

pkg_path = roslib.packages.get_pkg_dir('mock_graspit') + '/test/mock_check_grasp_reachability_requests/'




def build_mock_check_grasp_reachability_request(filename="grasp_proto_5.saved_proto"):
    f = open(pkg_path + filename, "rb")
    check_grasp_request = check_grasp_reachability_pb2.CheckGraspReachabilityRequest()
    check_grasp_request.ParseFromString(f.read())
    return check_grasp_request


def build_mock_object_recognition_request():
    run_recognition_request = run_recognition_pb2.ObjectRecognitionRequest()
    return run_recognition_request


def build_mock_execute_grasp_request():
    pass

