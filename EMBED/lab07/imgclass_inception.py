import numpy as np
import time
import cv2

# Define paths to the test image, to the model source files,
# and to the labels file. The labels file includes all 1000
# classes from the ImageNet database (out model was trained)
image_path = "/home/dani/EMBED/lab07/honda_adv.png"
label_path = "/home/dani/EMBED/lab07/imagenet_labels.txt"
model_path = "/home/dani/EMBED/lab07/googlenet.onnx"

# Read image from disk. Read all lines from the labels file into a list.
# Extract relevant class names from lines.
image = cv2.imread(image_path)
rows = open(label_path).read().strip().split("\n")
classes = [r.split(",")[0] for r in rows]

# The used classifier model requires fixed spatial dimensions for
# the input image. We use the blobFromImage() function to resize and
# normalize the image. At the end of the command, the output shape is (1, 3, 224, 224)
blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))

# Load model from disk:
print("Loading model...")
net = cv2.dnn.readNetFromONNX(model_path)

# Send the test image (blob) through the model to obtain classification result
net.setInput(blob)
start = time.time()
preds = net.forward()
end = time.time()
print("Classification time: {:.5} seconds".format(end - start))

# Sort predictions (class probabilities) descending order and
# extract the top 5 predictions
idxs = np.argsort(preds[0])[::-1][:5]

# Loop over the top 5 predictions. Print out the higher prediction's
# class name to the image
for (i, idx) in enumerate(idxs):
    if i == 0:
        text = "Label: {}, {:.2f}%".format(classes[idx], preds[0][idx] * 100)
        cv2.putText(image, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print("{}. label: {}, probability: {:.5}".format(i + 1, classes[idx], preds[0][idx]))
        
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
