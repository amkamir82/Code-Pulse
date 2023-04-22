import time
from subprocess import Popen, PIPE
from selenium import *
from selenium.webdriver.chrome.options import Options
import argparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from code_pulse_loader import webdriver_loader


def get_codepulse_address():
    out, err = Popen(['netstat', '-antlp'], stdout=PIPE).communicate()

    for line in out.splitlines():
        line = line.decode('utf8')
        if 'ESTABLISHED' not in line:
            continue

        line = line.split()
        if '/' not in line[-1]:
            continue
        p = line[-1].split('/')[0]
        line[-1] = str(p) + ' -> ' + open('/proc/' + p + '/cmdline', 'rb').read().replace(b'\x00', b' ').decode('utf8')
        if 'jetty' not in line[-1]:
            continue

        res = line[3].split(':')
        return res[0], int(res[1])


def main():
    parser = argparse.ArgumentParser(description='A simple tool to get data from CodePulse.')
    parser.add_argument("-f", "--file", help="Path to classpath that will import to code pulse", required=True)
    args = parser.parse_args()

    # run_codepulse()
    sleep(1)
    ip, port = get_codepulse_address()
    print(args.file)


if __name__ == "__main__":
    # main()
    driver = webdriver_loader.load_webdriver("35389")
    # webdriver_loader.load_codepulse_on_web(driver, "35389")
