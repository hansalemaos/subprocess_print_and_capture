# Print and capture the output of a subprocess simultaneously


```python

$pip install subprocess-print-and-capture

from subprocess_print_and_capture import execute_subprocess, execute_subprocess_multiple_commands, execute_subprocess_multiple_commands_v2

# -----------------------------------------------------------------------------------------------------------------------------
# Update 2022-12-01: added timeout / new functions
cmd = r"ls -R -s -i -n -H"
results = execute_subprocess(cmd, exit_keys="ctrl+e", end_of_printline="",timeout=2) # Useful if the process is frozen, will return the captured stdout

from subprocess_print_and_capture import execute_subprocess, execute_subprocess_multiple_commands, execute_subprocess_multiple_commands_v2,execute_subprocess_multiple_commands_with_timeout_bin ,execute_subprocess_multiple_commands_with_timeout_str  

adb_path = "C:\\Users\\Gamer\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe"
deviceserial = "localhost:5745"
cmd = rf"{adb_path} -s {deviceserial} shell"
subcommands=["ls", "sleep 1", "ls -R -s -i -n -H"]
results1 = execute_subprocess_multiple_commands_with_timeout_bin(cmd=cmd, subcommands=subcommands, exit_keys="ctrl+e", end_of_printline="",print_output=True,timeout=2) # returns a list containing bin (to avoid encoding problems)
results2 = execute_subprocess_multiple_commands_with_timeout_str(cmd=cmd, subcommands=subcommands, exit_keys="ctrl+e", end_of_printline="",print_output=True,timeout=2) # returns a list containing str

# -----------------------------------------------------------------------------------------------------------------------------

# Update: you can now pass multiple "subcommands", you will see the output on screen, get the printed text as a list, and can kill the process with a hotkey (and still getting the output)  
adboutput = execute_subprocess_multiple_commands(
    "adb shell", ["ls", "sleep 1", "ls -R -s -i -n -H"], exit_keys="ctrl+x"
)
adboutput = execute_subprocess_multiple_commands_v2(
    "adb shell", ["ls", "sleep 1", "ls -R -s -i -n -H"], exit_keys="ctrl+x"
) #alternative, works sometimes better


# output screen
acct
boot
bugreports
cache
charger
config
d
data
default.prop
dev
etc
file_contexts.bin
fstab.nougat
fstab_sdcard.nougat
init
init.environ.rc
init.nougat.rc
init.rc
init.usb.configfs.rc
init.usb.rc
init.zygote32.rc
lib
mnt
oem
proc
property_contexts
root
sbin
sdcard
seapp_contexts
selinux_version
sepolicy
service_contexts
storage
sys
system
ueventd.nougat.rc
ueventd.rc
vendor


adboutput
Out[3]: 
['acct\n',
 'boot\n',
 'bugreports\n',
 'cache\n',
 'charger\n',
 'config\n',
 'd\n',
 'data\n',
 'default.prop\n',
 'dev\n',
 'etc\n',
 'file_contexts.bin\n',
 'fstab.nougat\n',
 'fstab_sdcard.nougat\n',
 'init\n',
 'init.environ.rc\n',
 'init.nougat.rc\n',
 'init.rc\n',
 'init.usb.configfs.rc\n',
 'init.usb.rc\n',
 'init.zygote32.rc\n',
 'lib\n',
 'mnt\n',
 'oem\n',
 'proc\n',
 'property_contexts\n',
 'root\n',
 'sbin\n',
 'sdcard\n',
 'seapp_contexts\n',
 'selinux_version\n',
 'sepolicy\n',
 'service_contexts\n',
 'storage\n',
 'sys\n',
 'system\n',
 'ueventd.nougat.rc\n',
 'ueventd.rc\n',
 'vendor\n',
 '.:\n',
 'total 1680\n',
 '     1    0 dr-xr-xr-x  68 0    0          0 2022-11-19 15:28 acct\n',
 '  3524    0 drwxrwxr-x   6 1000 1000     240 2022-11-19 15:28 boot\n',
 '  4108    0 lrwxrwxrwx   1 0    0         50 2022-11-19 15:28 bugreports -> /data/user_de/0/com.android.shell/files/bugreports\n',
 '  6103    0 drwxrwx---   6 1000 2001     120 2022-11-19 15:28 cache\n',
 '  4110    0 lrwxrwxrwx   1 0    0         13 2022-11-19 15:28 charger -> /sbin/healthd\n',
 '  4111    0 dr-x------   2 0    0         40 2022-11-19 15:28 config\n',
 '  4112    0 lrwxrwxrwx   1 0    0         17 2022-11-19 15:28 d -> /sys/kernel/debug\n',
 '     2    8 drwxrwx--x  38 1000 1000    4096 2022-11-19 15:28 data\n',
 '  4114    4 -rw-r--r--   1 0    0        958 2022-11-19 15:28 default.prop\n',
 '  4387    0 drwxr-xr-x  13 0    0       3840 2022-11-19 15:28 dev\n',
 '  4115    0 lrwxrwxrwx   1 0    0         11 2022-11-19 15:28 etc -> /system/etc\n',
 '  4116   76 -rw-r--r--   1 0    0      77090 2022-11-19 15:28 file_contexts.bin\n',
 '  4117    4 -rw-r-----   1 0    0        564 2022-11-19 15:28 fstab.nougat\n',
 '  4118    4 -rw-r-----   1 0    0        354 2022-11-19 15:28 fstab_sdcard.nougat\n',
 '  4119 1304 -rwxr-x---   1 0    0    1334780 2022-11-19 15:28 init\n',
 '  4120    4 -rwxr-x---   1 0    0        887 2022-11-19 15:28 init.environ.rc\n',
 '  4121    4 -rwxr-x---   1 0    0       3690 2022-11-19 15:28 init.nougat.rc\n',
 '  4122   28 -rwxr-x---   1 0    0      27803 2022-11-19 15:28 init.rc\n',
 '  4123   12 -rwxr-x---   1 0    0       9283 2022-11-19 15:28 init.usb.configfs.rc\n',
 '  4124    8 -rwxr-x---   1 0    0       5694 2022-11-19 15:28 init.usb.rc\n',
 '  4125    4 -rwxr-x---   1 0    0        411 2022-11-19 15:28 init.zygote32.rc\n',
 '  4443    0 lrwxrwxrwx   1 0    0         10 2022-11-19 15:28 lib -> system/lib\n',
 '  4457    0 drwxr-xr-x  11 0    1000     240 2022-11-19 15:28 mnt\n',
 '  4127    0 drwxr-xr-x   2 0    0         40 2022-11-19 15:28 oem\n',


# -----------------------------------------------------------------------------------------------------------------------------

cmd = r"""adb shell getevent -l"""
results = execute_subprocess(cmd, exit_keys="ctrl+e", end_of_printline="")

#output on screen
add device 1: /dev/input/event3
  name:     "fts"
add device 2: /dev/input/event2
  name:     "STM VL53L1 proximity sensor"
add device 3: /dev/input/event1
  name:     "qwerty"
add device 4: /dev/input/event0
  name:     "gpio_keys"
/dev/input/event3: EV_KEY       BTN_TOUCH            DOWN                
/dev/input/event3: EV_ABS       ABS_MT_TRACKING_ID   00001830            
/dev/input/event3: EV_ABS       ABS_MT_POSITION_X    00000299            
/dev/input/event3: EV_ABS       ABS_MT_POSITION_Y    000006f5            
/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MAJOR   00000040            
/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MINOR   00000030            
/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      0000000d            
/dev/input/event3: EV_SYN       SYN_REPORT           00000000            
/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MAJOR   00000080            
/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MINOR   00000080            
/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      00000022            
/dev/input/event3: EV_SYN       SYN_REPORT           00000000            
/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MINOR   00000070            
/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      00000028            
/dev/input/event3: EV_SYN       SYN_REPORT           00000000            
/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      0000002a      
....


results
Out[3]: 
['add device 1: /dev/input/event3\n',
 '  name:     "fts"\n',
 'add device 2: /dev/input/event2\n',
 '  name:     "STM VL53L1 proximity sensor"\n',
 'add device 3: /dev/input/event1\n',
 '  name:     "qwerty"\n',
 'add device 4: /dev/input/event0\n',
 '  name:     "gpio_keys"\n',
 '/dev/input/event3: EV_KEY       BTN_TOUCH            DOWN                \n',
 '/dev/input/event3: EV_ABS       ABS_MT_TRACKING_ID   00001830            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_POSITION_X    00000299            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_POSITION_Y    000006f5            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MAJOR   00000040            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MINOR   00000030            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      0000000d            \n',
 '/dev/input/event3: EV_SYN       SYN_REPORT           00000000            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MAJOR   00000080            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MINOR   00000080            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      00000022            \n',
 '/dev/input/event3: EV_SYN       SYN_REPORT           00000000            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MINOR   00000070            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      00000028            \n',
 '/dev/input/event3: EV_SYN       SYN_REPORT           00000000            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      0000002a            \n',
 '/dev/input/event3: EV_SYN       SYN_REPORT           00000000            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_POSITION_X    0000029a            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_POSITION_Y    000006f4            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_TOUCH_MINOR   00000080            \n',
 '/dev/input/event3: EV_ABS       ABS_MT_PRESSURE      0000002c            \n',
 ....
 
```
