## 1 Watermark

In this project i choose to work with a image from the lab called etretat.jpg and a PNG picture of the University
logo my code is consist of 2 classes the main class "watermark" and the class "method"

### 1.1 class method

consist of:

**1.1.1 openImage**

**1.1.2 showImage**

**1.1.3 saveImage**

**1.1.4 getshape**

**1.1.5 getshape**

**1.1.6 resize**

to change the size of the watermark i choose (100,100) but its changeable

**1.1.7 getposition**

to get the position where we want to put the watermak
1 topleft
2 bottomleft
3 topright
4 bottomright
5 center

**1.1.8 watemark**

we need to give this function 4 attribute the name of the image the name of the watermark , the position we
want and the name of how we want to save the file.
this function is gonna convert the file from jpg and png to RGBA (red ,green, blue, alpha) alpha is for the
transparency.
it will create a new image on the form RGBA and past the image on the position (0,0) then the water mark on the
position we want, then change the format to RGB so we can save it as a jpg.

### 1.2 Class watermark

it contain the main that call the watermark function from method class.
This way we can do different image with different logo on different position at the same time.
