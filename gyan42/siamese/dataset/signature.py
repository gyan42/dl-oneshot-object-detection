import os
import pandas as pd
from PIL import Image
import torch
import numpy as np
from gyan42.siamese.dataset import SiameseDataset

#preprocessing and loading the dataset
class SiameseDataset():
    def __init__(self,training_csv=None, training_dir=None, transform=None):
        # used to prepare the labels and images path
        self.train_df=pd.read_csv(training_csv)
        self.train_df.columns =["image1","image2","label"]
        self.train_dir = training_dir
        self.transform = transform

    def __getitem__(self,index):
        # getting the image path
        image1_path=os.path.join(self.train_dir,self.train_df.iat[index,0])
        image2_path=os.path.join(self.train_dir,self.train_df.iat[index,1])
        # Loading the image
        img0 = Image.open(image1_path)
        img1 = Image.open(image2_path)
        img0 = img0.convert("L")
        img1 = img1.convert("L")
        # Apply image transformations
        if self.transform is not None:
            img0 = self.transform(img0)
            img1 = self.transform(img1)
        return img0, img1 , torch.from_numpy(np.array([int(self.train_df.iat[index,2])],dtype=np.float32))
    def __len__(self):
        return len(self.train_df)