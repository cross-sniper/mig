# mig specification v1.3

Any .mig should follow the following:
```mig
<width> <height>
<color palet>
<pixel information(A,B,C,...)>
```
every color in the pallet, should follow the [hex color format](https://www.w3schools.com/colors/colors_hexadecimal.asp), with 2 proceding hex values indicating transparency/opacity

hex aarrggbb

# what is a pixel in mig?
this is a red pixel on the color palet in mig:
`#ffff0000`
this is a 1x2(width, height) image
```mig
1 2
#ffff0000
A
A
```

# should any error arise?

yes, in fact, if the header, color palet, or the pixel data is missing, mig should throught a parsing error

# what about metadata? like titles

currently mig dosent support them, because they can be a hastle to parse, when compared to numbers, **but**, in the future, mig could support them


# editor support?

given how simple a .mig is, you should/could be able to whip out a editor(html, python, etc) for it in like, 20 minutes max

# how do i structure a image in mig?

example:
```mig
16 16
#ffff0000
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
```
