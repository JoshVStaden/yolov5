# YOLO5 Detector
Train and test the YOLOv5 object detector.

## Installation Instructions
- Install CUDA 11.1 or 10.2
- Download the appropriate version of PyTorch for that CUDA version. To choose the correct version, please select from the list below:
  - CUDA 11.1: `pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html`
  - CUDA 10.2: `pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html`
- Ensure that your installation of Torch can see CUDA with:
  
```python
import torch
print(torch.cuda.is_available())
```

## Configuring Training
- Open config.py
- Configure `DATASET_DIR` to point to your yaml file containing the dataset configuration
  - For an example on the yaml file, please refer to example.yaml
  - Annotations are written in [YOLO v5 PyTorch format](https://roboflow.com/formats/yolov5-pytorch-txt). A few datasets on Roboflow can be downloaded in this format automatically, but it is also possible to convert between formats.
- Create a .yaml file defining your model. To do this, use one of the `yolov5.yaml` files in the `models/` directory as a baseline. Create your own YAML file, copy-paste the contents of the `yolo5.yaml`, and change `nc:` at the top top to the number of classes you need.
- Point the `MODEL_CONFIG` variable in config.py to this YAML file.
- Configure hyperparams, epochs and batch size

## Downloading Pretrained Weights
- Run `python download_weights.py`
- Open config.py and set INITIAL_WEIGHTS to the appropriate weights
- This will depend on which YOLOv5 you based your model off of
- For example, if you based it off yolov5n.yaml, you will use yolov5n.pt as your pretrained weights

## Training Code
Run `python train.py` or `python train.py --multi-scale`
Each subsequent run of your code will be stored in runs/exp*n*/weights (where *n* is just the number of the run). To get the latest weights, use latest.pt. To use the weights with the best scores on the validation set, use best.pt.

## Using Your Model
Get the best weights (best.pt) from the above step and copy them to your current directory (wherever you are running your script from). The code to use the weights is:

```python
import torch

model = torch.hub.load('JoshVStaden/yolov5', 'custom', 'best.pt')

predictions = model([image]).pandas().xyxy[0]
```

This will return a Pandas dataframe with the keys 'xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class' and 'name'.

Or, for a more in-depth example of how to use this (possibly better than I am), you can [check out this guide here](https://docs.ultralytics.com/tutorials/pytorch-hub/).