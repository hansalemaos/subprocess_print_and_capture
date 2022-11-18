import subprocess
import keyboard


def execute_subprocess(
    cmd: str, exit_keys: str = "ctrl+e", end_of_printline: str = ""
) -> list:
    def run_subprocess(cmd):
        def kill_process():
            popen.terminate()
            keyboard.remove_hotkey(kill_process)

        try:
            popen = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, universal_newlines=True
            )
            counter = -1
            for stdout_line in iter(popen.stdout.readline, ""):
                counter += 1
                if counter == 0:
                    keyboard.add_hotkey(exit_keys, kill_process)

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
    for proxyresult in run_subprocess(cmd):
        proxyresults.append(proxyresult)
        print(proxyresult, end=end_of_printline)
    return proxyresults
