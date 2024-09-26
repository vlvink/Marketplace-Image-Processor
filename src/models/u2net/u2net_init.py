from .u2net_model import U2NET
import torch


class U2NetModel:
    def __init__(self):
        self.model_name = 'u2net'
        self.net = U2NET(3, 1)
        self.net.load_state_dict(torch.load("models/params/u2net/u2net.pth"))

        if torch.cuda.is_available():
            self.net.cuda()

        self.net.eval()

    def get_net(self):
        return self.net

