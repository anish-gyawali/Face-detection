import cv2

# Load pre trained data on the face frontals from opencv
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')


# To capture video from webcam
# Here "0" is default if you wantto detect face from vide then write file name eg:"video.mp4"
camera_port = 0
camera = cv2.VideoCapture(camera_port)
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)


# Iterate forever over frames
while True:
    # Read the current frame
    successfull_frame_read, frame = camera.read()
    # convert image to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # draw rectangle around the face
    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # to show the image
    cv2.imshow('Your Image Is Detected Press Q to close ', frame)
    key = cv2.waitKey(1)
    # stop if "Q" is pressed
    if key == 81 or key == 113:
        break

"""


                    ##### To Detect face from image #####

# choose an image to detect face
#img = cv2.imread('eximg.jpg')

# convert image to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# draw rectangle around the face
for(x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# print(face_coordinates)

# to show the image
cv2.imshow('random person image', img)
cv2.waitKey()

"""


print("Your code is running successfully")
