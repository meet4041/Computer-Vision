import os
import cv2
from pathlib import Path
import mediapipe as mp
import argparse

def process_img(img, face_detection):
    h_img, w_img, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            
            x1 = int(x1 * w_img)
            y1 = int(y1 * h_img)
            w = int(w * w_img)
            h = int(h * h_img)
            
            img[y1:y1 + h, x1:x1+w, :] = cv2.blur(img[y1:y1 + h, x1:x1+w, :], (50,50))

    preview_max_width = 950
    preview_max_height = 675
    
    scale = min(preview_max_width / w_img, preview_max_height / h_img, 1.0)
    preview_size = (int(w_img * scale), int(h_img * scale))
    # preview_img = cv2.resize(img, preview_size, interpolation=cv2.INTER_AREA)
    
    return img
    
args = argparse.ArgumentParser()
args.add_argument("--mode", default = 'webcam')
args.add_argument("--filePath", default = 'None')

args = args.parse_args()

project_dir = Path(__file__).resolve().parent

output_dir = project_dir / 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    if args.mode in ["image"]:
        file_path = Path(args.filePath)
        if not file_path.is_absolute():
            file_path = project_dir / file_path

        img = cv2.imread(str(file_path))
        if img is None:
            raise FileNotFoundError(f"Could not load image: {file_path}")

        img = process_img(img, face_detection)
        cv2.imwrite(str(output_dir / 'output.png'), img)
        
    elif args.mode in ['video']:
        file_path = Path(args.filePath)
        if not file_path.is_absolute():
            file_path = project_dir / file_path

        cap = cv2.VideoCapture(str(file_path))
        ret, frame = cap.read()
        if not ret or frame is None:
            raise FileNotFoundError(f"Could not read video: {file_path}")

        output_video = cv2.VideoWriter(
            str(output_dir / 'output.mp4'),
            cv2.VideoWriter_fourcc(*'MP4V'),
            25,
            (frame.shape[1], frame.shape[0]),
        )
        
        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)
            ret, frame = cap.read()
            if not ret or frame is None:
                break
        
        cap.release()
        output_video.release()
        
    elif args.mode in ['webcam']:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        while ret:
            frame = process_img(frame, face_detection)
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            ret, frame = cap.read()
        
        cap.release()
        cv2.destroyAllWindows()
