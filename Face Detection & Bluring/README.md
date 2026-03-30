# Face Detection and Blurring

This project detects faces with MediaPipe and blurs the detected face regions using OpenCV.

## Requirements

- Python 3.12
- `opencv-python`
- `mediapipe`

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Files

- `main.py`: main script
- `a.jpg`: sample image input
- `a.MOV`: sample video input
- `output/`: generated output files

## How It Works

The script uses `mediapipe.solutions.face_detection` to detect one or more faces in each frame.

For every detected face:

1. The bounding box is returned in relative coordinates.
2. The box is converted to image pixel coordinates.
3. The selected face area is blurred with `cv2.blur(...)`.

The same `process_img()` function is reused for image, video, and webcam frames.

## Run Modes

The script supports three modes:

- `image`
- `video`
- `webcam`

## 1. Image Mode

Use this to blur faces in a single image and save the result.

Command:

```powershell
python main.py --mode image --filePath a.jpg
```

What happens:

1. The image is loaded from the folder.
2. MediaPipe detects faces.
3. Each detected face is blurred.
4. The result is saved to `output/output.png`.

## 2. Video Mode

Use this to blur faces in a video file and save a processed video.

Command:

```powershell
python main.py --mode video --filePath a.MOV
```

What happens:

1. The video is opened frame by frame.
2. Each frame is passed to the face detection function.
3. Detected face regions are blurred.
4. The processed frames are written to `output/output.mp4`.

## 3. Webcam Mode

Use this to blur faces live from your webcam.

Command:

```powershell
python main.py --mode webcam
```

What happens:

1. The default webcam is opened.
2. Each live frame is processed.
3. Detected faces are blurred in real time.
4. A preview window is shown.
5. Press `q` to stop the webcam.

## Notes

- The script can detect multiple faces in the same frame.
- If a file path is relative, it is resolved from the `Face Detection & Bluring` folder.
- Output files are saved inside the `output` folder.
- If no face is detected, the image or frame is left unchanged.

## Example Commands

Run image:

```powershell
python main.py --mode image --filePath a.jpg
```

Run video:

```powershell
python main.py --mode video --filePath a.MOV
```

Run webcam:

```powershell
python main.py --mode webcam
```
