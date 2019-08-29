import os
import time

import requests


class Downloader:
    def __init__(self, path):
        self.__path = path

    def download(self, url, filename):
        file_path = self.__path + "/" + filename
        res = requests.get(url)
        if res.status_code == 200:
            content = res.content
            return save(file_path, content)
        else:
            raise Exception("Status code = [%s]" % res.status_code)


def gen_path():
    path = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def save(filename, content):
    f = open(filename, "wb")
    with f:
        f.write(content)
    return filename
