import cv2
import cvzone
import sys
from ultralytics import YOLO
from Poker_Hand_Detector.entity.artifact_entity import CardRecognizerArtifact
from Poker_Hand_Detector.entity.config_entity import HandDetectorConfig
from Poker_Hand_Detector.Components.Hand_detector import bounding_box, find_hand
from Poker_Hand_Detector.constant.training_pipeline import *
from Poker_Hand_Detector.logger import logging
from Poker_Hand_Detector.exception import pokerException



class Display:
    def __init__(self,CR_artifact: CardRecognizerArtifact,
                  config: HandDetectorConfig):
        self.card_artifact = CR_artifact
        self.config = config



    def display_Video(self):
        logging.info("Displaying Real-time results")
        try:
            # Initialize webcam
            cap = cv2.VideoCapture(0)  # Use 0 for built-in webcam, 1 for external webcam
            cap.set(3, 1280)  # Set width
            cap.set(4, 720)   # Set height

            # Load YOLO model
            model = YOLO('C:/Users/49179/Desktop/Poker_Hand_Detection/runs/detect/train2/weights/best.pt')

            while True:
                success, img = cap.read()  # Capture frame from webcam
                if not success:
                    break

                img=cv2.flip(img,flipCode=1)
                # Run YOLO model on frame
                results = model.predict(img, stream=True)

                hand = bounding_box(results=results, img= img)
                if len(hand) == 5:
                    results_1 = find_hand(hand)
                    cvzone.putTextRect(img, f'Your Hand: {results_1}', (300, 75), scale=3, thickness=5)

                # Display the image
                cv2.imshow("Image", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Release resources
            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            raise pokerException(e,sys)

