# Print and capture the output of a subprocess simultaneously


```python

$pip install subprocess-print-and-capture

from subprocess_print_and_capture import execute_subprocess
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