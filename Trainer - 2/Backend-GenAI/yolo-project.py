import os
import cv2
from ultralytics import YOLO

base_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(base_dir, "yolo11n.pt") if os.path.exists(os.path.join(base_dir, "yolo11n.pt")) else os.path.join(base_dir, "yolov10n.pt")
input_path = os.path.join(base_dir, "summer.mp4")
output_path = os.path.join(base_dir, "output.mp4")

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Input video not found: {input_path}")

model = YOLO(model_path)
model.to("cpu")

capture = cv2.VideoCapture(input_path)
if not capture.isOpened():
    raise RuntimeError(f"Could not open video file: {input_path}")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv2.CAP_PROP_FPS))

if width == 0 or height == 0 or fps == 0:
    raise RuntimeError("Could not read video properties from the input file")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

if not out.isOpened():
    raise RuntimeError(f"Could not create output video: {output_path}")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    results = model.predict(frame, stream=False)
    annotated_frame = results[0].plot()
    out.write(annotated_frame)

    cv2.imshow("YOLO Video Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
out.release()
cv2.destroyAllWindows()
print(f"Output saved to {output_path}")