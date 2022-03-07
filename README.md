# UnWrap
#### A library that transforms one-line css into a readable format.
---
## How to use it:
```py
#yourfile.py
from unwrap import unwrapCSS
unwrapCSS("yourCSSfile.css",
    outputfile="outputfile.txt",
    indent=4)
```
```shell
#on the terminal/cmd:
python3 yourfile.py
```
---
## Examples:
```css

input file:

html{background: black}button:hover{color: gray}


output file:

html{
    background: black
}
button:hover{
    color: gray
}
```