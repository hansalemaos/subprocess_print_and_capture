# Print and capture the output of a subprocess simultaneously


```python

$pip install subprocess-print-and-capture

from subprocess_print_and_capture import execute_subprocess, execute_subprocess_multiple_commands, execute_subprocess_multiple_commands_v2



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

 
# Update 2023-03-14:  Added some new stuff:
execute_subprocess_multiple_commands_with_timeout_bin2
    Executes a subprocess and runs one or more commands in it, with the option to add a timeout and exit keys.

    :param cmd: The command to be executed in the subprocess.
    :type cmd: str

    :param subcommands: Additional commands to run in the subprocess, as a list or tuple of strings or a single string. Defaults to None.
    :type subcommands: Union[list, tuple, None, str]

    :param exit_keys: If set, the process can be terminated by pressing the specified key combination (e.g. "ctrl+alt+x"). Defaults to None.
    :type exit_keys: Union[str, None]

    :param end_of_printline: The string to be printed at the end of each line of output. Defaults to "".
    :type end_of_printline: str

    :param print_output: Whether to print the output of the subprocess to the console. Defaults to True.
    :type print_output: bool

    :param timeout: The maximum amount of time to allow the subprocess to run before terminating it. Defaults to None.
    :type timeout: Optional[float]

    :param cwd: The working directory for the subprocess. Defaults to the current working directory.
    :type cwd: str

    :param decodestdout: The character encoding to use for decoding the output of the subprocess. Defaults to None.
    :type decodestdout: Optional[str]

    :param decodestdouterrors: The error handling mode to use for decoding the output of the subprocess. Defaults to "ignore".
    :type decodestdouterrors: str

    :param stderrfile: The file path to write standard error output to. Defaults to None.
    :type stderrfile: Optional[str]

    :param stdoutfile: The file path to write standard output to. Defaults to None.
    :type stdoutfile: Optional[str]

    :param create_no_window: Whether to create a new console window for the subprocess. Defaults to True.
    :type create_no_window: bool

    :param use_shlex: Whether to use the shlex module to split the command string into arguments. Defaults to False.
    :type use_shlex: bool

    :param pyinstaller_module_name: The name of the PyInstaller module to run in the subprocess. Defaults to None.
    :type pyinstaller_module_name: Optional[str]

    :param pyinstaller_entry: The name of the PyInstaller entry point to run in the subprocess. Defaults to None.
    :type pyinstaller_entry: Optional[str]

    :param argsforpyinstaller: Additional arguments to pass to the PyInstaller subprocess. Defaults to ().
    :type argsforpyinstaller: Tuple

    :param kwargs: Additional keyword arguments to pass to the subprocess.Popen() constructor.
    :type kwargs: Any

    :return: A list 

execute_as_mainprocess
    Starts a new process using the `start` command on Windows.

    Args:
        cmd (Union[str, List[str]]): The command to execute. Can be a string or a list of strings.
        nameofexe (Optional[str]): The name of the executable file to look for after the process has started. Defaults to None.
        returnpid (bool): Whether to return the PID of the new process or not. Defaults to True.
        timeout_get_pid (int): The maximum amount of time (in seconds) to wait for the new process to start. Defaults to 5.
        creationtimebreak (int): The maximum amount of time (in seconds) to wait for the new process to start after its creation time - if found, returns immediately. If not, the function returns the process after timeout_get_pid Defaults to 1.

    Returns:
        Union[subprocess.Popen, psutil.Process]: If `returnpid` is True, returns the `psutil.Process` object corresponding to the new process. Otherwise, returns the `subprocess.Popen` object that was used to start the new process.

# Examples
adb_path = "C:\\Users\\Gamer\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe"
deviceserial = "localhost:62037"
cmd2 = f"adb -s {deviceserial} shell su -c 'ls -la'"
for q in range(2):
    pap = execute_subprocess_multiple_commands_with_timeout_bin2(cmd=cmd2)
    with open("c:\\asdfasdfasdfasdfasdfasdf.txt", mode="a", encoding="utf-8") as f:
        f.write(b"".join(pap).decode("utf-8", "ignore"))

for q in range(2):
    pap = execute_subprocess_multiple_commands_with_timeout_bin2(
        cmd=cmd2,
        decodestdout="utf-8",
        decodestdouterrors="ignore",
        stdoutfile="f:\\lologo.txt",
    )
    print(pap)
    with open("c:\\asdfasdfasdfasdfasdfasdf.txt", mode="a", encoding="utf-8") as f:
        f.write("".join(pap))

for q in range(2):
    pap = execute_subprocess_multiple_commands_with_timeout_bin2(
        cmd='dir /bvabds /dsxds ""', stderrfile="f:\\testtestloglog.txt"
    )
    with open("c:\\asdfasdfasdfasdfasdfasdf.txt", mode="a", encoding="utf-8") as f:
        f.write(b"".join(pap).decode("utf-8", "ignore"))

for q in range(2):
    pap = execute_subprocess_multiple_commands_with_timeout_bin2(
        cmd='dir /b ""',
        stderrfile="f:\\testtestloglog.txt",
        stdoutfile="f:\\lologo.txt",
    )
    with open("c:\\asdfasdfasdfasdfasdfasdf.txt", mode="a", encoding="utf-8") as f:
        f.write(b"".join(pap).decode("utf-8", "ignore"))


pap = execute_subprocess_multiple_commands_with_timeout_bin2(
    cmd="notepad.exe", subcommands=None, timeout=2
)

for q in range(2):
    pap = execute_subprocess_multiple_commands_with_timeout_bin2(
        cmd=["ls"],
        stderrfile="f:\\testtestloglog.txt",
        stdoutfile="c:\\locccclogo.txt",
    )

mainp = execute_as_mainprocess(
    cmd="notepad.exe",
    nameofexe="notepad.exe",
    returnpid=True,
    timeout_get_pid=5,
    creationtimebreak=1,
)
print(mainp)

pap = execute_subprocess_multiple_commands_with_timeout_bin2(
    cmd='notepad.exe "C:\locccclogo.txt"',
    stdoutfile="c:\\locccclogo.txt2",
    stderrfile="f:\\testtestloglog2.txt",
    subcommands=None,
    timeout=2,
    use_shlex=True,
)

bab = execute_subprocess_multiple_commands_with_timeout_bin2(
    cmd="notepad.exe",
    subcommands=None,
    exit_keys=None,
    end_of_printline="",
    print_output=True,
    timeout=None,
    cwd=os.getcwd(),
    decodestdout=None,
    decodestdouterrors="ignore",
    stdoutfile="c:\\locccclogo3.txt",
    stderrfile="f:\\testtestloglog3.txt",
    create_no_window=False,
    use_shlex=False,
    pyinstaller_module_name="tes",
    pyinstaller_entry="tete",
    argsforpyinstaller=(),
)


bab2 = execute_subprocess_multiple_commands_with_timeout_bin2_thread(
    cmd="dir",
    subcommands=None,
    exit_keys=None,
    end_of_printline="",
    print_output=True,
    timeout=None,
    cwd=os.getcwd(),
    decodestdout=None,
    decodestdouterrors="ignore",
    stdoutfile="c:\\locccclogo3.txt",
    stderrfile="f:\\testtestloglog3.txt",
    CREATE_NO_WINDOW=False,
    use_shlex=False,
    pyinstaller_module_name="tes",
    pyinstaller_entry="tete",
    argsforpyinstaller=(),
)

```
