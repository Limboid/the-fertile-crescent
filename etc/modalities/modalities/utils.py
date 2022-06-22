
# TODO: also make something like this that can annotate types from `int` to `List[int]`

def export(x, name: str):
    """
    Export a variable to the global scope.
    """
    globals()[name] = x  # double check this. copilot generated it


def make_container(x, container=list):
    if isinstance(x, container):
        return x
    else:
        return container(x)

# TODO: tree flatten, unflatten, and map functions
