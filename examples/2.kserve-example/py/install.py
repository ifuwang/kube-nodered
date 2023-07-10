import os
import subprocess

def python3_version():
    return subprocess.check_call(["python3", "--version"])

def which(command):
    return subprocess.check_call(["which", command])

def pip3_install_requirements():
    return subprocess.check_call(["pip3", "install", "-r", "requirements.txt", "--upgrade", "--user"])

def pip3_install_kfp():
    return subprocess.check_call(["pip3", "install",
                                  "git+https://github.com/kubeflow/pipelines.git@1.8.19#subdirectory=backend/api/python_http_client",
                                  "--user"])

def pip3_install_kubernetes():
    return subprocess.check_call(["pip3", "install", "kubernetes>=12.0.0"])

def pip3_install_opencv():
    return subprocess.check_call(["pip3", "install", "opencv-python", "--user"])


python3_version()
pip3_install_requirements()
pip3_install_kfp()
pip3_install_kubernetes()
# pip3_install_opencv()

print("done")
