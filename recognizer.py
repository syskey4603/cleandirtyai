from imageai.Classification.Custom import CustomImageClassification
import os
import cv2


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)   


video = cv2.VideoCapture('drone.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)


minutes = 0
maxseconds = round(frames / fps)

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


# for camera takes 10 images checks for each
for x in range(0, 10):
    s, img = cam.read()
    if s:
        cv2.namedWindow("cam-test")
        cv2.imwrite("filename.jpg",img)
    else:
        print("No image detected. Please! try again")
    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "filename.jpg"), result_count=2)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)


#for video upload

'''
for seconds in range(0, maxseconds+1):


    frame_id = int(fps*(minutes*60 + seconds))
    print('frame id =',frame_id)

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()

    #cv2.imshow('frame', frame); cv2.waitKey(0)
    cv2.imwrite('testing.jpg', frame)
    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "testing.jpg"), result_count=2)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)

'''

'''
for normal image
predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "image.jpg"), result_count=2)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)



'''











'''
from imageai.Classification.Custom import CustomImageClassification
import os

path_model = "models/resnet50-cleandirty-test_acc_0.76923_epoch-19.pt"  
path_input = "cleanstreet.jpg"  
path_json = "models/cleandirty_model_classes.json"  

execution_path = os.getcwd()

prediction = CustomImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, path_model))
prediction.setJsonPath(os.path.join(execution_path, path_json))
prediction.loadModel()
print(os.path.join(execution_path, path_input))
predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, path_input), result_count=1)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

'''


'''

from imageai.Classification.Custom import ClassificationModelTrainer

model_trainer = ClassificationModelTrainer()
model_trainer.setModelTypeAsResNet50()
model_trainer.setDataDirectory(r"C:/Users/vedan/OneDrive/Documents/Vedant/ai learn/hackathon proj/cleandirty")
model_trainer.trainModel(num_experiments=100, batch_size=32)


execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, path_model))
prediction.loadModel()


predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, path_input), result_count=10)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)


# using the setModelTypeAsTinyYOLOv3() function  
recognizer.setModelTypeAsTinyYOLOv3()  
# setting the path of the Model  
recognizer.setModelPath(path_model)  
# loading the model  
recognizer.loadModel()  
# calling the detectObjectsFromImage() function  
recognition = recognizer.detectObjectsFromImage(  
    input_image = path_input,  
    output_image_path = path_output  
    )  
  
# iterating through the items found in the image  
for eachItem in recognition:  
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])  '''
