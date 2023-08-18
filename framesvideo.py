import cv2
video = cv2.VideoCapture('drone.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)


minutes = 0
maxseconds = round(frames / fps)


for seconds in range(0, maxseconds+1):


    frame_id = int(fps*(minutes*60 + seconds))
    print('frame id =',frame_id)

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()

    cv2.imshow('frame', frame); cv2.waitKey(0)
    cv2.imwrite('my_video_frame.png', frame)

'''

216 frames

'''