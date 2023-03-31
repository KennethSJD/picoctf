# Glory of the Garden
file to download and is 'more than it seems'

## First thoughts
Checking the file type finds nothing

```bash
$ file garden.jpg 

garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3
```

## Solution
Using bash:

```bash
$ strings garden.jpg | grep -e flag

Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"

```