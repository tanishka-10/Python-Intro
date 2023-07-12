length = int(input("What is the length?"))
width = int(input("What is the width?"))
height = int(input("What is the height?"))
def volume(length, width, height):
    return(length * width * height)


print(str("The volume of the rectangular prism is " +  str(volume(length, width, height)) + " cubic feet."))
