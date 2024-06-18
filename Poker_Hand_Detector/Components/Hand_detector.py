from ultralytics import YOLO
import math
import cvzone
import sys
from Poker_Hand_Detector.entity.config_entity import HandDetectorConfig 
from Poker_Hand_Detector.constant.training_pipeline import *
from Poker_Hand_Detector.logger import logging
from Poker_Hand_Detector.exception import pokerException

config = HandDetectorConfig
def find_hand(hand):
    logging.info("Finding the best hand")
    ranks = []
    suits = []
    possible_rank = []
    try:
        for card in hand:
            if len(card) == 2:
                rank=card[0]
                suit = card[1]
            else:
                rank= card[0:2]
                suit = card[2]

            if rank == "A":
                rank = 14
            elif rank == "J":
                rank = 11
            elif rank == "Q":
                rank = 12
            elif rank == "K":
                rank= 13
            ranks.append(int(rank))
            suits.append(suit)

        sorted_ranks = sorted(ranks)

        # check for royal_flush,straight_flush, flush and straight
        #first we check for flush
        if suits.count(suits[0]) == 5:
            if 10 in sorted_ranks and 11 in sorted_ranks and 12 in sorted_ranks and 13 in sorted_ranks and 14 in sorted_ranks:
                possible_rank.append("10")
            elif all(sorted_ranks[i] == sorted_ranks[i-1] +1 for i in range(1, len(sorted_ranks))):
                possible_rank.append("9")

            else:
                possible_rank.append("6")

        elif all(sorted_ranks[i]== sorted_ranks[i-1] + 1 for i in range(1, len(sorted_ranks))):
            possible_rank.append("5")


        #Check for Four of a kind, full_house, three of a kind
        values = list(set(sorted_ranks))

        if len(values) == 2:
            for i in values:
                if sorted_ranks.count(i) == 4:
                    possible_rank.append("8")
                elif sorted_ranks.count(i) == 3:
                    possible_rank.append("7")

        elif len(values) == 3:
            for i in values:
                if sorted_ranks.count(i) == 3:
                    possible_rank.append("4")
                elif sorted_ranks.count(i) == 2:
                    possible_rank.append("3")

        elif len(values) == 4:
            for i in values:
                if sorted_ranks.count(i) == 2:
                    possible_rank.append("2")

        else:
            possible_rank.append("1")

        mapping = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        
        Handranking = {"10": "Royal Flush", "9": "Straight Flush", "8": "Four of a Kind", "7": "Full House", "6": "Flush", "5": "Straight", "4": "Three of a Kind", "3": "Two pair", "2": "A Pair", "1": f"High Card: {mapping.get(max(sorted_ranks))}"} 

        
        Winning_Hand = Handranking[max(possible_rank)]
        return Winning_Hand
    except Exception as e:
        raise pokerException(e,sys)
    

def bounding_box(results,img):
    logging.info(" detecting Crads location and recognizing")
    try:
        hand = []

        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))
                
                # Confidence
                conf = box.conf[0]
                conf = math.ceil((conf * 100)) / 100
                
                # Class Name
                cls = int(box.cls[0])
                label = f'{config.classnames[cls]} {conf}'
                cvzone.putTextRect(img, label, (max(0, x1), max(35, y1)), scale=1, thickness=1)

                # Add to hand if confidence is high enough
                if conf > 0.25: #config.confidence:
                    hand.append(config.classnames[cls])


        Detected_Hand=list(set(hand))
        return Detected_Hand
    
    except Exception as e:
        raise pokerException(e,sys)