import argparse
import os
import cv2
from ultralytics import YOLO

base_dir = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description="Run YOLO object detection on a video file or webcam.")
parser.add_argument("--input", default="summer.mp4", help="Input video path or 0 for webcam")
parser.add_argument("--output", default="output.mp4", help="Output video path")
args = parser.parse_args()

local_yolo11 = os.path.join(base_dir, "yolo11n.pt")
local_yolo10 = os.path.join(base_dir, "yolo10n.pt")
if os.path.exists(local_yolo11):
    model_source = local_yolo11
elif os.path.exists(local_yolo10):
    model_source = local_yolo10
else:
    model_source = "yolo11n.pt"

input_value = args.input
if input_value == "0":
    input_source = 0
else:
    input_source = input_value if os.path.isabs(input_value) else os.path.join(base_dir, input_value)

output_path = args.output if os.path.isabs(args.output) else os.path.join(base_dir, args.output)

if input_source != 0 and not os.path.exists(input_source):
    raise FileNotFoundError(f"Input video not found: {input_source}. Pass --input 0 for webcam or provide a valid video file.")

model = YOLO(model_source)
model.to("cpu")

capture = cv2.VideoCapture(input_source)
if not capture.isOpened():
    raise RuntimeError(f"Could not open input source: {input_source}")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv2.CAP_PROP_FPS))

if width == 0 or height == 0 or fps == 0:
    if input_source == 0:
        fps = 30
    else:
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