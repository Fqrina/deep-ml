# --- cell 1 ---
import torch, torch.nn as nn

def build_model() -> nn.Module:
    """
    Return a tiny nn.Module for MNIST classification (10 classes).
    IMPORTANT: If total trainable params > 2048, final accuracy will be set to 0.
    Tip: Consider very small convs, global average pooling, and tiny linear head.
    """
    class TinyNet(nn.Module):
         def __init__(self):
             super().__init__()
             self.maxpool = nn.MaxPool2d(kernel_size=2, stride=2)
             self.conv1 = nn.Conv2d(1,3,kernel_size=2, stride=1)
             self.conv2 = nn.Conv2d(3,6, kernel_size=2, stride=1)
             self.inter = nn.Linear(6*6*6,8)
             self.relu = nn.ReLU()
             self.out = nn.Linear(8, 10)
         def forward(self, x): # 28,28
             # x = x.unsqueeze(1)
             c = self.maxpool(self.conv1(x)) #13,13
             c2 = self.maxpool(self.conv2(c)) #6,6
             inter = self.inter(c2.view(c2.size(0), -1))
             out = self.out(self.relu(inter))
             return out
    return TinyNet()