import os, optparse
from PIL import Image, ImageOps

def resizeAllImages(width,height,IMAGES_PATH, cropImage): 
    if(width == None and height == None):
        raise Exception("ERROR: A Width Or Height Must Be Specified")
    elif(cropImage and (width == None or height == None)):
        raise Exception("ERROR: crop enabled but WIDTH or HEIGHT are not specified. For croping images, BOTH must be specified.")
    else:
        # For Each Images
        for (dirpath, dirnames, filenames) in os.walk(IMAGES_PATH):
            if("resized" not in dirpath):
                # Create New Directory To Save Images
                new_directory = "resized-"
                if(width == None or height == None):
                    if(width ==  None):
                        new_directory += "X-" + str(height)
                    elif(height == None):
                        new_directory += str(width) + "-X"
                else:
                    new_directory += str(width) + "-" + str(height)
                if(cropImage):
                    new_directory += "-Cropped"
                if not os.path.exists(os.path.join(dirpath, new_directory)):
                    os.makedirs(os.path.join(dirpath, new_directory))
                # Go Throuth All Images
                for fileName in filenames:
                    if(fileName[-3:] == "jpg" or fileName[-3:] == "png"):
                        if(fileName[-3:] == "jpg"):
                            fileType = "JPEG"
                        if(fileName[-3:] == "png"):
                            fileType = "PNG"
                        resizeImage(dirpath, os.path.join(dirpath,new_directory), fileName, width, height, fileType, cropImage)
# Declare Function
def resizeImage(imageLocation, imageDestinattionDirecotry, imageName, width, height, fileType, cropImage):
    # Declare Outfile
    outfile = os.path.join(imageDestinattionDirecotry, imageName)
    # Get Image
    img = Image.open(os.path.join(imageLocation, imageName))
    # Calculate Size
    if(width == None and height == None):
        raise Exception("ERROR: A Width Or Height Must Be Specified")
    elif(width == None or height == None):
        if(cropImage):
            raise Exception("ERROR: crop enabled but WIDTH or HEIGHT are not specified. For croping images, BOTH must be specified.")
        if(width == None):
            proportion = (height/float(img.size[1]))
            width = int((float(img.size[0])*float(proportion)))
        elif(height == None):
            proportion = (width/float(img.size[0]))
            height = int((float(img.size[1])*float(proportion)))
        size = width, height
    else:
        size = width, height
    print size
    # If Crop Image
    if(cropImage):
        img = ImageOps.fit(img, size, Image.ANTIALIAS)
    else:
        img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, fileType)
# Set up Get Opts
def main():
    # OPTIONS PARSER
    def resizeImages(option, opt, value, parser):
        # Parse Width and Height
        if(parser.values.resizeWidth):
            width = parser.values.resizeWidth
        else:
            width = None
        if(parser.values.resizeHeight):
            height = parser.values.resizeHeight
        else:
            height = None
        # Find Images Path
        if(parser.values.imagesDirectory):
            IMAGES_PATH = parser.values.imagesDirectory
        else:
            IMAGES_PATH = os.path.join(os.getcwd(),"images")
        # Crop
        if(parser.values.cropImage):
            cropImage = parser.values.cropImage
        else:
            cropImage = False
        resizeAllImages(width,height,IMAGES_PATH, cropImage)        

    parser = optparse.OptionParser()
    parser.add_option("-w", "--width",  type="int", dest="resizeWidth", help="Set the WIDTH at which the images will be resized.")
    parser.add_option("-j", "--height", type="int", dest="resizeHeight", help="Set the HEIGHT at which the images will be resized.")
    parser.add_option("-d", "--directory", type="int", dest="imagesDirectory", help="Set the DIRECTORY where the images are located. DEFAULT is CWD of script.")
    parser.add_option("-c", "--crop", action="store_true", dest="cropImage", help="Set the if (given a height and width) images will be cropped to that size.")
    parser.add_option("-r", "--resize", action="callback", callback=resizeImages, help="Call This function with a width or height to resize images.")
    (options, arguments) = parser.parse_args()

    if options is None:
        print "A mandatory option is missing"
        parser.print_help()
        print "Options Provided:"
        print options
    exit(-1)
    # Declare New Path

if __name__ == "__main__":
    main()