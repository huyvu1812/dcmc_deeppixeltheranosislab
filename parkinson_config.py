# import the necessary packages
import os

# initialize the base path for the LISA dataset
BASE_PATH = "parkinson"

# build the path to the annotations file
ANNOT_PATH = os.path.sep.join([BASE_PATH, "allParkinsons.csv"])

# build the path to the output training and testing record files,
# along with the class labels file
TRAIN_RECORD = os.path.sep.join([BASE_PATH,
	"records/training.record"])
TEST_RECORD = os.path.sep.join([BASE_PATH,
	"records/testing.record"])
CLASSES_FILE = os.path.sep.join([BASE_PATH,
	"records/classes.pbtxt"])

# initialize the test split size
TEST_SIZE = 0.2

# initialize the class labels dictionary
CLASSES = {"Parkinson": 1, "Normal": 2}
