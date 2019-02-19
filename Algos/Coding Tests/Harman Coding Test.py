'''
Problem Statement: There are different types of files located in the file location that will be provided. You are to wap to find all the .csv files having current month initials in its name and then check two conditions:
1) If the file size is 0MB,then raise a user defined exception and then send a mail reporting the exception
2) If the file has less than 5MB, then raise another user defined exception and then send a mail reporting the exception
'''
import os
import datetime
import sys


def mail(x, file):
    print('mailed the error: ' + x + ' for the file: ' + file.split('\\')[-1])


class dataNotFound(Exception):
    def __init__(self, file):
        print('dataNotFound')
        mail('dataNotFound', file)

    # pass


class lowDataFound(Exception):
    pass


def getFiles(month, loc=r'E:\temp'):
    files = []
    for i, _, j in os.walk(loc):
        for k in j:
            if month in k and '.csv' in k:
                # yield (os.path.join(i, k))
                files.append(os.path.join(i, k))
    return files


def checkFileSize(file):
    if os.stat(file).st_size > 10 * 1024:
        try:
            raise dataNotFound(file)
        except dataNotFound:
            pass
            # print('dataNotFound')
            # mail('dataNotFound', file)
    else:
        try:
            raise lowDataFound
        except lowDataFound:
            print('lowDataFound')
            mail('dataNotFound', file)


if __name__ == '__main__':
    month = datetime.datetime.now().strftime("%b").upper()
    files = getFiles(month)
    for file in files:
        checkFileSize(file)


# if __name__ == '__main__':
#     month = datetime.datetime.now().strftime("%b").upper()
#     files = getFiles(month)
#     for _ in files:
#         print(next(files))
#     if len(sys.argv) > 1:
#         loc = sys.argv[1]
#         file = getFiles(month, loc)
#         for _ in file:
#             checkFileSize(file)
#     else:
#         file = getFiles(month)
#         for _ in file:
#             checkFileSize(file)
