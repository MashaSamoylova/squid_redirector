#!/usr/bin/env python3
import sys
import json
import syslog


def modify_url(line, config_file):
    with open(config_file) as f:
        config = json.load(f)
        redirect_urls = config.keys()

    old_url = line.split(' ')[0]

    for url in redirect_urls:
        if url in old_url:
            new_url = "http://" + config[url] + "\n"
            syslog.syslog(old_url + " -> " + new_url)
            return new_url
    return "\n"


def main():
    config_file = sys.argv[1]
    while True:
        line = sys.stdin.readline().strip()
        new_url = modify_url(line, config_file)
        sys.stdout.write(new_url)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
