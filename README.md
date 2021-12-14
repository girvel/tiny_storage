![](https://byob.yarr.is/girvel/tiny_storage/coverage)

# Summary

Library for application data storage. It is:

- tiny
- key-value
- single-file
- YAML based

# Example

```py
from tiny_storage import Storage, Type
import sys

# matches the file /etc/example-app/yaml or %PROGRAMDATA%\example-app\config.yaml
config = Storage('example-app', Type.global_config)

if sys.argv[1] == 'set-greeting':
  # changes greeting only if does not exist
  if not config('lines.greeting').try_put(sys.argv[2]):
    print('Greeting already exists. It should not be changed.')
else:
  # prints greeting if it exists or given string
  print(config('lines.greeting').pull('Hello, world!'))
```

