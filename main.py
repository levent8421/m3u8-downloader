from m3u8.decoder import decode
from net_utils.downloader import download

FILE_URL = "https://cloud.video.taobao.com/play/u/3907963977/p/1/d/hd/e/3/t/1/233022958320.m3u8?auth_key" \
           "=YXBwX2tleT04MDQ0ODEmYXV0aF9pbmZvPXsiY291cnNlSWQiOjExMzYxOCwiYml6VHlwZSI6ImJ1eSIsInZpZGVvSWQ" \
           "iOjIzMzAyMjk1ODMyMCwiZW5jcnlwdElkIjoiQ0EwOTUxNDFDMzVGMDY4NUQ4MzExMERCNjIyQkM5ODczNThGQTdCN0Y" \
           "0OEU4QkQ5RTM2NjkzOTJGNThDMENDQSJ9JnRpbWVzdGFtcD0xNTY3MDcwNTU2 "


def download_m3u8(url):
    return download(url)


def main():
    # file = download_m3u8(FILE_URL)
    file = "20190828174543/playlist.m3u8"
    decode(file)


if __name__ == '__main__':
    main()
