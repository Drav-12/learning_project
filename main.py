# Load the YOLO model for object detection
model_od = YOLO("yolo11n.pt")  # pretrained YOLO11n model

# Request user input for the image path
image_input = input("Enter the path of the image you want to use (leave empty to exit): ")

if image_input:
    # Request user input for the basename
    basename = input("Enter the basename for the output files: ")

    # Run batched inference on the user-provided image for object detection
    results_od = model_od([image_input], stream=True)  # return a generator of Results objects

    # Process results for object detection
    for result in results_od:
        result.show()  # display to screen
        result.save(filename=f"{basename}_od.jpg")  # save to disk with "_od" suffix

    # Load the YOLO model for pose estimation
    model_pe = YOLO("yolo11n-pose.pt")  # load an official model for pose estimation

    # Predict with the model for pose estimation
    results_pe = model_pe(image_input)  # predict on the same image

    # Process results for pose estimation
    for result in results_pe:
        result.show()  # display to screen
        result.save(filename=f"{basename}_pe.jpg")  # save to disk with "_pe" suffix

print("Processing completed.")
