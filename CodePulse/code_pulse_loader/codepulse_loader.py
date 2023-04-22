from subprocess import Popen, PIPE
import config
import subprocess


def run_codepulse():
    command = [config.CODEPULSE_ADDRESS, "/codepulse"]

    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    output, error = p.communicate()
    print(output)
