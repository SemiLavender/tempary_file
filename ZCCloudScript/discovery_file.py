import json
import os
import re
import sys
import time

_DEBUG = os.getenv("DEBUG", True)


def discovery(path):
    data = []
    with os.popen("ls -l " + path + " | grep - | awk \'{print $NF}\'") as apps:
        for app in apps:
            log_path = path + "/" + app
            if os.path.isdir(log_path):
                with os.popen("ls -l " + log_path + " | grep \'\\.log\' | awk \'{print $NF}\'") as logs:
                    for log in logs:
                        data.append({
                            "{#LOG_NAME}": log,
                            "{#LOG_PATH}": log_path + log
                        })
            else:
                if re.match("\.log$", app):
                    data.append({
                            "{#LOG_NAME}": app,
                            "{#LOG_PATH}": path + "/" + app
                        })
    print(json.dumps({
        "data": data
    }))


def debug(output):
    if _DEBUG:
        if not "debuglog" in globals():
            global debuglog
            debuglog = open("debuglog","a")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S : ", time.gmtime())
        debuglog.write(timestamp + str(output)+"\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        debug('discovery called is successful.')
        discovery(sys.argv[1])
    else:
        debug('the discovery called is failed, it request only one argv.')
    if "debuglog" in globals():
        debuglog.close()



