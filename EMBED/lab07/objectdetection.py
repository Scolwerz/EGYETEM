import numpy as np
import cv2

# Define paths to the model and the test image
model_path = "/home/dani/EMBED/lab07/mobilenet.onnx"
image_path = "/home/dani/EMBED/lab07/biciklis.png"

# Define a confidence threshold to filter out less certain predictions
conf_limit = 0.25

# Create a dictionary with class labels and ids our model was trained.
# Those labels will be used to image annotation.
CLASSES = {
    1: "person",
    2: "bicycle",
    3: "car",
    4: "motorcycle",
    5: "airplane",
    6: "bus",
    7: "train",
    8: "truck",
    9: "boat",
    10: "traffic light",
    11: "fire hydrant",
    13: "stop sign",
    14: "parking meter",
    15: "bench",
    16: "bird",
    17: "cat",
    18:"dog",
    19: "horse",
    20: "sheep",
    21: "cow",
    22: "elephant",
    23: "bear",
    24: "zebra",
    25: "giraffe",
    27: "backpack",
    28: "umbrella",
    31: "handbag",
    32: "tie",
    33: "suitcase",
    34: "frisbee",
    35: "skis",
    36: "snowboard",
    37: "sports ball",
    38: "kite",
    39: "baseball bat",
    40: "baseball glove",
    41: "skateboard",
    42: "surfboard",
    43: "tennis racket",
    44: "bottle",
    46: "wine glass",
    47: "cup",
    48: "fork",
    49: "knife",
    50: "spoon",
    51: "bowl",
    52: "banana",
    53: "apple",
    54: "sandwich",
    55: "orange",
    56: "broccoli",
    57: "carrot",
    58: "hot dog",
    59: "pizza",
    60: "donut",
    61: "cake",
    62: "chair",
    63: "couch",
    64: "potted plant",
    65: "bed",
    67: "dining table",
    70: "toilet",
    72: "tv",
    73: "laptop",
    74: "mouse",
    75: "remote",
    76: "keyboard",
    77: "cell phone",
    78: "microwave",
    79: "oven",
    80: "toaster",
    81: "sink",
    82: "refrigerator",
    84: "book",
    85: "clock",
    86: "vase",
    87: "scissors",
    88: "teddy bear",
    89: "hair drier",
    90: "toothbrush",
}

# Generate as many random colors as the number of classes. Each class will be marked
# with its own color on the test image
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Load the pre-trained model from your disk
print("Loading model...")
net = cv2.dnn.readNetFromONNX(model_path)

# Load the image from your storage and construct an input blob.
# The blobFromImage() function is optionally resize, crop, subtract mean,
# scale, and swap channels in the input image
image = cv2.imread(image_path)

# BGR to RGB channel conversion
image = cv2.resize(image, (800, 500))
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
(h, w) = rgb_image.shape[:2]

# uint8 data type and (1, 800, 500, 3) dimensions
input_tensor = np.expand_dims(rgb_image.astype(np.uint8), axis=0)

# Send the test image through the object detector model.
print("Sending image through the network...")
output_names = net.getUnconnectedOutLayersNames()
net.setInput(input_tensor)
output_values = net.forward(output_names)

# take out detection information from the model's output
num_detections = output_values[3][0]
scores = output_values[2][0]
class_ids = output_values[1][0]
boxes = output_values[0][0]

# print out detections
print("# detections: {}\n".format(num_detections))
for i, s in zip(class_ids, scores):
    if s > 0.0:
        print("id: {} -- {}".format(i, s))
    else:
        break

# Loop over all detections and extract confidence (probability) values
for i in np.arange(0, len(scores)):
    # extract the confidence
    confidence = scores[i]
    # Filter out week detections with the earlier defined threshold value.
    if confidence > conf_limit:
        idx = int(class_ids[i])
        ymin, xmin, ymax, xmax = boxes[i]
        startX = int(xmin * w)
        startY = int(ymin * h)
        endX = int(xmax * w)
        endY = int(ymax * h)

        label = "{}: {:.2f}%".format(CLASSES.get(idx), confidence * 100)
        print("{}".format(label))

        cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
