# -*- coding:utf-8 -*-

from xmlrpc import client

def main():
    proxy = client.ServerProxy('http://127.0.0.1:7001')
    print(proxy.addtogether('x', 'y', 'z'))
    print(proxy.addtogether(20, 30, 4, 1))
    print(proxy.quadratic(2, -4, 0))
    print(proxy.quadratic(1, 2, 1))
    print(proxy.remote_repr((1, 2.0, 'three')))
    print(proxy.remote_repr([1, 2.0, 'three']))
    print(proxy.remote_repr({'name': 'Arthur',
                             'data': {'age': 42, 'sex': 'M'},
                             }))
    print(proxy.quadratic(1, 0, 1))


if __name__ == '__main__':
    main()