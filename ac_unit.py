#!/usr/bin/env python3
# pylint: disable=C0301,C0111

"""
An example of a script for turning an AC unit on/off via Flipper Zero.

Usage: python ac_unit.py
"""

import argparse
import sys
from pyflipper.pyflipper import PyFlipper

SAMPLES_POWEROFF = [12103, 5153, 651, 424, 706, 1860, 652, 424, 707, 1865, 653, 426, 705, 1860, 652, 425, 706, 1868, 650, 425, 653, 424, 707, 1860, 704, 1866, 653, 425, 653, 426, 652, 426, 704, 1867, 652, 426, 652, 427, 651, 426, 652, 433, 651, 426, 652, 427, 651, 425, 653, 433, 652, 427, 651, 426, 652, 427, 651, 434, 650, 427, 651, 1913, 651, 1914, 650, 1921, 650, 428, 650, 427, 651, 427, 651, 433, 651, 427, 651, 428, 650, 426, 652, 434, 598, 480, 650, 428, 598, 480, 598, 487, 650, 428, 597, 481, 597, 481, 597, 486, 651, 427, 599, 479, 599, 480, 651, 1920, 599, 479, 599, 481, 597, 481, 650, 1920, 651, 1915, 597, 480, 598, 479, 599, 486, 651, 1913, 599, 478, 600, 480, 598, 488, 599, 480, 650, 428, 651, 1912, 600, 490, 597, 481, 650, 1913, 651, 1914, 650, 436, 651]

SAMPLES_POWERON = [12079, 5177, 544, 531, 600, 1966, 545, 531, 600, 1973, 568, 509, 599, 1965, 570, 509, 599, 1972, 569, 509, 569, 507, 601, 1966, 622, 1949, 569, 507, 571, 508, 623, 1941, 624, 1949, 569, 509, 569, 509, 569, 507, 571, 514, 571, 508, 570, 508, 570, 507, 571, 514, 571, 508, 570, 510, 568, 508, 570, 514, 571, 508, 623, 1941, 624, 1942, 623, 1949, 569, 509, 569, 508, 570, 507, 571, 514, 570, 509, 569, 507, 571, 508, 570, 515, 570, 507, 571, 507, 571, 508, 570, 513, 572, 506, 572, 508, 570, 508, 570, 513, 572, 508, 570, 506, 572, 508, 623, 1947, 571, 508, 570, 509, 569, 508, 623, 1949, 599, 1968, 567, 509, 569, 509, 569, 514, 600, 1966, 569, 509, 568, 510, 546, 539, 548, 532, 546, 531, 600, 1965, 547, 541, 598, 1965, 547, 532, 546, 532, 546, 540, 547]

def main():
    parser = argparse.ArgumentParser(description="Control AC via Flipper Zero")
    parser.add_argument("action", choices=["on", "off"], help="Turn AC on or off")
    parser.add_argument("--port", default="/dev/ttyACM0", help="Flipper Zero port")
    args = parser.parse_args()
    
    try:
        flipper = PyFlipper(com=args.port)
        samples = SAMPLES_POWERON if args.action == "on" else SAMPLES_POWEROFF
        flipper.ir.tx_raw(frequency=38000, duty_cycle=0.33, samples=samples)
        print(f"AC turned {args.action}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
