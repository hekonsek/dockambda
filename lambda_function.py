import subprocess, os

def my_handler(event, context):
    # result = subprocess.call(["udocker", "run", "hello-world"])

    my_env = os.environ
    my_env["UDOCKER_TARBALL"] = "/var/task/udocker-1.1.4.tar.gz"

    p = subprocess.Popen(["python", "udocker", "install"], stdout=subprocess.PIPE, env=my_env)
    #p = subprocess.Popen(["pwd"], stdout=subprocess.PIPE, env=my_env)
    output, err = p.communicate()

    # result = subprocess.call(["ls"])
    message = output
    return {
        'message' : message
    }

