 # Problem 1 - Obedient Cat
## Description
This file has a flag in plain sight (aka "in-the-clear"). Download flag.

link to file
https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag

## Solutoin
```bash
operator99@clamshell obedientcat $ wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag
--2023-03-31 21:14:48--  https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: ‘flag’

flag                      100%[==================================>]      34  --.-KB/s    in 0s      

2023-03-31 21:14:50 (6.71 MB/s) - ‘flag’ saved [34/34]


operator99@clamshell obedientcat $ file flag 
flag: ASCII text

operator99@clamshell obedientcat $ cat flag 
picoCTF{s4n1ty_v3r1f13d_2aa22101}

```
