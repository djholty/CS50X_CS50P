import os.path
import sys
from PIL import Image, ImageShow, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <3:
    sys.exit("Too few command-line arguments")
else:
    try:
        #treat case insensitivelyS
        sys.argv[1] = sys.argv[1].lower()
        sys.argv[2] = sys.argv[2].lower()
        #get filename and extension of command-line arguments
        fn1, ext1 = os.path.splitext(sys.argv[1])
        fn2, ext2 = os.path.splitext(sys.argv[2])
        #error check for proper extension in both files
        if ext1 not in ['.jpg','.jpeg','.png']:
            sys.exit('Invalid input')
        if ext2 not in ['.jpg','.jpeg','.png']:
            sys.exit('Invalid output')
        if ext1 != ext2.lower():
            sys.exit('Input and output have different extensions')
        if not os.path.exists(sys.argv[1]):
            sys.exit('Input does not exist')
        #create a shirt image object of the the shirt to overlay on image
        shirt = Image.open("shirt.png")

        #open the image to put the shirt on
        photo1 = Image.open(sys.argv[1])
        #resize and crop using ImageOps.fit
        resizedimg = ImageOps.fit(photo1, shirt.size)
        #paste the image of the shirt in place
        resizedimg.paste(shirt, mask=shirt) #pasts image over image but does it in place.  does not return a new image
        resizedimg.save(sys.argv[2])

    #must specify exactly 2 command-line arguments or sys.exit
    #must end in .jpg .jpeg or .png case-insensitive
    #input name has same extension as output name determined with os.path.splitext
    #input does not exists
    except ValueError:
        print("unable to open")