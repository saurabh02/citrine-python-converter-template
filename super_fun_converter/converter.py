from pypif.obj import ChemicalSystem()

def convert(files=[], important_argument=None, whatever_argument=[1.0, 1.0, 1.0], **kwargs):
    """
    Convert files into a pif
    :param files: to convert
    :param important_argument: an important argument, must be provided
    :param whatever_argument: a less important argument with default 1
    :param kwargs: any other arguments
    :return: the pif produced by this conversion
    """
    if not important_argument:
        raise KeyError("The important_argument argument was not passed to convert")
    return ChemicalSystem() 
