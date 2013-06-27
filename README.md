CO+LAB - Exercises
==============

A couple of programming exercises for CO+LAB.

## Iteration

After sitting for about an hour in the computer, I finally figured this out. No Google, I promise! Basically, I went the recurrsion route, passing a long a list of the parent keywords and when there was no more child anymore, that meant that the combination was finished and was then added to an array. I then tested both methods (Manual and Programatic) to see if they matched.

I bet there's an easier way to do it, but that's who I figured it out.

	def superFunction(options, level, listOfoptions):
	    global finalListOfOptions
	    finalListOfOptions   = []
	    def goThroughEachOne(options, level, listOfoptions):
	        global finalListOfOptions
	        if(level < len(options)):
	            # print "Option Exists - ", level
	            for option in options[level]:
	                try:
	                    listOfoptions[level] = (option)
	                except:
	                    listOfoptions.append(option)
	                goThroughEachOne(options, level + 1, listOfoptions)
	        else:
	            # This is probably the ugliest part of the whole thing, but, for some reason. .append(listOfoptions) wasn't working for me
	            finalListOfOptions.append([])
	            finalListOfOptions[len(finalListOfOptions) - 1].extend(listOfoptions)

	    goThroughEachOne(options, level, listOfoptions)
	    return finalListOfOptions

## Radius

I was a little scared of this one yesterday, but thinking about it yesterday night I figured the answer was quite simple. Given that the diameter is nothing more than an infinite number of lines at distance R (radius), then the radius would always be greater than the distance of the point to any given point insinde the circle. I'm not now sure if that was the quesiton I was being asked, so I apologize if I answered an easier question than the one given to me. Google helped me confirm if what I was thinking was right: <http://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle>.

The python version is ok, but it's not that interesting, so I made a [Processing](http://processing.org/) example. To view that one you have to download the Processing software or you can see a canvas based HTML5 version here: <http://thejsj.com/2013/colab/Radius/Radius-Processing/web-export/>. In this example, there is a point class with and X and Y variable and a BasePoint class with a radius. If the point is within the diameter of that circle (drawn with a red stroke), then the script draw an ellipse around the point. It's interactive so you can change the radius or the position of the BasePoint with the mouse.

Again, this wasn't really too hard, so I apologize if this wasn't the question.

### Live Online Example:

http://thejsj.com/2013/colab/Radius/Radius-Processing/web-export/

## Image Resize

At 100 lines of code this is the longest one of all the excercise, yet I really leaned on PIL to do most of the complicated stuff. 

I created a simple command line interface for specifing width, height, if the images will be cropped and directory. So a command for the script would look something like this: 

	python imageResize.py --height 200 --width 200 --crop --resize

Resize being the base function that actually converts the images. I directory is not specified and default to the CWD of the script. Since I included a couple of images, this variable doesn't have to be specified. 

### Instructions

If given a Height OR a Width with no --crop flag, the script will resize all images to a height of 200, calculating the width based on image size. Example command:

	python imageResize.py --height 200 --resize

Example code for figuring out width or height: 

	if(width == None):
	    proportion = (height/float(img.size[1]))
	    width = int((float(img.size[0])*float(proportion)))
	elif(height == None):
	    proportion = (width/float(img.size[0]))
	    height = int((float(img.size[1])*float(proportion)))

If both, height AND width are given without the --crop flag, the images are resized to whatever is highest. If both width and height are set to 200 and the image has a width of 1000 and a height of 500, the image will be resized to 200 by 100. Example command: 

		python imageResize.py --height 200 --width 200 --resize

If both, heigh AND width are provided without the --crop flag, the images will be resized to that specifid height and width, cropping everything else. Example command: 

	python imageResize.py --height 200 --width 200 --crop --resize

### Possible Errors

If the user doesn't provide either width or height, the script throws an error: 

	raise Exception("ERROR: A Width Or Height Must Be Specified")

If the user provides only width or height, but adds the --crop flag, the script throw and error:

	raise Exception("ERROR: crop enabled but WIDTH or HEIGHT are not specified. For croping images, BOTH must be specified.")