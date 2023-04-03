# inspect0r
download this file https://jupiter.challenges.picoctf.org/problem/41511/

## search for flags
 ```
 $ cat index.html | grep -e flag
	<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->

 ```

## where is the rest
using dev tools it's in the 'sources' tab and there are two more comments in the JS and CSS files

### 2/3 of the flag
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */

### 3/3 of the flag
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?832b0699} */

## here it is
Part of the flag (1/3 of it) ```picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}```