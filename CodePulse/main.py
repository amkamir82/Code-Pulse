import argparse
from code_pulse_loader import webdriver_loader
from netstat_service import codepulse_address_service


def check_arguments():
    parser = argparse.ArgumentParser(description='A simple tool to get data from CodePulse.')
    parser.add_argument("-f", "--file", help="Path to classpath that will import to code pulse", required=False)
    args = parser.parse_args()
    if args.file:
        pass


def main():
    ip, port = codepulse_address_service.get_address()
    webdriver_loader.load_codepulse_on_web(ip, port)


if __name__ == "__main__":
    main()
