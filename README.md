# Object-Detection-using-python-and-opencv

Aim of the Project:- To Detect any contour of image section and trace it in real time.

Previous Knowledge :- 1. Python
                      2. Opencv version:- 2

Step 1 :- Color Filtering i.e. Conversion of BGR color space to HSV color space. Since this is a color based detection every color has a             HSV high and low values and hence is converted to a binary image using inrange function , after a mask is applied. The output             image was the bitwise and of the masked i.e binary image and the actual image highliting only the required color region we need.
          
Step 2 :- Still After the Color Filtering there is noise in the output image which is filtered by performing morfological operations :               Erode and Dilate Functions operated on the binary output image. Erode "Erodes" into Whitespace Area making it smaller or non-             Existent . Dilate makes the non-eroded white space larger.

Step 3 :- Find Contour where input is a binary filtered image and the output is a list of contours i.e the outline of all objects found in           the Binary image.And Draw the Contour region.

Finally The moment point is sent to Arduino And this region was mapped into the resl 2-D space.

Thank You!!
