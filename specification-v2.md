# mig specification v1.2

Any .mig should follow the following:
```mig
<width> <height>
<pixel information>
```
every pixel should follow the [hex color format](https://www.w3schools.com/colors/colors_hexadecimal.asp), with 2 proceding hex values indicating transparency/opacity

hex aarrggbb

# what is a pixel in mig?
this is a red pixel in mig:
`#ffff0000`
this is a 1x2(width, height) image
```mig
1 2
#ffff0000
#ffff0000
```

# should any error arise?

yes, in fact, if the header, or the pixel data is missing, mig should throught a parsing error

# what about metadata? like titles

currently mig dosent support them, because they can be a hastle to parse, when compared to numbers, **but**, in the future, mig could support them


# editor support?

given how simple a .mig is, you should/could be able to whip out a editor(html, python, etc) for it in like, 20 minutes max

# how do i structure a image in mig?

example:
```mig
16 16
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000#ffff0000
```
