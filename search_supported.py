#!/usr/bin/env python3
import subprocess
import glob

def run_cmd(cmdstr):
    cmd = cmdstr.split()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    proc.wait()
    return proc.stdout.read().decode('utf8')

def cpuid():
    regs_raw = run_cmd("cpuid -l 1 -r -1").strip().split(":")[-1].strip().split()
    regs = {}
    for r in regs_raw:
        x = r.split('=')
        regs.update({x[0]: int(x[1], 16)})
    return regs['eax']


def main():
    c = 0
    _id = cpuid()
    print ("[!] Searching for supported microcodes...")
    for line in glob.glob("Intel/*"):
        tag = "Intel/cpu%s"%hex(_id)[2:].upper()
        if line.startswith(tag):
            print("\t", c, line)
            c += 1

if __name__ == "__main__":
    main()
