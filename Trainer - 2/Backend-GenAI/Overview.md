# 🎯 YOLO Video Object Detection — Project Overview

## 📌 What is this Project?

This project uses **YOLOv10/YOLOv11** (You Only Look Once), a state-of-the-art real-time object detection model, to process a video file frame-by-frame. It detects objects in each frame, annotates them with bounding boxes and labels, displays a live preview window, and saves the final annotated video to disk.

---

## 🗂️ Project Files

| File | Description |
|---|---|
| `yolo-project.py` | Main Python script — runs YOLO inference on a video |
| `yolov10n.pt` | Pre-trained YOLOv10 nano model weights |
| `yolo11n.pt` | Pre-trained YOLOv11 nano model weights (used if present) |
| `summer.mp4` | Input video file *(must be placed by user)* |
| `output.mp4` | Output annotated video *(auto-generated after running)* |

---

## ⚙️ How It Works

```
summer.mp4  ──►  [YOLO Model]  ──►  Annotated Frames  ──►  output.mp4
                      │
                      └──►  Live Preview Window (press Q to quit)
```

1. **Loads** the YOLO model (`yolo11n.pt` preferred, falls back to `yolo10n.pt`)
2. **Opens** the input video `summer.mp4` using OpenCV
3. **Reads** video properties: width, height, FPS
4. **Creates** an output video writer (`output.mp4`) with the same properties
5. **Processes each frame**:
   - Runs YOLO object detection (on CPU)
   - Draws bounding boxes + class labels on the frame
   - Writes the annotated frame to the output file
   - Displays a live preview window
6. **Stops** when the video ends or the user presses **`Q`**
7. **Saves** the annotated video to `output.mp4`

---

## 🚀 How to Run

### 1. Prerequisites

Make sure you have **Python 3.8+** installed. Then install the required libraries:

```bash
pip install ultralytics opencv-python
```

### 2. Prepare Input Files

Place your input video file in the **same folder** as the script and name it:

```
summer.mp4
```

> ⚠️ The script will raise a `FileNotFoundError` if `summer.mp4` is not found.

Make sure the model weight file is also present in the same folder:

```
yolov10n.pt    ← already included in the project folder
```
> The script first looks for `yolo11n.pt`. If not found, it falls back to `yolo10n.pt` / `yolov10n.pt`.

### 3. Run the Script

```bash
python yolo-project.py
```

### 4. Output

- A **live preview window** titled `YOLO Video Detection` will appear showing detections in real-time.
- Press **`Q`** at any time to stop early.
- The final annotated video will be saved as **`output.mp4`** in the same directory.

```
✅ Output saved to: <your-folder>/output.mp4
```

---

## 🧠 Model Info

| Property | Detail |
|---|---|
| Model | YOLOv10 Nano / YOLOv11 Nano |
| Device | CPU (forced via `model.to("cpu")`) |
| Task | Object Detection |
| Input | Video frames (BGR via OpenCV) |
| Output | Annotated frames with bounding boxes |

> 💡 **Tip:** To use GPU acceleration, change `model.to("cpu")` to `model.to("cuda")` in `yolo-project.py` — requires NVIDIA GPU + CUDA toolkit.

---

## 📦 Dependencies

```txt
ultralytics    # YOLO model framework
opencv-python  # Video reading, writing, and display
```

Install all at once:

```bash
pip install ultralytics opencv-python
```

---

## 🛑 Common Errors & Fixes

| Error | Cause | Fix |
|---|---|---|
| `FileNotFoundError: Input video not found` | `summer.mp4` missing | Place `summer.mp4` in the project folder |
| `RuntimeError: Could not open video file` | Corrupted or unsupported video format | Use a valid `.mp4` file |
| `RuntimeError: Could not read video properties` | Video has 0 width/height/fps | Re-encode the video using `ffmpeg` |
| `RuntimeError: Could not create output video` | Permission or codec issue | Check folder write permissions |
| `ModuleNotFoundError: No module named 'ultralytics'` | Package not installed | Run `pip install ultralytics` |

---

*Project built as part of the Summer PEP Backend-GenAI training module.*
