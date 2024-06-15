import sys
if sys.platform in ["linux", "linux2", "win32", "win64"]:
    orange = "\033[93m"
    putih = "\033[39m"
    merah = "\033[91m"
    hijau = "\033[92m"
    biru = "\033[94m"
    borange = "\033[1;93m"
    bputih = "\033[1;39m"
    bmerah = "\033[1;91m"
    bhijau = "\033[1;92m"
    bbiru = "\033[1;94m"
    reset = '\033[0m'
else:
    orange = ""
    putih = ""
    merah = ""
    hijau = ""
    biru = ""
    borange = ""
    bputih = ""
    bmerah = ""
    bhijau = ""
    bbiru = ""
    reset = ''
