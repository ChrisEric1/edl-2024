#!/usr/bin/env python3
from edl.Library.tcpclient import tcpclient


class client:
    def __init__(self):
        self.commands = []

    def send(self):
        self.tcp = tcpclient(1340)
        self.tcp.sendcommands(self.commands)

    def read(self, src):
        self.commands.append(f"peekqword:{hex(src)}")

    def write(self, dest, value):
        self.commands.append(f"pokeqword:{hex(dest)},{hex(value)}")

    def memcpy(self, dest, src, size):
        self.commands.append(f"memcpy:{hex(dest)},{hex(src)},{hex(size)}")


def main():
    exp = client()
    exp.commands = [
        "send:nop",
        "r:boot,boot.img",
        "peek:0x00100000,0x8,qfp.bin"
        #"pokehex:0x1402C2CC,1f2003d5",
        #"peek:0x14084840,0xC00,uart.bin"
    ]
    exp.send()


if __name__ == "__main__":
    main()
