
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


input_image = "input/images/cow1.jpg"

output_image = "output/images/cow1_output.jpg"



# openCV converts image to numpy array 
image = cv2.imread(input_image)

if image is None:

    print("Image not found")

    exit()

results = model(image)

# first result
result = results[0]

# detected objects
boxes = result.boxes


for box in boxes:

    
    class_id = int(box.cls[0])

    
    class_name = model.names[class_id]

    
    confidence = float(box.conf[0])


    if class_name == "cow" and confidence > 0.5:


        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )



        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )



        label = (
            f"{class_name} "
            f"{confidence:.2f}"
        )

        cv2.putText(
            image,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

cv2.imwrite(output_image, image)

print(
    f"Processed image saved at: "
    f"{output_image}"
)


cv2.imshow(
    "Cow Detection",
    image
)

cv2.waitKey(0)

cv2.destroyAllWindows()

