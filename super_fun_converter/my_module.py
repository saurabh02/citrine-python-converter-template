from pypif.obj import ChemicalSystem

def convert(
        files=[],
        important_argument=None,
        whatever_argument=[0.0, 1.0, 2.0],
        do_some_extra_thing=False,
        some_condition=None,
        **kwargs):
    """
    Convert files into a pif

    :param files: to convert
    :param important_argument: an important argument, must be provided
    :param whatever_argument: a less important argument with default 1
    :param do_some_extra_thing:
    :param kwargs: any other arguments
    :return: the pif produced by this conversion
    """
    if not important_argument:
        raise KeyError("The important_argument argument was not passed to convert")
    return ChemicalSystem()
