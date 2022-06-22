from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
import typing as T

from modalities.distributions import Distribution

# TODO: allow None for all of these fields to indicate unknown. inf is unknown
# TODO: for many of the tensor-level fields, make decoration for T or list[T]


class CompositeModality(ABC, dataclass):
    """
    A composite modality is a modality that is composed of other modalities.
    """
    pass


class Modality:
    # TODO: make the modality attrs be tree[T] instead of T
    # TODO: convenience initialization for grouping
    # None for completely unknown, slice for range of sizes, ellipses for unknown rank. iterables (sets, lists) can also be passed to denote a choice of specific sizes.
    shape: list[int]
    dtype: type
    groupings: Grouping
    dist: Distribution
    meta: any  # usually description string


class Grouping:
    axes: list[int]
    ordering: list[int]
