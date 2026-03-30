# Colour Detection

This project opens your webcam, detects yellow objects, and draws a green box around the detected area.

## Requirements

- Windows PowerShell
- Python 3.14 or a recent Python 3 version
- A webcam connected to your computer

## Step 1: Open the project folder

Open PowerShell and move into the folder:

```powershell
cd "C:\Users\BAPS\Desktop\Computer Vision\Colour Detection"
```

## Step 2: Install the required packages

Run:

```powershell
& C:\Users\BAPS\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install -r requirements.txt
```

This installs:

- `opencv-python`
- `numpy`
- `Pillow`

## Step 3: Run the project

Start the script with:

```powershell
& C:\Users\BAPS\AppData\Local\Python\pythoncore-3.14-64\python.exe .\main.py
```

## Step 4: Test yellow object detection

Hold a yellow object in front of the webcam.

What you should see:

- A webcam window opens.
- A green rectangle appears around the yellow object.
- The terminal prints the bounding box coordinates.

If no yellow area is detected, the printed value may be `None`.

## Step 5: Quit the program

Press `q` on your keyboard to close the webcam window.

## Troubleshooting

If you get `ModuleNotFoundError`, install the requirements again using the same Python command from Step 2.

If detection is weak:

- Try better lighting.
- Move the yellow object closer to the camera.
- Make sure the object is clearly yellow.
