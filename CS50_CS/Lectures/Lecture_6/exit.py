import sys

if len(sys.argv)!=2:
    sys.exit("Missing command-line argument")
print(f"Hello, {sys.argv[1]}")
sys.exit(0)

