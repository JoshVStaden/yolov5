# Path to file containing the .yaml file
DATASET_DIR = '../../Datasets/Pistols/data.yaml'

# YAML file containing model configuration
MODEL_CONFIG = 'models/yolopistol.yaml'

# For transfer learning, the weights to begin with
# If you don't want to begin with pretrained weights, 
# then set this to ' '
INITAL_WEIGHTS = './best_latest.pt'

# File containing hyperparam config
HYPERPARAMS = 'data/hyps/hyp.scratch.yaml'

# Number of epochs
EPOCHS = 300

# Batch size
BATCH_SIZE = 16

# Size of image
IMAGE_SIZE = 256