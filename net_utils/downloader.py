import os
import time

import requests


def save(filename, content):
    target_path = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    file_path = target_path + "/" + filename
    f = open(file_path, "w")
    f.write(content.decode())
    f.close()
    return file_path


def download(url):
    res = requests.get(url)
    if res.status_code == 200:
        content = res.content
        return save("playlist.m3u8", content)
    else:
        raise Exception("Status code = [%s]" % res.status_code)
