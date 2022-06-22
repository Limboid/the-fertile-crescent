# TODO: define some common modality structures for common applications

class ImageModality:
    ...


class VideoModality:
    ...


class AudioModality:
    ...


class TextModality:
    ...


class ImageTextModality:
    ...


class ImageAudioModality:
    ...


class VideoAudioModality:
    ...


class VideoTextModality:
    ...


class AudioTextModality:
    ...


class VideoAudioTextModality:
    ...


class GraphModality(ABC, dataclass):
    """Represents a graph."""
    directed: bool


class AdjacencyMatrixGraphModality(GraphModality):
    """
    A graph modality that is represented by an adjacency matrix and possibly vertex values
    """
    A: Modality
    V: Modality | None


class AdjacencyListGraphModality(GraphModality):
    """
    A graph modality that is represented by an adjacency list and possibly vertex values
    """
    A: list[tuple[int, int]]
    V: Modality | None
