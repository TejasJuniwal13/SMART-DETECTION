

import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

input_video = "input/videos/cow1.mp4"

output_video = "output/videos/output.mp4"

cap = cv2.VideoCapture(input_video)

if not cap.isOpened():

    print("Error opening video")

    exit()

# width
frame_width = int(
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
)

# height
frame_height = int(
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
)

# fps
fps = int(
    cap.get(cv2.CAP_PROP_FPS)
)

# video codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# output writer object
writer = cv2.VideoWriter(
    output_video,
    fourcc,
    fps,
    (frame_width, frame_height)
)

while True:

    ret, frame = cap.read()

    # video ended
    if not ret:
        break

    results = model(frame)

    result = results[0]

    boxes = result.boxes

    for box in boxes:

        # class id
        class_id = int(box.cls[0])

        # class name
        class_name = model.names[class_id]

        # confidence score
        confidence = float(box.conf[0])

        if class_name == "cow" and confidence > 0.5:

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            cv2.rectangle(
                frame,
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
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    writer.write(frame)

    cv2.imshow(
        "Cow Detection Video",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

writer.release()

cv2.destroyAllWindows()

print(
    f"Processed video saved at: "
    f"{output_video}"
)


