from moviepy.editor import *


class VideoSplicer:
    def __init__(self, ts_list):
        self.__ts_list = ts_list
        self.__ts_files = []
        self.__res = None

    def __load_files(self):
        for file in self.__ts_list:
            print('Loading [%s]' % file)
            video = VideoFileClip(file)
            self.__ts_files.append(video)

    def concat(self):
        self.__load_files()
        print('Concat video ......')
        self.__res = concatenate_videoclips(self.__ts_files)

    def save(self, filename):
        print('Save result [%s]', filename)
        self.__res.to_videofile(filename, fps=24, remove_temp=False)
