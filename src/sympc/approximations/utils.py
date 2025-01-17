"""Utility functions for approximation functions."""

from sympc.tensor import MPCTensor
from sympc.tensor import RegisterApproximation


@RegisterApproximation("sign")
def sign(data: MPCTensor) -> MPCTensor:
    """Calculate sign of given tensor.

    Args:
        data (MPCTensor): tensor whose sign has to be determined

    Returns:
        MPCTensor: tensor with the determined sign
    """
    return (data > 0) + (data < 0) * (-1)


@RegisterApproximation("modulus")
def modulus(data: MPCTensor) -> MPCTensor:
    """Calculation of modulus for a given tensor.

    Args:
        data (MPCTensor): tensor whose modulus has to be calculated

    Returns:
        MPCTensor: the required modulus

    """
    return sign(data) * data
