# colab_utils
It aims to be a repository with various scripts that help make it easier to work in collaboration


## Tensorboard 
This part was extract from https://github.com/mixuala/colab_utils
create a public `tensorboard` URL using secure introspective tunnels via `ngrok`

When training on `colaboratory` VMs it it often useful to monitor the session via 
`tensorboard`. This script helps you launches tensorboard on the `colaboratory` VM and 
uses `ngrok` to create a secure introspective tunnel to access tensorboard via public URL.

```
************************************
*     A simple working script      *
************************************

import os
import colab_utils.tboard

# set paths
ROOT = %pwd
LOG_DIR = os.path.join(ROOT, 'log')

# will install `ngrok`, if necessary
# will create `log_dir` if path does not exist
colab_utils.tboard.launch_tensorboard( bin_dir=ROOT, log_dir=LOG_DIR )

```

### `launch_tensorboard( bin_dir=ROOT, log_dir=LOG_DIR )`
launch tensorboard on `colaboratory` VM and open a tunnel for access by public URL. Automatically installs `ngrok`. if necessary.

```
tboard.launch_tensorboard( bin_dir=ROOT, log_dir=LOG_DIR )
```


### `install_ngrok( bin_dir=ROOT )`
install `ngrok` package, if necessary

```
tboard.install_ngrok( bin_dir=ROOT, log_dir=LOG_DIR )
```


##Git


##Object Detection

