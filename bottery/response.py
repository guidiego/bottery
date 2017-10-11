__all__ = ['telegram']

class Response():
    def __init__(self, *args, **kw):
        for integration in __all__:
            i = kw.get(integration, None)

            if i:
                setattr(self, integration, i)