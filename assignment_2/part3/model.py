# MIT License
#
# Copyright (c) 2017 Tom Runia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to conditions.
#
# Author: Deep Learning Course | Fall 2018
# Date Created: 2018-09-04
################################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torch.nn as nn
import torch

class TextGenerationModel(nn.Module):

    def __init__(self, batch_size, seq_length, vocabulary_size,
                 lstm_num_hidden=256, lstm_num_layers=2, device='cuda:0'):

        super(TextGenerationModel, self).__init__()
        self.batch_size = batch_size
        self.seq_length = seq_length
        self.hidden_dim = lstm_num_hidden
        self.lstm_num_layers = lstm_num_layers
        self.device = device

        self.lstm = nn.LSTM(1, self.hidden_dim, num_layers=lstm_num_layers)
        self.linear = nn.Linear(self.hidden_dim, vocabulary_size)

    def forward(self, x, batch_size = None):
        if batch_size:
            self.hidden = (torch.zeros(self.lstm_num_layers, batch_size, self.hidden_dim).to(device=self.device),
                           torch.zeros(self.lstm_num_layers, batch_size, self.hidden_dim).to(device=self.device))

        lstm_out, self.hidden = self.lstm(x, self.hidden)
        out = self.linear(lstm_out.view(-1, lstm_out.size(2)))
        return out