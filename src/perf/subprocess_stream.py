import subprocess
def stream_git_log(cmd: list, cwd: str):
    return subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, text=True)
