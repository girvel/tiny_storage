# Data storage convention

This table describes where application data of different types are placed. Names that look like valid python expressions are already realized, the other ones are not.

## Already realized

| Data type            | Windows                            | Linux                          |
|----------------------|------------------------------------|--------------------------------|
| `Type.local`         | `{name}.yaml`                      | `{name}.yaml`                  |
| `Type.user_data`     | `%APPDATA%/{name}/{name}.yaml`     | `$HOME/.{name}.yaml`           |
| `Type.user_config `  | `%APPDATA%/{name}/config.yaml`     | `$HOME/.config/{name}.yaml`    |
| `Type.global_data`   | `%PROGRAMDATA%/{name}/data.yaml`   | `/var/lib/{name}.yaml`         |
| `Type.global_config` | `%PROGRAMDATA%/{name}/config.yaml` | `/etc/{name}.yaml`             |
 
## Maybe later

| Data type                     | Windows                                  | Linux                           |
|-------------------------------|------------------------------------------|---------------------------------|
| User non-portable             | `%LOCALAPPDATA%/{name}/{name}.yaml`      | `$HOME/.{name}.yaml`            |
| User non-portable config      | `%LOCALAPPDATA%/{name}/{name}.yaml`      | `$HOME/.{name}.yaml`            |
| Global read-only portable     | `%PROGRAMDATA%/{name}/portable.yaml`     | `/usr/share/{name}/{name}.yaml` |   
| Global read-only non-portable | `%PROGRAMDATA%/{name}/non-portable.yaml` | `/usr/lib/{name}/{name}.yaml`   |


