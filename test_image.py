import cv2

# Load an image (replace 'your_image.jpg' with an actual image file in your project folder)
img = cv2.imread('falcao_futsal.png')

# Check if the image is loaded
if img is None:
    print("Error: Could not load image.")
else:
    # Display the image in a window
    cv2.imshow('Image', img)

    # Wait until any key is pressed to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
