class OpenVQEException(Exception):
    """
    Base class for other exceptions
    """

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

    pass


class OpenVQEParameterError(OpenVQEException):
    """
    Raised when a specific choice of a parameter is not accepted
    """

    def __init__(self, parameter_name, parameter_class, parameter_value, called_from=""):
        self.message = "OpenVQE ParameterError:" + called_from + " unknown parameter value: " + str(
            parameter_name) + "=" + str(
            parameter_value) + " for " + str(parameter_class)


class OpenVQETypeError(OpenVQEException):
    """
    Raised when an attribute is of wrong type
    """

    def __init__(self, attr, type, expected):
        self.message = "OpenVQE TypeError: " + "excpected type: " + str(expected) + " but got type " + str(
            type) + " for attribute " + str(attr)
