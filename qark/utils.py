import os
from functools import partial

import json
import urllib.request
import time
from urllib.error import URLError

global TASK_ID
TASK_ID = None

def create_directories_to_path(path):
    """Create directories to a path if they don't exist."""

    try:
        os.makedirs(os.path.dirname(path))
    except Exception:
        # directory already exists
        pass


def file_has_extension(extension, file_path):
    return os.path.splitext(file_path.lower())[1] == extension.lower()


is_java_file = partial(file_has_extension, ".java")

httpHeaders = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

rdata = {
        "Function": "appTestMain.py",
        "ErrorCode": 1000,
        "Result": "",
        "ExecDesc": "",
        "FailReason": "",
        "Advice": "",
        "StartTime": int(time.time()),
        "EndTime": int(time.time()),
        "State": 4,
    }


def RsltPush(taskId, rdata, charset='utf-8', reqnum=2):
    # Push function modules and script execution results to the cloud via the HTTP API

    if taskId is None:
        print("taskid is None")
        return

    DATA = json.JSONEncoder().encode(rdata).encode('utf-8')
    #  url = 'http://10.120.99.202:8090/api/v1/LockTest/LockRsltPush=' + taskId
    url = 'http://127.0.0.1:9000/api/v1/LockTest/LockRsltPush?taskid=' + taskId

    req = urllib.request.Request(url, data=DATA, headers=httpHeaders, method='POST')
    info = None
    try:
        response = urllib.request.urlopen(req)
        info = response.read().decode(charset,errors="ignore")
    except URLError as e:
        if hasattr(e,'reason'):
            print("[RsltPush]Failed to reach a server,Reason:",e.reason, flush=True)
        elif hasattr(e, 'code'):
            print("[RsltPush]The Server couldnt fulfill the request,errcode:",e.code, flush=True)
            if reqnum > 0 and 500 <= e.code <= 600:
                time.sleep(random.randint(5, 11))
                RsltPush(taskId,rdata,charset=charset, reqnum=reqnum-1)


def environ_path_variable_exists(variable_name):
    """Determines if the os.environ variable exists and is a valid path.

    :rtype: bool
    """
    try:
        return os.path.exists(os.environ[variable_name])
    except KeyError:
        return False
