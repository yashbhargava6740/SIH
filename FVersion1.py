# Importing Required Modules, Functions and methods
from PIL import Image
from statistics import mode
import cv2

# Capturing Sample Image
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # CAP_DSHOW To avoid warnings
cv2.namedWindow("test")
img_name = ""
while True:
    ret, frame = cam.read()
    if not ret:
        print("Technical Issue")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Closed......")     # Exit on Escape
        break
    elif k % 256 == 32:
        img_name = "opencv_frame_0.jpg"    # Press Space To Capture
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        break
cam.release()

im = Image.open(img_name)
pix = list(im.getdata())
n = len(pix)
i = 0

# Main Algorithm
while(i < len(pix)):  # REMOVING WHITE PIXELS OR GRAY PIXELS
    p = pix[i]
    if(p[0] >= 140 and p[1] == p[2]):
        pix.pop()
    i += 1
l = mode(pix)

# Initializing Reoprts
alg, mud, bacteria, fit = "NO", "LOW", "Probably low", "Fit"
DO = "Normal"

if(l[0] > l[1] and l[0] > l[2]):  # CHECKING FOR REDDISH GREEN OR BROWN ALGAE
    if(l[0]-l[1] > 30):
        alg,mud,fit,DO = ["No", "Filterable", "After Filtaration", "Probably Decent"]
    elif(l[0]-l[1] > 70 and l[0]-l[2] > 70):
        alg,mud,fit,DO, bacteria = ["Red", "High", "Not", "Not Good", "High"]
    if(l[0] > 100 and l[1] > 100):
        if(l[0]-l[1] > 30):
            alg,mud,fit,DO, bacteria = ["Reddish Green", "High", "Not", "Not Good", "High"]
        elif(l[0]-l[1] > 10):
            alg,mud,fit,DO, bacteria = ["Greenish", "High", "Not", "Not Good", "High"]
    elif(l[0] > 200 and l[1] > 200):
        alg,mud,fit,DO, bacteria = ["Probably Low and Reddish Green", "Low But Exists", "Not", "Not Good", "High"]

if(l[1] > l[0] and l[1] > l[2]):  # CHECKING FOR REDDISH GREEN OR BROWN ALGAE
    if(l[0]-l[1] > 50):
        alg,mud,fit,DO = ["No", "Filterable", "After Filtaration", "Probably Decent"] 
    elif(l[1]-l[1] > 70 and l[0]-l[2] > 70):
        alg,mud,fit,DO, bacteria = ["Green", "High", "Not", "Not Good", "High"]
        
    if(l[0] > 100 and l[1] > 100):
        if(l[1]-l[2] > 50):
            alg,mud,fit,DO, bacteria = ["Greenish Red", "High", "Not", "Not Good", "High"]
        elif(l[1]-l[2] > 10):
            alg,mud,fit,DO, bacteria = ["Greenish", "High", "Not", "Not Good", "High"]       
    elif(l[0] > 200 and l[1] > 200):
        alg,mud,fit,DO, bacteria = ["Probably Low and Reddish Green", "Low But Exists", "Not", "Average", "High"]
print("Result:")
print("********")
print("BACTERIA : ", bacteria, "\nAlgae content :", alg,"\nMud content : ", mud, "\nDissoved Oxygen Status : ", DO)
print()
print("********************************")
print(f" Conclusion : {fit} for drinking ")
print("********************************")
