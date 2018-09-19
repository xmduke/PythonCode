#!/usr/bin/env python3
#破解zip文件密码
#自己指定破解文件和字典，多线程破解
import zipfile
import threading
import optparse

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd = password)
        print("FoundPassword:", password)
        return password
    except:
        pass

def main():
    parser = optparse.OptionParser('usage%prog -f<zipfile>'
                                   '-d <dictionary>')
    parser.add_option('-f', dest = 'zname',
                      type = 'string',
                      help = 'specify zip file')
    parser.add_option('-d', dest = 'dname', type = 'string',
                      help = 'specify dictionary file')
    options, args = parser.parse_args()
    if options.zname == None | options.dname == None:
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    dFile = open(dname, 'r')

    for line in dFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target = extractFile,
                             args = (zFile, password))
        t.start()

if __name__ == '__main__':
  main()