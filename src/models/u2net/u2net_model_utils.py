import torch
from torch import Tensor
from PIL import Image
import numpy as np
from skimage import io
import os
from torchvision import transforms
from torch.autograd import Variable
from .u2net_init import U2NetModel
from .u2net_processor import SalObjDataset, RescaleT, ToTensorLab
from torch.utils.data import DataLoader


def make_u2net_dataloader(img_path: str) -> DataLoader:
    """ Makes dataloader for user's input image
    :param img_path: Path to image
    :return dataloader: Ready to use dataloader for input image
    """
    img_name_list = [img_path]

    test_salobj_dataset = SalObjDataset(
        img_name_list=img_name_list,
        lbl_name_list=[],
        transform=transforms.Compose([
            RescaleT(320),
            ToTensorLab(flag=0)
        ])
    )
    salobj_dataloader = DataLoader(
        test_salobj_dataset,
        batch_size=1,
        shuffle=False,
        num_workers=1
    )
    return salobj_dataloader


def normPRED(d: Tensor) -> Tensor:
    """ Normalizing the output from U2Net channel
    :param d: Torch tensor, representing the
    """
    ma = torch.max(d)
    mi = torch.min(d)

    dn = (d - mi) / (ma - mi)

    return dn


def generate_mask(model,
                  image_dataloader: DataLoader,
                  orig_image_path: str) -> None:
    """ Generating the output mask from U2Net model
    :param image_dataloader: Torch DataLoader with user's input image
    :param orig_image_path: Path to original image for resizing
    :param model: U2Net model
    :return :
    """
    for i_test, data_test in enumerate(image_dataloader):
        inputs_test = data_test['image']
        inputs_test = inputs_test.type(torch.FloatTensor)
        if torch.cuda.is_available():
            inputs_test = Variable(inputs_test.cuda())
        else:
            inputs_test = Variable(inputs_test)

        net = model
        d1, d2, d3, d4, d5, d6, d7 = net(inputs_test)
        pred = d1[:, 0, :, :]
        pred = normPRED(pred)

        predict = pred.squeeze()
        predict_np = predict.cpu().data.numpy()

        im = Image.fromarray(predict_np * 255).convert('RGB')
        image = io.imread(orig_image_path)
        imo = im.resize((image.shape[1], image.shape[0]), resample=Image.BILINEAR)

        imo.save('models/predictions/u2net_masked_image.png')
