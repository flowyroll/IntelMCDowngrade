#!/usr/bin/env python3
import subprocess

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
    applicable_mc = []
    c = 0
    print ("[!] Searching for supported microcodes...")
    for line in run_cmd('ls Intel/').split("\n"):
        tag = "cpu%s"%hex(cpuid())[2:].upper()
        if line.startswith(tag):
            print("\t", c, line)
            applicable_mc.append(line)
            c += 1

if __name__ == "__main__":
    main()
