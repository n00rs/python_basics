'''
module = a file containg code you want to include in program
        use import to include a module (built in or you own module)
        useful to break up a large program reusable to separate FILES
'''

# in built modules are
# print(help("modules"))
'''
"_weakrefset",         "gettext",               "queue",
"_xxinterpchannels",   "gi",                    "quopri",
"_xxsubinterpreters",  "glob",                  "random",
"_xxtestfuzz",         "graphlib",              "random_modules",
"_yaml",               "grp",                   "re",
"_zoneinfo",           "gzip",                  "readline",
"abc",                 "hashlib",               "reprlib",
"aifc",                "heapq",                 "requests",
"antigravity",         "hmac",                  "resource",
"apport",              "hpmudext",              "rich",
"apport_python_hook",  "html",                  "rlcompleter",
"apt",                 "http",                  "runpy",
"apt_inst",            "httplib2",              "scanext",
"apt_pkg",             "idna",                  "sched",
"aptdaemon",           "if_statements",         "secrets",
"aptsources",          "imaplib",               "select",
"argparse",            "imghdr",                "selectors",
"array",               "importlib",             "serial",
"ast",                 "input",                 "shelve",
"asyncio",             "inspect",               "shlex",
"atexit",              "io",                    "shutil",
"attr",                "ipaddress",             "signal",
"attrs",               "iterables",             "site",
"audioop",             "itertools",             "sitecustomize",
"babel",               "janitor",               "six",
"base64",              "jinja2",                "smtplib",
"bcc",                 "json",                  "sndhdr",
"bdb",                 "jsonpatch",             "socket",
"binascii",            "jsonpointer",           "socketserver",
"bisect",              "jsonschema",            "softwareproperties",
"blinker",             "jwt",                   "speechd",
"brlapi",              "keyword",               "speechd_config",
"builtins",            "language_support_pkgs", "spwd",
"bz2",                 "launchpadlib",          "sqlite3",
"cProfile",            "linecache",             "sre_compile",
"cairo",               "locale",                "sre_constants",
"calendar",            "logging",               "sre_parse",
"certifi",             "logical_operator",      "ssl",
"cgi",                 "loops",                 "stat",
"cgitb",               "louis",                 "statistics",
"chardet",             "lzma",                  "string",
"chunk",               "mailbox",               "string_methods",
"click",               "mailcap",               "stringprep",
"cloudinit",           "markdown_it",           "struct",
"cmath",               "markupsafe",            "subprocess",
"cmd",                 "marshal",               "sunau",
"code",                "matchcase",             "symtable",
"codecs",              "math",                  "sys",
"codeop",              "math_fun",              "sysconfig",
"collection",          "mdurl",                 "syslog",
"collections",         "mimetypes",             "systemd",
"colorama",            "mmap",                  "tabnanny",
"colorsys",            "modulefinder",          "tarfile",
"compileall",          "modules",               "telnetlib",
"concurrent",          "multiprocessing",       "tempfile",
"configobj",           "netaddr",               "termios",
"configparser",        "netifaces",             "test",
"contextlib",          "netplan",               "textwrap",
"contextvars",         "netrc",                 "this",
"copy",                "nntplib",               "threading",
"copyreg",             "ntpath",                "time",
"crypt",               "nturl2path",            "timeit",
"cryptography",        "numbers",               "token",
"csv",                 "oauthlib",              "tokenize",
"ctypes",              "olefile",               "tomllib",
"cups",                "opcode",                "trace",
"cupsext",             "operator",              "traceback",
"cupshelpers",         "optparse",              "tracemalloc",
"curses",              "orca",                  "tty",
"dataclasses",         "os",                    "turtle",
"datetime",            "ossaudiodev",           "types",
"dateutil",            "pathlib",               "typing",
"dbm",                 "pcardext",              "typing_extensions",
"dbus",                "pdb",                   "uaclient",
"deb822",              "perf",                  "ufw",
"debconf",             "pexpect",               "unicodedata",
"debian",              "pickle",                "unittest",
"debian_bundle",       "pickletools",           "urllib",
"decimal",             "pipes",                 "urllib3",
"defer",               "pkg_resources",         "uu",
"dice",                "pkgutil",               "uuid",
"dictionaries",        "platform",              "validate",
"difflib",             "plistlib",              "variables",
"dis",                 "poplib",                "venv",
"distro",              "posix",                 "wadllib",
"distro_info",         "posixpath",             "warnings",
"doctest",             "pprint",                "wave",
"email",               "problem_report",        "weakref",
"encodings",           "profile",               "webbrowser",
"enum",                "pstats",                "wsgiref",
"errno" ,              "pty",                   "xdg",
"excersie_"!,          "ptyprocess",            "xdrlib",
"faulthandler",        "pvectorc",              "xkit",
"fcntl",               "pwd",                   "xml",
"filecmp",             "py_compile",            "xmlrpc",
"fileinput",           "pyclbr",                "xxlimited",
"fnmatch",             "pydoc",                 "xxlimited_35",
"for_loop",            "pydoc_data",            "xxsubtype",
"fractions",           "pyexpat",               "yaml",
"ftplib",              "pygments",              "zipapp",
"functions",           "pygtkcompat",           "zipfile",
"functools",           "pyparsing",             "zipimport",
"gc",                  "pyrsistent",            "zlib",
"genericpath",         "pysss",                 "zoneinfo",
"getopt",              "pysss_murmur",        
"getpass",             "pytz",                
'''

# to import 
# import math
# import with alias
# import math as Math
# import an function from module
# from math import e

# print(Math.pi)
# here e is overidden
# a,b,c,d,e = 1,2,3,4 ,5
# print(e**a,e**b,e**c,e**d)


import math

pi = math.pi

def square(int_num:int):
    return int_num ** 2

def cube(int_num:int):
    return int_num ** 3

def circumference(dbl_radius:float):
    return 2* pi* dbl_radius

def area(dbl_radius:float):
    return pi * dbl_radius ** 2
