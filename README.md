# Finger Counting

A real-time hand tracking and finger counting system using computer vision. Detects hand landmarks and counts extended fingers from webcam input.

## Features 

- Real-time hand detection (1 or 2 hands)
- Visual display of 21 hand landmarks per hand
- Mirror mode for intuitive interaction
- Adjustable detection confidence

## Technology Stack
- OpenCV: Computer vision operations
- cvzone: Simplified hand tracking interface

## Installation 

### Prerequisites
- Python 3.7+
- Webcam

### Setup
```bash
pip install opencv-python cvzone
```

## Usage

1. Run the script:
```bash
python finger_counting.py
```

2. Interact with the camera:
	- Show your hand(s) to the camera
	- System will display landmarks and count fingers
	- For two hands, displays combined finger count

3. To exit the program press 'q'.
