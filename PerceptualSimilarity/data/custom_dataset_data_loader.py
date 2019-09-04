from __future__ import absolute_import

import os
import torch.utils.data

from . import dataset as dsm
from .base_data_loader import BaseDataLoader

def CreateDataset(dataroots,dataset_mode='2afc',load_size=64,):
    dataset = None
    if dataset_mode=='2afc': # human judgements
        dataset = dsm.TwoAFCDataset()
    elif dataset_mode=='jnd': # human judgements
        dataset = dsm.JNDDataset()
    else:
        raise ValueError("Dataset Mode [%s] not recognized."%self.dataset_mode)

    dataset.initialize(dataroots,load_size=load_size)
    return dataset

class CustomDatasetDataLoader(BaseDataLoader):
    def name(self):
        return 'CustomDatasetDataLoader'

    def initialize(self, datafolders, dataroot='./dataset',dataset_mode='2afc',load_size=64,batch_size=1,serial_batches=True, nThreads=1):
        BaseDataLoader.initialize(self)
        if(not isinstance(datafolders,list)):
            datafolders = [datafolders,]
        data_root_folders = [os.path.join(dataroot,datafolder) for datafolder in datafolders]
        self.dataset = CreateDataset(data_root_folders,dataset_mode=dataset_mode,load_size=load_size)
        self.dataloader = torch.utils.data.DataLoader(
            self.dataset,
            batch_size=batch_size,
            shuffle=not serial_batches,
            num_workers=int(nThreads))

    def load_data(self):
        return self.dataloader

    def __len__(self):
        return len(self.dataset)
