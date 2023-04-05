# Wireshark doo dooo do doo...
Had no clue how to search properly in wireshark and clearly all the other writeupds just guessed or spent way too much time manually looking through the file

## Attempts
Tried ```ctrl + f``` but had no luck finding flag or pico
Googled it and people had not said how they found the right flag for them but they just 'followed tcp stream' which seems stupid to me, so inefficient.

## Time to learn regex, yay but also yuck
Basically I know a flag will be 7 [a-z] characters and then and unknown number of ```{[a-z][0-9]}``` so i need to match that pattern

```bash
[a-z]{7}{[^<>]+}
```

This will first match 7 characters between a-z and then any number of anything between {}. You could also use ```{.+?}``` but that's supposedly 'bad' or something so I just did what the internet man said at 

## Flag
Flag ended up being ```Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}``` which is shifted by 13 characters, aka ROT13
You could put some deoderant on and get sweaty writing this in python or you could just google it

### Working smarter
Website: https://rot13.com/

Answer: ```picoCTF{p33kab00_1_s33_u_deadbeef}```