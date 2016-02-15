# A few funny/handy scripts

## PC turned on

In `/etc/rc.local`:

```bash
su - romain -c /whatever/commandline.sh &
```

where `/whatever/commandline.sh` contains:

```bash
#!/bin/sh

python3 /home/romain/git/python-mailer/scripts/script-pc-turned-on.py
```