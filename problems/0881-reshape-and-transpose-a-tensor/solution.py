import torch

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    x = torch.reshape(x, (-1,))
    return torch.reshape(x, (new_shape))

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    return x.transpose(-2, -1)
