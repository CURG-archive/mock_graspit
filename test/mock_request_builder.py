

from gen_proto import check_grasp_reachability_pb2
from gen_proto import run_recognition_pb2
from gen_proto import execute_grasp_pb2
from gen_proto import get_camera_origin_pb2

import roslib.packages

pkg_path = roslib.packages.get_pkg_dir('mock_graspit')


def build_valid_check_grasp_reachability_request(filename="grasp_proto_5.saved_proto"):
    file_path = pkg_path + "/test/mock_requests/mock_check_grasp_reachability_requests/" + filename
    emtpy_request = check_grasp_reachability_pb2.CheckGraspReachabilityRequest()
    request = _build_request(file_path, emtpy_request)
    return request


def build_invalid_check_grasp_reachability_request(filename="grasp_proto_5.saved_proto"):
    file_path = pkg_path + "/test/mock_requests/mock_check_grasp_reachability_requests/" + filename
    emtpy_request = check_grasp_reachability_pb2.CheckGraspReachabilityRequest()
    request = _build_request(file_path, emtpy_request)
    return request


def build_mock_object_recognition_request():
    run_recognition_request = run_recognition_pb2.ObjectRecognitionRequest()
    return run_recognition_request


def build_mock_execute_grasp_request(filename="execute_grasp_request3.saved_proto"):
    file_path = pkg_path + "/test/mock_requests/mock_execute_grasp_requests/" + filename
    emtpy_request = execute_grasp_pb2.ExecuteGraspRequest()
    request = _build_request(file_path, emtpy_request)
    return request


def build_mock_get_camera_origin_request():
    request = get_camera_origin_pb2.CameraOriginRequest()
    return request


def _build_request(file_path, request):
    f = open(file_path, "rb")
    request.ParseFromString(f.read())
    return request