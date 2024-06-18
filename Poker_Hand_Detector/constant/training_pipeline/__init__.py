from datetime import datetime
from typing import List
import os

### Data Ingestion Constants
TIMESTAMP: datetime =  datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

ARTIFACT_DIR: str = f"artifacts"

BUCKET_NAME: str = "cardimgs"

S3_DATA_FOLDER: str = "data"

OUTPUT_DIR: str = "model_weights"

WEIGHTS: str = "yolov8l.pt"

EPOCHS: int = 30

BATCH_SIZE: int = 8

IMAGE_SIZE: int = 512

PLOT: bool = True

NUM_CLASSES: int = 52

NAMES: List[str] = ['10C', '10D', '10H', '10S', '2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'AC', 'AD', 'AH', 'AS', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC', 'QD', 'QH', 'QS']

CONFIDENCE: float = 0.5

RANKS: List[int] = []

SUITS: List[str] = []

POSSIBLE_RANKS: List[str] = []

HAND: List[str] = []



