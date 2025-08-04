import psutil
import os 
def KillProcess(name):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == name:
            print("Killing the Process : ",name)
            proc.kill()

def main():
    KillProcess("msedge.exe")



if __name__ == "__main__":
    main()