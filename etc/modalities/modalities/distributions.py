# These distributions are here to establish a common metadata vocabulary,
# not to perform computation.

from __future__ import annotations
from abc import ABC
import typing as T


class Distribution(ABC):
    ...


class Categorical(Distribution):
    """

    """


# TODO: think about how all of the below are special cases of categorical
# maybe remove some of the special cases

class Multinoulli(Distribution):
    """A distribution over the values {0, 1}^k. Commonly seen as gym.spaces.MultiBinary."""
    probs: list[float]
    # TODO: convenience initer with just num categories


class Bernoulli(Multinoulli):
    """A distribution over the values {0, 1}."""
    p: float


class KHot(Distribution):
    """Indicates that k elements on `axes` are hot while the rest are inactive"""
    axes: list[int]  # usually just -1, but for 2d hard attention, could be [-2, -1]
    k: list[int]  # all possible k's


class OneHot(KHot, Categorical):
    """One-hot distribution. A special case of KHot and another name for Categorical"""
    pass  # TODO: custom initializer


class Uniform(Distribution):
    """A uniform distribution: p(x) = 1 / (high - low)"""
    low: float | None
    high: float | None


class Normal(Distribution):
    """A normal distribution: p(x) = 1/sqrt(2*pi*sigma^2) * exp(-(x-mu)^2/(2*sigma^2))"""
    mean: float | None
    std: float | None


class Exponential(Distribution):
    """An exponential distribution: p(x)=lambda*exp(-lambda*x)"""
    rate: float | None


class Clipped(Distribution):
    """A distribution that is clipped to a range."""
    low: float | None
    high: float | None
    dist: Distribution


class Sparse(Distribution):
    """Gaussian mixture model between zero and the given distribution"""
    dist: Distribution
    k: int
