import cv2

# Load pre trained data on the face frontals from opencv
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# choose an image to detect face
img = cv2.imread('eximg.jpg')


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
print("code Completed")
