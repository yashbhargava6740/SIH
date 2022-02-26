from PIL import Image
from statistics import mode
import cv2
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
img_name = ""
while True:
    ret, frame = cam.read()
    if not ret:
        print("Technical Issue")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Closed......")     # Exit on Escape
        break
    elif k%256 == 32:
        img_name = f"opencv_frame_{img_counter}.jpg"    # Press Space To Capture
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        break
    
cam.release()


im =Image.open(img_name) # THIS HAS TO BE REPLACED WITH CAMERA FEATURE OR BROWSE FEATURE
pix = list(im.getdata())

n = len(pix)
i=0

while(i<len(pix)): #REMOVING WHITE PIXELS OR GRAY PIXELS
    p=pix[i]
    if(p[0]>=140 and p[1]==p[2]):
       
        pix.pop()
    i=i+1
        
l = mode(pix)


alg,mud,bacteria,fit = "NO","LOW","Probably low","Fit"
DO="Normal"

if(l[0]>l[1] and l[0]>l[2]):  #CHECKING FOR REDDISH GREEN OR BROWN ALGAE
    if(l[0]-l[1]>50):
        alg="No"
        mud="filtrable"
        fit="after filtration it is"
        DO=" Probably Decent"
    elif(l[0]-l[1]>70 and l[0]-l[2]>70):
        alg="Red"
        mud="high"
        fit="Not"
        DO="Not Good"
        bacteria = "high"
    if(l[0]>100 and l[1]>100):
        if(l[0]-l[1]>50):
            alg="reddish green"
            mud="high"
            DO="Not Good"
            fit="Not"
            bacteria = "high"
        elif(l[0]-l[1]>10):
            alg="Greenish"
            mud ="High"
            fit ="Not"
            Do="Not Good"
            bacteria = "high"
    elif(l[0]>200 and l[1]>200):
            alg = "Probably Low and Redish Green"
            mud ="Low but exists"
            fit ="Not"
            DO="Not Good"
            bacteria = "high"
    

if(l[1]>l[0] and l[1]>l[2]):  #CHECKING FOR REDDISH GREEN OR BROWN ALGAE
    if(l[0]-l[1]>50):
        alg="No"
        mud="filtrable"
        fit="after filtration it is"
        DO="Probably decent"
    elif(l[1]-l[1]>70 and l[0]-l[2]>70):
        alg="Green"
        mud="high"
        fit="Not"
        DO="Not good"
        bacteria = "high"
    if(l[0]>100 and l[1]>100):
        if(l[1]-l[2]>50):
            alg="Greenish red"
            mud="high"
            fit="Not"
            DO="Not good"
            bacteria = "high"
        elif(l[1]-l[2]>10):
            alg="Greenish"
            mud ="High"
            fit ="Not"
            DO="Not good"
            bacteria = "high"
    elif(l[0]>200 and l[1]>200):
            alg = "Probably Low and Redish Green"
            mud ="Low but exists"
            fit ="Not"
            DO="Average"
            bacteria = "high"
print("Results:")
print("********")
print("BACTERIA : ",bacteria,"\nAlgae content :",alg,"\nMud content : ",mud,"\nDissoved Oxygen Status : ",DO)
print()
print("********************************")
print(f" Conclusion : {fit} for drinking ")
print("********************************")
