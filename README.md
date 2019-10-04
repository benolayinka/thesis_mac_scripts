# thesis_mac_scripts

## Run lizard and get an estimate of computation cycles
python lizard/lizard.py source.c -Einstructioncount

## Compile source without optimization
clang source.c -O0

## Simulate and tabulate instructions for x86
python getinstr.py -b a.out
