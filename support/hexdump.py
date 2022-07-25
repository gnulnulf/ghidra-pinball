# credits: https://www.geoffreybrown.com/blog/a-hexdump-program-in-python/
import sys
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("FILE", help="the name of the file that you wish to dump", type=str)
parser.add_argument("-b", "--binary", help="display bytes in binary format instead of hexadecimal", action="store_true")
args = parser.parse_args()

try:
    with open(args.FILE, "rb") as f:
        n = 0
        b = f.read(16)

        while b:
            if not args.binary:
                s1 = " ".join([f"{i:02x}" for i in b])
                s1 = s1[0:23] + " " + s1[23:]
                width = 48
            else:
                s1 = " ".join([f"{i:08b}" for i in b])
                s1 = s1[0:71] + " " + s1[71:]
                width = 144

            s2 = "".join([chr(i) if 32 <= i <= 127 else "." for i in b])

            print(f"{n * 16:08x}  {s1:<{width}}  |{s2}|") # parameterized width

            n += 1
            b = f.read(16)

    print(f"{os.path.getsize(args.FILE):08x}")

except Exception as e:
    print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)