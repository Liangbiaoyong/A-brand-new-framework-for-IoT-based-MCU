

__version__ = "1.0.0"

__help__ = '''

Pin:
0-key
25-beep
6-ds18x20
27-dht
19-ctrl1
23-ctrl2
pass-ctrl3
18-ctrl4
25-strokeswitch
16-lowerleft
9-lowerright
22-right

'''


def main(args: Optional[List[str]] = None) -> int:
    """This is an internal API only meant for use by pip's own console scripts.

    For additional details, see https://github.com.
    """
    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
