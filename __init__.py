from time import sleep
import os
import random
import shlex
import subprocess
import sys
from typing import Union, Optional, Tuple, List
from time import perf_counter, time
import kthread
import psutil
import keyboard as keyboard__
from kthread_sleep import sleep
from tolerant_isinstance import isinstance_tolerant
from touchtouch import touch

outputvars = sys.modules[__name__]
outputvars.results = []

def execute_subprocess(
    cmd: str, exit_keys: str = "ctrl+e", end_of_printline: str = "", timeout=None
) -> list:
    popen = None

    t= None
    def run_subprocess(cmd):
        nonlocal t
        nonlocal popen
        def killer():
            sleep(timeout)
            kill_process()
        def kill_process():
            nonlocal popen
            try:
                print("Killing the process")
                p = psutil.Process(popen.pid)
                p.kill()
                # popen.kill()
                try:
                    if exit_keys in keyboard__.__dict__["_hotkeys"]:
                        keyboard__.remove_hotkey(exit_keys)
                except Exception:
                    try:
                        keyboard__.unhook_all_hotkeys()
                    except Exception:
                        pass
            except Exception:
                try:
                    keyboard__.unhook_all_hotkeys()
                except Exception:
                    pass

        if timeout is not None:
            t = kthread.KThread(target=killer, name=str(random.randrange(1, 100000000000)))
            t.start()

        try:
            popen = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, universal_newlines=True
            )
            counter = -1
            for stdout_line in iter(popen.stdout.readline, ""):
                counter += 1
                if counter == 0:
                    try:
                        if exit_keys not in keyboard__.__dict__["_hotkeys"]:
                            keyboard__.add_hotkey(exit_keys, kill_process)
                    except Exception:
                        pass

                try:
                    yield stdout_line
                except Exception as Fehler:
                    continue
            popen.stdout.close()
            return_code = popen.wait()
        except Exception as Fehler:
            print(Fehler)
            try:
                popen.stdout.close()
                return_code = popen.wait()
            except Exception as Fehler:
                yield ""

    proxyresults = []
    try:
        for proxyresult in run_subprocess(cmd):
            proxyresults.append(proxyresult)
            print(proxyresult, end=end_of_printline)
    except BaseException:
        try:
            p = psutil.Process(popen.pid)
            p.kill()
            popen = None
        except Exception as da:
            print(da)

    try:
        if popen is not None:
            p = psutil.Process(popen.pid)
            p.kill()
    except Exception as da:
        pass

    try:
        if exit_keys in keyboard__.__dict__["_hotkeys"]:
            keyboard__.remove_hotkey(exit_keys)
    except Exception:
        try:
            keyboard__.unhook_all_hotkeys()
        except Exception:
            pass
    try:
        if t is not None:
            if t.is_alive():
                t.kill()
    except Exception:
        pass
    return proxyresults


def execute_subprocess_multiple_commands(
    cmd: str, subcommands: list, exit_keys: str = "ctrl+x", end_of_printline: str = ""
) -> list:
    popen = None

    def run_subprocess(cmd):
        nonlocal popen

        def kill_process():
            nonlocal popen
            try:
                print("Killing the process")
                p = psutil.Process(popen.pid)
                p.kill()
                try:
                    if exit_keys in keyboard__.__dict__["_hotkeys"]:
                        keyboard__.remove_hotkey(exit_keys)
                except Exception:
                    try:
                        keyboard__.unhook_all_hotkeys()
                    except Exception:
                        pass
            except Exception:
                try:
                    keyboard__.unhook_all_hotkeys()
                except Exception:
                    pass

        try:
            read, write = os.pipe()
            for subcommand in subcommands:
                if not isinstance(subcommand, bytes):
                    subcommand = subcommand.rstrip("\n") + "\n"
                    subcommand = subcommand.encode()
                else:
                    subcommand = subcommand.rstrip(b"\n") + b"\n"
                os.write(write, subcommand)
            os.close(write)
            if exit_keys not in keyboard__.__dict__["_hotkeys"]:

                keyboard__.add_hotkey(exit_keys, kill_process)
            popen = subprocess.Popen(
                cmd,
                stdin=read,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                stderr=None,
                shell=True,
            )

            for stdout_line in iter(popen.stdout.readline, ""):
                try:
                    yield stdout_line
                except Exception as Fehler:
                    continue
            popen.stdout.close()
            return_code = popen.wait()
        except Exception as Fehler:
            print(Fehler)
            try:
                popen.stdout.close()
                return_code = popen.wait()
            except Exception as Fehler:
                yield ""

    proxyresults = []
    try:
        for proxyresult in run_subprocess(cmd):
            proxyresults.append(proxyresult)
            print(proxyresult, end=end_of_printline)
    except BaseException:
        try:
            p = psutil.Process(popen.pid)
            p.kill()
            popen = None
        except Exception as da:
            print(da)

    try:
        if popen is not None:
            p = psutil.Process(popen.pid)
            p.kill()
    except Exception as da:
        pass

    try:
        if exit_keys in keyboard__.__dict__["_hotkeys"]:
            keyboard__.remove_hotkey(exit_keys)
    except Exception:
        try:
            keyboard__.unhook_all_hotkeys()
        except Exception:
            pass
    return proxyresults


def execute_subprocess_multiple_commands_v2(
    cmd: str, subcommands: list, exit_keys: str = "ctrl+x", end_of_printline: str = ""
) -> list:
    popen = None

    def run_subprocess(cmd):
        nonlocal popen

        def kill_process():
            nonlocal popen
            try:
                print("Killing the process")
                p = psutil.Process(popen.pid)
                p.kill()
                try:
                    if exit_keys in keyboard__.__dict__["_hotkeys"]:
                        keyboard__.remove_hotkey(exit_keys)
                except Exception:
                    try:
                        keyboard__.unhook_all_hotkeys()
                    except Exception:
                        pass
            except Exception:
                try:
                    keyboard__.unhook_all_hotkeys()
                except Exception:
                    pass

        if exit_keys not in keyboard__.__dict__["_hotkeys"]:

            keyboard__.add_hotkey(exit_keys, kill_process)

        try:
            popen = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                stderr=None,
                shell=False,
            )

            for subcommand in subcommands:
                if isinstance(subcommand, bytes):
                    subcommand = subcommand.rstrip(b"\n") + b"\n"

                    subcommand = subcommand.decode("utf-8", "replace")
                else:
                    subcommand = subcommand.rstrip("\n") + "\n"

                popen.stdin.write(subcommand)

            popen.stdin.close()

            for stdout_line in iter(popen.stdout.readline, ""):
                try:
                    yield stdout_line
                except Exception as Fehler:
                    continue
            popen.stdout.close()
            return_code = popen.wait()
        except Exception as Fehler:
            print(Fehler)
            try:
                popen.stdout.close()
                return_code = popen.wait()
            except Exception as Fehler:
                yield ""

    proxyresults = []
    try:
        for proxyresult in run_subprocess(cmd):
            proxyresults.append(proxyresult)
            print(proxyresult, end=end_of_printline)
    except BaseException:
        try:
            p = psutil.Process(popen.pid)
            p.kill()
            popen = None
        except Exception as da:
            print(da)

    try:
        if popen is not None:
            p = psutil.Process(popen.pid)
            p.kill()
    except Exception as da:
        pass

    try:
        if exit_keys in keyboard__.__dict__["_hotkeys"]:
            keyboard__.remove_hotkey(exit_keys)
    except Exception:
        try:
            keyboard__.unhook_all_hotkeys()
        except Exception:
            pass
    return proxyresults


def execute_subprocess_multiple_commands_with_timeout_str(
    cmd: str, subcommands: list, exit_keys: str = "ctrl+x", end_of_printline: str = "", print_output=True, timeout=None
) -> list:
    if isinstance(subcommands, str):
        subcommands = [subcommands]
    elif isinstance(subcommands, tuple):
        subcommands = list(subcommands)
    popen = None
    t= None
    def run_subprocess(cmd):
        nonlocal t
        nonlocal popen

        def killer():
            sleep(timeout)
            kill_process()

        def kill_process():
            nonlocal popen
            try:
                print("Killing the process")
                p = psutil.Process(popen.pid)
                p.kill()
                try:
                    if exit_keys in keyboard__.__dict__["_hotkeys"]:
                        keyboard__.remove_hotkey(exit_keys)
                except Exception:
                    try:
                        keyboard__.unhook_all_hotkeys()
                    except Exception:
                        pass
            except Exception:
                try:
                    keyboard__.unhook_all_hotkeys()
                except Exception:
                    pass

        if exit_keys not in keyboard__.__dict__["_hotkeys"]:
            keyboard__.add_hotkey(exit_keys, kill_process)

        DEVNULL = open(os.devnull, "wb")
        try:
            popen = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                stderr=DEVNULL,
                shell=False,
            )

            for subcommand in subcommands:
                if isinstance(subcommand, bytes):
                    subcommand = subcommand.rstrip(b"\n") + b"\n"

                    subcommand = subcommand.decode("utf-8", "replace")
                else:
                    subcommand = subcommand.rstrip("\n") + "\n"

                popen.stdin.write(subcommand)

            popen.stdin.close()

            if timeout is not None:
                t = kthread.KThread(target=killer, name=str(random.randrange(1,100000000000)))
                t.start()

            for stdout_line in iter(popen.stdout.readline, ""):
                try:
                    yield stdout_line
                except Exception as Fehler:
                    continue
            popen.stdout.close()
            return_code = popen.wait()
        except Exception as Fehler:
            print(Fehler)
            try:
                popen.stdout.close()
                return_code = popen.wait()
            except Exception as Fehler:
                yield ""

    proxyresults = []
    try:
        for proxyresult in run_subprocess(cmd):
            proxyresults.append(proxyresult)
            if print_output:
                print(proxyresult, end=end_of_printline)
    except KeyboardInterrupt:
        try:
            p = psutil.Process(popen.pid)
            p.kill()
            popen = None
        except Exception as da:
            print(da)

    try:
        if popen is not None:
            p = psutil.Process(popen.pid)
            p.kill()
    except Exception as da:
        pass

    try:
        if exit_keys in keyboard__.__dict__["_hotkeys"]:
            keyboard__.remove_hotkey(exit_keys)
    except Exception:
        try:
            keyboard__.unhook_all_hotkeys()
        except Exception:
            pass
    try:
        if t is not None:
            if t.is_alive():
                t.kill()
    except Exception:
        pass
    return proxyresults


def execute_subprocess_multiple_commands_with_timeout_bin(
    cmd: str, subcommands: list, exit_keys: str = "ctrl+x", end_of_printline: str = "", print_output=True, timeout=None
) -> list:
    if isinstance(subcommands, str):
        subcommands = [subcommands]
    elif isinstance(subcommands, tuple):
        subcommands = list(subcommands)
    popen = None
    t= None
    def run_subprocess(cmd):
        nonlocal t
        nonlocal popen

        def killer():
            sleep(timeout)
            kill_process()

        def kill_process():
            nonlocal popen
            try:
                print("Killing the process")
                p = psutil.Process(popen.pid)
                p.kill()
                try:
                    if exit_keys in keyboard__.__dict__["_hotkeys"]:
                        keyboard__.remove_hotkey(exit_keys)
                except Exception:
                    try:
                        keyboard__.unhook_all_hotkeys()
                    except Exception:
                        pass
            except Exception:
                try:
                    keyboard__.unhook_all_hotkeys()
                except Exception:
                    pass

        if exit_keys not in keyboard__.__dict__["_hotkeys"]:
            keyboard__.add_hotkey(exit_keys, kill_process)

        DEVNULL = open(os.devnull, "wb")
        try:
            popen = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=False,
                stderr=DEVNULL,
                shell=False,
            )

            for subcommand in subcommands:
                if isinstance(subcommand, str):
                    subcommand = subcommand.rstrip("\n") + "\n"

                    subcommand = subcommand.encode()
                else:
                    subcommand = subcommand.rstrip(b"\n") + b"\n"

                popen.stdin.write(subcommand)

            popen.stdin.close()

            if timeout is not None:
                t = kthread.KThread(target=killer, name=str(random.randrange(1,100000000000)))
                t.start()

            for stdout_line in iter(popen.stdout.readline, b""):
                try:
                    yield stdout_line
                except Exception as Fehler:
                    continue
            popen.stdout.close()
            return_code = popen.wait()
        except Exception as Fehler:
            print(Fehler)
            try:
                popen.stdout.close()
                return_code = popen.wait()
            except Exception as Fehler:
                yield ""

    proxyresults = []
    try:
        for proxyresult in run_subprocess(cmd):
            proxyresults.append(proxyresult)
            if print_output:
                try:
                    print(f'{proxyresult!r}', end=end_of_printline)
                    print('')
                except Exception:
                    pass
    except KeyboardInterrupt:
        try:
            p = psutil.Process(popen.pid)
            p.kill()
            popen = None
        except Exception as da:
            print(da)

    try:
        if popen is not None:
            p = psutil.Process(popen.pid)
            p.kill()
    except Exception as da:
        pass

    try:
        if exit_keys in keyboard__.__dict__["_hotkeys"]:
            keyboard__.remove_hotkey(exit_keys)
    except Exception:
        try:
            keyboard__.unhook_all_hotkeys()
        except Exception:
            pass
    try:
        if t is not None:
            if t.is_alive():
                t.kill()
    except Exception:
        pass
    return proxyresults






def execute_as_mainprocess(
    cmd: Union[str, List[str]],
    nameofexe: Optional[str] = None,
    returnpid: bool = True,
    timeout_get_pid: int = 5,
    creationtimebreak: int = 1,
) -> Union[subprocess.Popen, psutil.Process]:
    """
    Starts a new process using the `start` command on Windows.

    Args:
        cmd (Union[str, List[str]]): The command to execute. Can be a string or a list of strings.
        nameofexe (Optional[str]): The name of the executable file to look for after the process has started. Defaults to None.
        returnpid (bool): Whether to return the PID of the new process or not. Defaults to True.
        timeout_get_pid (int): The maximum amount of time (in seconds) to wait for the new process to start. Defaults to 5.
        creationtimebreak (int): The maximum amount of time (in seconds) to wait for the new process to start after its creation time - if found, returns immediately. If not, the function returns the process after timeout_get_pid Defaults to 1.

    Returns:
        Union[subprocess.Popen, psutil.Process]: If `returnpid` is True, returns the `psutil.Process` object corresponding to the new process. Otherwise, returns the `subprocess.Popen` object that was used to start the new process.
    """
    _startupinfo = subprocess.STARTUPINFO()
    _startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    if isinstance(cmd, str):
        cmd = [cmd]
    exefile = cmd[0]
    exefile = exefile.strip().strip('"').strip()
    exefile = os.path.normpath(exefile)
    exefile = f'"{exefile}"'
    try:
        arguments = cmd[1:]
    except Exception:
        arguments = []

    args_command = " ".join(arguments).strip()
    wholecommand = f'start "" {exefile} {args_command}'
    for pp in psutil.process_iter():
        try:
            pp
        except Exception:
            pass

    p = subprocess.Popen(wholecommand, shell=True, startupinfo=_startupinfo)
    timeoutfinal = time() + timeout_get_pid
    alla = []
    if returnpid:
        while timeoutfinal > time():

            for pp in psutil.process_iter():
                try:
                    if pp.name().lower() == nameofexe.lower():
                        g = pp.create_time()

                        if time() - g < creationtimebreak:
                            print(time() - g)
                            return pp
                        alla.append((g, pp))
                except Exception as fe:
                    continue
    if alla:
        p = list(sorted(alla, key=lambda x: x[0]))[0][-1]
    return p


def _killpro(t, addhotkeys, exit_keys, popen):
    DEVNULL = open(os.devnull, "wb")
    _startupinfo = subprocess.STARTUPINFO()
    _startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    try:
        try:
            subprocess.Popen(
                f"taskkill /F /PID {popen.pid} /T",
                stdin=DEVNULL,
                stdout=DEVNULL,
                universal_newlines=False,
                stderr=DEVNULL,
                shell=False,
                creationflags=subprocess.CREATE_NO_WINDOW,
                startupinfo=_startupinfo,
            )
        except Exception as fe:
            pass
        try:
            if psutil.pid_exists(popen.pid):
                p = psutil.Process(popen.pid)
                p.kill()
        except Exception as fe:
            pass
        try:
            if t.is_alive():
                t.kill()
        except Exception as fe:
            pass
    finally:
        _unhookkeys(addhotkeys, exit_keys)
        try:
            DEVNULL.close()
        except Exception:
            pass


def _unhookkeys(addhotkeys, exit_keys):
    try:
        if addhotkeys:
            if exit_keys in keyboard__.__dict__["_hotkeys"]:
                keyboard__.remove_hotkey(exit_keys)
    except Exception:
        try:
            if addhotkeys:
                keyboard__.unhook_all_hotkeys()
        except Exception:
            pass


def execute_subprocess_multiple_commands_with_timeout_bin2(
    cmd: Union[list, str],
    subcommands: Union[list, tuple, None, str] = None,
    exit_keys: Union[str, None] = None,
    end_of_printline: str = "",
    print_output: bool = True,
    timeout: Optional[float] = None,
    cwd: str = os.getcwd(),
    decodestdout=None,
    decodestdouterrors: str = "ignore",
    stderrfile: Optional[str] = None,
    stdoutfile: Optional[str] = None,
    create_no_window: bool = True,
    use_shlex: bool = False,
    pyinstaller_module_name: Optional[str] = None,
    pyinstaller_entry: Optional[str] = None,
    argsforpyinstaller: Tuple = (),
    isthread=False,
    **kwargs,
) -> list:
    r"""
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

    :return: A list of
    """

    _startupinfofun = subprocess.STARTUPINFO()
    creationflags = 0
    if create_no_window:
        creationflags = creationflags | subprocess.CREATE_NO_WINDOW
        _startupinfofun.wShowWindow = subprocess.SW_HIDE
    if isinstance_tolerant(subcommands, str):
        subcommands = [subcommands]
    elif isinstance_tolerant(subcommands, tuple):
        subcommands = list(subcommands)
    popen = None
    t = None
    addhotkeys = not isinstance_tolerant(exit_keys, None)
    stoutputfile = None

    def run_subprocess(cmd):
        nonlocal t
        nonlocal popen
        nonlocal stderrfile
        nonlocal stoutputfile

        def killer():
            sleep(timeout)
            kill_process()

        def kill_process():
            nonlocal popen
            _killpro(t, addhotkeys, exit_keys, popen)

        if addhotkeys:
            if exit_keys not in keyboard__.__dict__["_hotkeys"]:
                keyboard__.add_hotkey(exit_keys, kill_process)

        if isinstance_tolerant(stderrfile, None):
            DEVNULL = open(os.devnull, "wb")
        else:
            stderrfile = os.path.normpath(stderrfile)
            if not os.path.exists(stderrfile):
                touch(stderrfile)
            DEVNULL = open(stderrfile, "ab")
        if not isinstance_tolerant(stdoutfile, None):
            if not os.path.exists(stdoutfile):
                touch(stdoutfile)
            stoutputfile = open(stdoutfile, "ab")
        try:
            if use_shlex:
                if isinstance_tolerant(cmd, str):
                    cmd = shlex.split(cmd)

            if not isinstance_tolerant(
                pyinstaller_module_name, None
            ) and not isinstance_tolerant(pyinstaller_entry, None):
                if getattr(sys, "frozen", False):
                    popen = subprocess.Popen(
                        [
                            os.path.join(sys._MEIPASS, pyinstaller_entry),
                            *argsforpyinstaller,
                        ],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        universal_newlines=False,
                        stderr=DEVNULL,
                        shell=False,
                        cwd=cwd,
                        creationflags=creationflags,
                        startupinfo=_startupinfofun,
                        **kwargs,
                    )

                else:
                    popen = subprocess.Popen(
                        [
                            sys.executable,
                            "-m",
                            f"{pyinstaller_module_name}.{pyinstaller_entry}",
                            *argsforpyinstaller,
                        ],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        universal_newlines=False,
                        stderr=DEVNULL,
                        shell=False,
                        cwd=cwd,
                        creationflags=creationflags,
                        startupinfo=_startupinfofun,
                        **kwargs,
                    )
            else:

                popen = subprocess.Popen(
                    cmd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    universal_newlines=False,
                    stderr=DEVNULL,
                    shell=False,
                    cwd=cwd,
                    creationflags=creationflags,
                    startupinfo=_startupinfofun,
                    **kwargs,
                )

            if not isinstance_tolerant(subcommands, None):
                for subcommand in subcommands:
                    if isinstance(subcommand, str):
                        subcommand = subcommand.rstrip("\n") + "\n"

                        subcommand = subcommand.encode()
                    else:
                        subcommand = subcommand.rstrip(b"\n") + b"\n"

                    popen.stdin.write(subcommand)

            popen.stdin.close()

            if not isinstance_tolerant(timeout, None):
                t = kthread.KThread(
                    target=killer,
                    name=str(perf_counter() + random.randrange(1, 100000000000)),
                )
                t.start()

            woutput = not isinstance_tolerant(stoutputfile, None)
            dodecode = not isinstance_tolerant(decodestdout, None)
            for stdout_line in iter(popen.stdout.readline, b""):
                try:
                    if woutput:
                        try:
                            stoutputfile.write(stdout_line)
                        except Exception as fe:
                            print(fe)
                    if dodecode:
                        stdout_line = stdout_line.decode(
                            decodestdout, decodestdouterrors
                        )

                    yield stdout_line
                except Exception as Fehler:
                    continue
            popen.stdout.close()
            return_code = popen.wait()
        except Exception as Fehler:

            try:
                popen.stdout.close()
                return_code = popen.wait()
            except Exception as Fehler:
                yield ""
        finally:
            if not isinstance_tolerant(stderrfile, None):
                try:
                    DEVNULL.close()
                except Exception as fe:
                    pass
            if not isinstance_tolerant(stdoutfile, None):
                try:
                    stoutputfile.close()
                except Exception as fe:
                    pass

    proxyresults = []
    keyex = False
    try:
        for proxyresult in run_subprocess(cmd):
            proxyresults.append(proxyresult)
            if print_output:
                try:
                    print(f"{proxyresult!r}", end=end_of_printline)
                    print("")
                except Exception:
                    pass

    except KeyboardInterrupt:
        keyex = True
        _killpro(t, addhotkeys, exit_keys, popen)

    if not keyex:
        _killpro(t, addhotkeys, exit_keys, popen)
    if isthread:
        outputvars.results.append(proxyresults)
    return proxyresults


def execute_subprocess_multiple_commands_with_timeout_bin2_thread(
    cmd: Union[list, str],
    subcommands: Union[list, tuple, None, str] = None,
    exit_keys: Union[str, None] = None,
    end_of_printline: str = "",
    print_output: bool = True,
    timeout: Optional[float] = None,
    cwd: str = os.getcwd(),
    decodestdout=None,
    decodestdouterrors: str = "ignore",
    stderrfile: Optional[str] = None,
    stdoutfile: Optional[str] = None,
    CREATE_NO_WINDOW: bool = True,
    use_shlex: bool = False,
    pyinstaller_module_name: Optional[str] = None,
    pyinstaller_entry: Optional[str] = None,
    argsforpyinstaller: Tuple = (),
    **kwargs,
) -> None:
    t = kthread.KThread(
        target=execute_subprocess_multiple_commands_with_timeout_bin2,
        name=str(perf_counter() + random.randrange(1, 100000000000)),
        # args=args,
        kwargs={
            "cmd": cmd,
            "subcommands": subcommands,
            "exit_keys": exit_keys,
            "end_of_printline": end_of_printline,
            "print_output": print_output,
            "timeout": timeout,
            "cwd": cwd,
            "decodestdout": decodestdout,
            "decodestdouterrors": decodestdouterrors,
            "stderrfile": stderrfile,
            "stdoutfile": stdoutfile,
            "create_no_window": CREATE_NO_WINDOW,
            "use_shlex": use_shlex,
            "pyinstaller_module_name": pyinstaller_module_name,
            "pyinstaller_entry": pyinstaller_entry,
            "argsforpyinstaller": argsforpyinstaller,
            "isthread": True,
        }
        | kwargs,
    )
    t.start()
