from emotionDetection.emotion_detection import emotion_detector
import unittest

TEST_CASES = [
    ["I am glad this happened", "joy"],
    ["I am really mad about this", 	"anger"],
    ["I feel disgusted just hearing about this", "disgust"],
    ["I am so sad about this", "sadness"],
    ["I am really afraid that this will happen", "fear"]
]

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        for test_case in TEST_CASES:
            result = emotion_detector(test_case[0])
            self.assertEqual(result['dominant_emotion'],test_case[1])

unittest.main()