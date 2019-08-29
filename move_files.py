import os
import os.path


def main():
    root = 'E:/tmp/res'
    dirs = os.listdir(root)
    num = 0
    for d in dirs:
        file = os.path.join(root, d, 'result.mp4')
        if os.path.exists(file):
            os.rename(file, os.path.join('E:/tmp/res/res', str(num) + '.mp4'))
            num += 1


if __name__ == '__main__':
    main()
