import os
import subprocess
import keyboard as keyboard__
import psutil


def execute_subprocess(
    cmd: str, exit_keys: str = "ctrl+e", end_of_printline: str = ""
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
    return proxyresults



def execute_subprocess_multiple_commands(
    cmd: str, subcommands:list, exit_keys: str = "ctrl+x", end_of_printline: str = ""
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
                shell=False,
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
