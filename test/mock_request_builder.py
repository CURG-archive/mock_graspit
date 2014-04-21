

from gen_proto import check_grasp_reachability_pb2
from gen_proto import run_recognition_pb2


def build_mock_check_grasp_reachability_request(filename="mock_check_grasp_reachability_requests/grasp_proto_5.saved_proto"):
    f = open(filename, "rb")
    check_grasp_request = check_grasp_reachability_pb2.CheckGraspReachabilityRequest()
    check_grasp_request.ParseFromString(f.read())
    return check_grasp_request


def build_mock_object_recognition_request():
    run_recognition_request = run_recognition_pb2.ObjectRecognitionRequest()
    return run_recognition_request


def build_mock_execute_grasp_request():
    pass

