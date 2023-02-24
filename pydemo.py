#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, time

def main(argv):
    i=str(argv[1])
    o=str(argv[2])
    print('模拟跑了个处理python程序，传入的zip包是'+i)
    print('模拟等了1秒')
    time.sleep(1)
    try:
        f = open('./files/'+o, 'w')
        f.write('KANKAN IMG HERE')
    finally:
        if f:
            f.close()
    print('模拟跑完了，输出文件：'+o)

if __name__ == "__main__":
    main(sys.argv)