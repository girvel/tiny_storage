import re


if __name__ == '__main__':
    def increment_init(match):
        return "__version__ = '{}.{}.{}'".format(
            match.group(1),
            match.group(2),
            int(match.group(3)) + 1,
        )

    def increment_setup(match):
        return "version='{}.{}.{}'".format(
            match.group(1),
            match.group(2),
            int(match.group(3)) + 1,
        )

    for file, pattern, function in (
        ('tiny_storage/__init__.py',
         r'__version__\s*=\s*[\'"](\d+)\.(\d+)\.(\d+)[\'"]',
         increment_init),

        ('setup.py',
         r'version\s*=\s*[\'"](\d+)\.(\d+)\.(\d+)[\'"]',
         increment_setup),
    ):
        with open(file, 'r') as f:
            content = f.read()

        with open(file, 'w') as f:
            f.write(re.sub(pattern, function, content))


