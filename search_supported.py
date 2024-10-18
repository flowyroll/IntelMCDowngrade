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
    print(regs['eax'])
    return regs['eax'] 


def main():
    c = 0
    _id = hex(cpuid())[2:].zfill(8).upper()
    print ("[!] Searching for supported microcodes...")
    for line in glob.glob("Intel/*"):
        tag = "Intel/cpu%s"%_id
        if line.startswith(tag):
            print("\t", c, line)
            c += 1

    for line in glob.glob("AMD/*"):
        tag = "AMD/cpu%s"%_id
        if line.startswith(tag):
            print(line)
            print("\t", c, line)
            c += 1


if __name__ == "__main__":
    main()
