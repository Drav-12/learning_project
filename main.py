from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # pretrained YOLO11n model

# Request user input
image_input = input("Enter the path of the image you want to use (leave empty to exit): ")

if image_input:
    # Run batched inference on a the user image
    results = model([image_input], stream=True)  # return a generator of Results objects

    # Process results generator
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen
        result.save(filename="result.jpg")  # save to disk

        # Load a model
    model = YOLO("yolo11n-pose.pt")  # load an official model

    # Predict with the model for the user image
    results = model(image_input)  # predict on an image

    for result in results:
        result.show()  # display to screen
        result.save(filename="result.jpg")  # save to disk