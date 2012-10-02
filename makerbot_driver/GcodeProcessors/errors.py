class NotGCodeFileError(Exception):
    """
    A NotGCodeFileError is thrown when a file is passed into
    process_file that is not a .gcode file
    """


class ProcessorNotFoundError(Exception):
    """
    A PreprocessorNotFoundError is raised when a preprocessor
    is searched for by the factory, but not found.
    """


class VersionError(Exception):
    """
    A Version Error is thrown if a gcode file of an incompatible
    version is encountered
    """
