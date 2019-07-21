check_doublon
=============

check_doublon is a simple tool how can check if
two files have the same content, even if they have
differents names.
It works by comparing md5sums computed
by the content of the file.

It has been tested on Linux only.

usage
-----

1. launch 'install.sh' to create 'config.py'
2. add the path to the folder to check in the 'url' field in 'config.py'
3. add a name of application to read the files in the 'reader' field
4. launch 'check_doublon.py'. This can take a while.
5. launch 'launch.py'. All doublons files will be played and a prompt will
ask if the program can remove the file.

config.py example
-----------------

```
url = "/path/to/my/failed/save"
reader = "mpv"
```
