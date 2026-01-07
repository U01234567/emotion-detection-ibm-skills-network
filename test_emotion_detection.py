# Import relevant functions from package
from EmotionDetection.emotion_detection import emotion_detector

# Import test lib
import unittest


STATEMENTS = {
    "I am glad this happened":                    "joy",
    "I am really mad about this":                 "anger",
    "I feel disgusted just hearing about this":   "disgust",
    "I am so sad about this":                     "sadness",
    "I am really afraid that this will happen":   "fear",
}

class TestEmotionDetector(unittest.TestCase):
    def test_emotions(self):
        for statement, aimed_result in STATEMENTS.items():
            tested_result = emotion_detector(statement)["dominant_emotion"]
            self.assertEqual(tested_result, aimed_result)

if __name__ == '__main__':
    unittest.main()
