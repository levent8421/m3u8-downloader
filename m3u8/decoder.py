import re


class M3U8Decoder:
    def __init__(self, lines):
        self.__lines = lines
        self.__lines_num = len(lines)
        self.__res = {
            'playList': [],
            'mate': {}
        }

    def decode(self):
        pos = 0
        while pos < self.__lines_num:
            pos += self.decode_line(pos, self.__lines)
        return self.__res

    def decode_line(self, pos, lines):
        line = lines[pos]
        line = line.strip()
        res = re.match(r'^#([^:\s]+):?([^\s]+)?$', line)
        if not res:
            return 1
        groups = res.groups()
        if groups[0] == 'EXTINF':
            length = groups[1].replace(',', '')
            play_item = {
                'url': lines[pos + 1].strip(),
                'len': float(length)
            }
            self.__res['playList'].append(play_item)
            return 2
        else:
            self.__res['mate'][groups[0]] = groups[1]
            return 1

    def normalization_play_list_url(self, base_url):
        for play_item in self.__res['playList']:
            url = play_item['url']
            if not (url.startswith('http://') or url.startswith('https://')):
                url = base_url + url
                play_item['url'] = url

    def get_result(self):
        return self.__res


def decode(file, base_url):
    f = open(file)
    with f:
        lines = f.readlines()
    decoder = M3U8Decoder(lines)
    decoder.decode()
    decoder.normalization_play_list_url(base_url)
    return decoder.get_result()
