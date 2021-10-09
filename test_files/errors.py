class RunTimeErrorWithCode(Exception):
    # This message in multi quotes called dockstring.
    """
    Exception raised when a specific error code is needed.
    """

    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code


raise RunTimeErrorWithCode("OUCH! An error happened.", 500)
