#!/usr/bin/env python3

from pwn import *

exe = ELF("./col_patched_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = ssh(user='col', host='pwnable.kr', port=2222, password='guest')

    return r


def main():
    r = conn()
    
    payload = p32(0x6c5cec8)*4 + p32(0x6c5cecc)
    p = r.process(executable='./col', argv=['col', payload])

    log.success('flag:{}'.format(p.recv()))

    p.interactive()


if __name__ == "__main__":
    main()
