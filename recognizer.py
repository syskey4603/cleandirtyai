from imageai.Classification.Custom import CustomImageClassification
import os
import cv2
import geocoder
import folium
import webbrowser
import os



coordlist = []




path_model = "cleandirty/models/resnet50-cleandirty-test_acc_0.82609_epoch-82.pt"  
path_input = "cleanstreet.jpg"  
path_json = "cleandirty/models/cleandirty_model_classes.json"  

execution_path = os.getcwd()

prediction = CustomImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, path_model))
prediction.setJsonPath(os.path.join(execution_path, path_json))
prediction.loadModel()
print(os.path.join(execution_path, path_input))

def genmap(coordlist):
  #print(coordlist)
  m = folium.Map(coordlist[0], zoom_start=13)

  tooltip = "Click me!"

  for coords in coordlist:

    folium.Marker(
        coords, 
        popup="<i>Mt. Hood Meadows</i>", 
        tooltip=tooltip, 
        icon=folium.Icon(color="red", icon="trash"),
    ).add_to(m)

  m.save("index.html")  

  filename = 'file:///'+os.getcwd()+'/' + 'index.html'
  webbrowser.open_new_tab(filename)


# for camera takes 10 images checks for each
def camrun(filename, resultcount, picnum):
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)   
    for x in range(0, picnum):
        s, img = cam.read()
        if s:
            cv2.namedWindow("cam-test")
            cv2.imwrite(filename,img)
        else:
            print("No image detected. Please! try again")
        predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, filename), result_count=resultcount)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction , " : " , eachProbability)
            if(eachPrediction == "dirty"):
                g = geocoder.ip('me')
                
                
                latlonglist = []
                for z in range(0, len(g.latlng)):
                    latlonglist.append(g.latlng[z])
                coordlist.append(latlonglist)


    if(coordlist != []):
        genmap(coordlist)


def preimage(filename, resultcount):
    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, filename), result_count=resultcount)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
        if(eachPrediction == "dirty"):
                g = geocoder.ip('me')
                
                
                latlonglist = []
                for z in range(0, len(g.latlng)):
                    latlonglist.append(g.latlng[z])
                coordlist.append(latlonglist)


    if(coordlist != []):
        genmap(coordlist)


def previd(filename, vidname, resultcount):
    video = cv2.VideoCapture(vidname)

    fps = video.get(cv2.CAP_PROP_FPS)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)


    minutes = 0
    maxseconds = round(frames / fps)

    for seconds in range(0, maxseconds+1):


        frame_id = int(fps*(minutes*60 + seconds))
        print('frame id =',frame_id)

        video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = video.read()

        #cv2.imshow('frame', frame); cv2.waitKey(0)
        cv2.imwrite(filename, frame)
        predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, filename), result_count=resultcount)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction , " : " , eachProbability)
            if(eachPrediction == "dirty"):
                g = geocoder.ip('me')
                
                
                latlonglist = []
                for z in range(0, len(g.latlng)):
                    latlonglist.append(g.latlng[z])
                coordlist.append(latlonglist)


    if(coordlist != []):
        genmap(coordlist)


def mainfunc():
    print("Take pictures from camera type camera")
    print("use pre-existing image type preimage")
    print("use pre-existing video type prevideo")
    choice = input("Choose an option: ")
    resultcount = int(input("Number of predictions: "))


    if(choice == "camera"):
        camrun("camerafile.jpg", resultcount, 10)
        continchoice()
    elif(choice == "preimage"):
        filename = input("enter file name of image include file type: ")
        preimage(filename, resultcount)
        continchoice()
    elif(choice == "prevideo"):
        vidfilename = input("enter file name of the video include file type: ")
        previd("vidimg.jpg", vidfilename, resultcount)
        continchoice()


def continchoice():
    choiceforcontinue = input("Do you want to continue? (y/n): ")

    if(choiceforcontinue == "y"):
        mainfunc()
    else:
        return
    

mainfunc()
