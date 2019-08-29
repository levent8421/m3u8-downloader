import os
import re

from m3u8.decoder import decode
from m3u8.editor import VideoSplicer
from net_utils.downloader import Downloader, gen_path


def download_ts(playlist, downloader):
    files = []
    for i in range(len(playlist)):
        play_item = playlist[i]
        url = play_item['url']
        print('Downloading ts[%s]-[%s]......' % (i, url))
        file = downloader.download(url, str(i) + '.ts')
        print('Download [%s] Success!' % i)
        files.append(file)
    return files


def load_files(path):
    files = os.listdir(path)
    res = []
    for file in files:
        if file.endswith('.ts'):
            res.append(os.path.join(path, file))

    def get_file_num(filename):
        g = re.match(r'\w+\\(\d+)\.ts', filename)
        if g:
            return int(g.groups()[0])
        raise Exception('Unknown file [%s]' % filename)

    return sorted(res, key=get_file_num)


def concat(files, target_filename):
    vs = VideoSplicer(files)
    vs.concat()
    vs.save(target_filename)


def download(url):
    save_path = gen_path()
    downloader = Downloader(save_path)
    file = downloader.download(url, 'playlist.m3u8')
    base_url = url.split('?')[0]
    base_url = base_url[:base_url.rindex('/') + 1]
    decode_res = decode(file, base_url)
    file_list = download_ts(decode_res['playList'], downloader)
    concat(file_list, os.path.join(save_path, 'result.mp4'))


def main():
    f = open('job.txt')
    with f:
        lines = f.readlines()
    for url in lines:
        url = url.strip()
        if url:
            download(url)
        else:
            print('Ignore [%s]' % url)


if __name__ == '__main__':
    main()
