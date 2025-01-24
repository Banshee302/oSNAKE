import subprocess
import sys
import os

class CobraPackageManager:
    def __init__(self):
        self.installed_packages = {}

    def install(self, package_name):
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True)
            self.installed_packages[package_name] = True
            print(f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install package '{package_name}': {e}")

    def uninstall(self, package_name):
        try:
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", package_name], check=True)
            if package_name in self.installed_packages:
                del self.installed_packages[package_name]
            print(f"Package '{package_name}' uninstalled successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to uninstall package '{package_name}': {e}")

    def list_installed(self):
        installed = subprocess.check_output([sys.executable, "-m", "pip", "list"]).decode('utf-8')
        print("Installed packages:")
        print(installed)

def main():
    manager = CobraPackageManager()
    while True:
        command = input("cobra> ").strip()
        if command.startswith("install"):
            package_name = command.split()[1]
            manager.install(package_name)
        elif command.startswith("uninstall"):
            package_name = command.split()[1]
            manager.uninstall(package_name)
        elif command == "list":
            manager.list_installed()
        elif command == "exit":
            break
        else:
            print("Unknown command. Use 'install <package>', 'uninstall <package>', 'list', or 'exit'.")

if __name__ == "__main__":
    main()
