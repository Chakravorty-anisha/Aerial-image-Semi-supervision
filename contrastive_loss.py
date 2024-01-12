# -*- coding: utf-8 -*-
"""contrastive_loss.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PFD4xQokcJs3neKjA3g79-Sk4THz-XQh
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

def contrastive_loss(projections):
    # Example contrastive loss using cosine similarity
    sim_matrix = F.cosine_similarity(projections.unsqueeze(1), projections.unsqueeze(0), dim=2)
    sim_matrix = sim_matrix / 0.07  # Temperature scaling, adjust as needed

    labels = torch.arange(len(sim_matrix)).to(projections.device)
    loss = F.cross_entropy(sim_matrix, labels)

    return loss