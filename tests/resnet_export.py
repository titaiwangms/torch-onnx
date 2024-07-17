import torch
import torchvision
import torch_onnx
from torch_onnx import _validation


def main():
    torch_onnx.patch_torch(
        error_report=True,
        profile=True,
        dump_exported_program=True,
        artifacts_dir="resnet18",
    )

    resnet18 = torchvision.models.resnet18(
        weights=torchvision.models.ResNet18_Weights.DEFAULT
    )
    sample_input = (torch.randn(4, 3, 224, 224),)
    onnx_program = torch.onnx.export(
        resnet18,
        sample_input,
        "resnet18.onnx",
        opset_version=18,
    )
    _validation.verify_onnx_program(onnx_program)


if __name__ == "__main__":
    main()
