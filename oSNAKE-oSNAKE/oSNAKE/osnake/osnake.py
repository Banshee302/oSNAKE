# PLEASE AVOID EDITING OSNAKE SOURCE CODE.
# IF YOU NEED DEBUG HELP TO ASSESS DEBUGS AND SCRIPT ERRORS CHECK DOCUMENTATION.txt FOR HELP.
import subprocess
import sys

def install_libraries():
    libraries = [
        "paramiko", "requests", "matplotlib", "numpy", "pandas", 
        "beautifulsoup4", "scikit-learn", "cryptography", "flask", 
        "opencv-python", "beautifultable"
    ]

    for library in libraries:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

if __name__ == "__main__":
    install_libraries()

import paramiko

class OSnakeInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.ssh_client = None

    def execute(self, code):
        lines = code.split('\n')
        for line in lines:
            self.process_line(line.strip())

    def process_line(self, line):
        if not line:
            return
        if line.startswith('DATA'):
            self.handle_data_section(line)
        elif line.startswith('data'):
            self.handle_data_declaration(line)
        elif line.startswith('print'):
            self.handle_print(line)
        elif line.startswith('if'):
            self.handle_if_statement(line)
        elif line.startswith('func'):
            self.handle_function_declaration(line)
        elif line in self.functions:
            self.execute(self.functions[line])
        elif line.startswith('dir='):
            self.handle_directory(line)
        elif line.startswith('set --filepath'):
            self.setup_directories(line)
        elif line == 'osnakepad':
            self.open_osnakepad()
        elif line.startswith('run'):
            self.run_osnake_file(line)
        elif line.endswith('.osnake'):
            self.run_osnake_file(f'run {line}')
        elif line == 'exit':
            print("Exiting osnake interpreter.")
            exit()
        elif line.startswith('fixme'):
            self.handle_fixme(line.replace('fixme', '').strip())
        elif line.startswith('module.ssh'):
            self.handle_ssh_command(line.replace('module.ssh', '').strip())
        elif line.startswith('module.http'):
            self.handle_http_command(line.replace('module.http', '').strip())
        elif line.startswith('module.plot'):
            self.handle_plot_command(line.replace('module.plot', '').strip())
        elif line.startswith('module.math'):
            self.handle_math_command(line.replace('module.math', '').strip())
        elif line.startswith('module.dataframe'):
            self.handle_dataframe_command(line.replace('module.dataframe', '').strip())
        elif line.startswith('module.web'):
            self.handle_web_command(line.replace('module.web', '').strip())
        elif line.startswith('module.database'):
            self.handle_database_command(line.replace('module.database', '').strip())
        elif line.startswith('module.ml'):
            self.handle_ml_command(line.replace('module.ml', '').strip())
        elif line.startswith('module.crypto'):
            self.handle_crypto_command(line.replace('module.crypto', '').strip())
        elif line.startswith('module.webapp'):
            self.handle_webapp_command(line.replace('module.webapp', '').strip())
        elif line.startswith('module.cv'):
            self.handle_cv_command(line.replace('module.cv', '').strip())
        elif line.startswith('module.table'):
            self.handle_table_command(line.replace('module.table', '').strip())
        elif line.startswith('module.network'):
            self.handle_network_command(line.replace('module.network', '').strip())
        else:
            print(f"Unknown command: {line}")

    # Placeholder methods for other commands (implement them as needed)
    def handle_data_section(self, line):
        pass

    def handle_data_declaration(self, line):
        pass

    def handle_print(self, line):
        pass

    def handle_if_statement(self, line):
        pass

    def handle_function_declaration(self, line):
        pass

    def handle_directory(self, line):
        pass

    def setup_directories(self, line):
        pass

    def open_osnakepad(self):
        pass

    def run_osnake_file(self, line):
        pass

    def handle_fixme(self, line):
        pass

    def handle_ssh_command(self, line):
        pass

    def handle_http_command(self, line):
        pass

    def handle_plot_command(self, line):
        pass

    def handle_math_command(self, line):
        pass

    def handle_dataframe_command(self, line):
        pass

    def handle_web_command(self, line):
        pass

    def handle_database_command(self, line):
        pass

    def handle_ml_command(self, line):
        pass

    def handle_crypto_command(self, line):
        pass

    def handle_webapp_command(self, line):
        pass

    def handle_cv_command(self, line):
        pass

    def handle_table_command(self, line):
        pass

    def handle_network_command(self, line):
        pass

# Main loop
interpreter = OSnakeInterpreter()
print("oSNAKE interpreter. Type 'osnakepad' to edit scripts, 'run <filename>' to execute .osnake files, 'set --filepath <path>' to set up directories, 'fixme' to enter FixMe shell, 'exit' to quit.")
while True:
    code = input('> ')
    if code == 'fixme':
        interpreter.fix_me_shell()
    else:
        interpreter.execute(code)

# Main loop
interpreter = OSnakeInterpreter()
print("oSNAKE interpreter. Type 'osnakepad' to edit scripts, 'run <filename>' to execute .osnake files, 'set --filepath <path>' to set up directories, 'fixme' to enter FixMe shell, 'exit' to quit.")
while True:
    code = input('> ')
    if code == 'fixme':
        interpreter.fix_me_shell()
    else:
        interpreter.execute(code)


class OSnakeInterpreter:
 import sys
 import os
 libs_path = os.path.join(os.path.dirname(__file__), "osnake/libs")
 sys.path.append(libs_path)

def __init__(self):
        self.variables = {}
        self.functions = {}

def execute(self, code):
        lines = code.split('\n')
        for line in lines:
            self.process_line(line.strip())

def process_line(self, line):
        if not line:
            return
        if line.startswith('DATA'):
            self.handle_data_section(line)
        elif line.startswith('data'):
            self.handle_data_declaration(line)
        elif line.startswith('print'):
            self.handle_print(line)
        elif line.startswith('if'):
            self.handle_if_statement(line)
        elif line.startswith('func'):
            self.handle_function_declaration(line)
        elif line in self.functions:
            self.execute(self.functions[line])
        elif line.startswith('dir='):
            self.handle_directory(line)
        elif line.startswith('set --filepath'):
            self.setup_directories(line)
        elif line == 'osnakepad':
            self.open_osnakepad()
        elif line.startswith('run'):
            self.run_osnake_file(line)
        elif line.endswith('.osnake'):
            self.run_osnake_file(f'run {line}')
        elif line == 'exit':
            print("Exiting osnake interpreter.")
            exit()
        elif line.startswith('fixme'):
            self.handle_fixme(line.replace('fixme', '').strip())
        else:
            print(f"Unknown command: {line}")

def handle_data_section(self, line):
        try:
            data_str = line.replace('DATA[', '').replace(']', '')
            data_pairs = data_str.split(',')
            for pair in data_pairs:
                var_name, var_value = pair.split('=')
                self.variables[var_name.strip()] = eval(var_value.strip())
        except Exception as e:
            print(f"Error in DATA section: {e}")

def handle_data_declaration(self, line):
        try:
            parts = line.split('=')
            var_name = parts[0].replace('data', '').strip()
            var_value = parts[1].strip()
            self.variables[var_name] = eval(var_value)
            print(f"Data variable '{var_name}' set to {var_value}")
        except Exception as e:
            print(f"Error in data declaration: {e}")

def handle_print(self, line):
        try:
            if '>' in line:
                parts = line.split('>')
                expression = parts[0].replace('print(', '').replace(')', '').strip()
                file_path = parts[1].strip()
                value = eval(expression, {}, self.variables)
                with open(file_path, 'a') as file:
                    file.write(str(value) + '\n')
                print(f"Printed to file: {file_path}")
            else:
                expression = line.replace('print(', '').replace(')', '').strip()
                value = eval(expression, {}, self.variables)
                print(value)
        except Exception as e:
            print(f"Error in print statement: {e}")

def handle_if_statement(self, line):
        try:
            condition = line[line.find("[")+1:line.find("]")]
            body = line[line.find("then")+5:].strip()
            if eval(condition, {}, self.variables):
                self.process_line(body)
        except Exception as e:
            print(f"Error in if statement: {e}")

def handle_function_declaration(self, line):
        try:
            parts = line.split('{')
            func_name = parts[0].replace('func', '').strip()
            func_body = parts[1].replace('}', '').strip()
            self.functions[func_name] = func_body
        except Exception as e:
            print(f"Error in function declaration: {e}")

def handle_directory(self, line):
        try:
            parts = line.split(' ')
            dir_path = parts[0].replace('dir=', '').strip()
            output_file = parts[1].replace('output=', '').strip()
            data_content = ' '.join(parts[2:])

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            with open(os.path.join(dir_path, output_file), 'w') as file:
                file.write(data_content)
                print(f"Data saved to {os.path.join(dir_path, output_file)}")

            self.variables["directory"] = dir_path
        except Exception as e:
            print(f"Error in directory command: {e}")

def setup_directories(self, line):
        try:
            base_path = line.replace('set --filepath', '').strip()
            directories = ['DATA', 'Errors', 'osnake-lib']

            for directory in directories:
                dir_path = os.path.join(base_path, directory)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                    print(f"Created directory: {dir_path}")

            self.variables["base_path"] = base_path
            print(f"Directories set up at: {base_path}")
        except Exception as e:
            print(f"Error in setup_directories command: {e}")

def open_osnakepad(self):
        filename = input("Enter filename to edit (or 'exit' to cancel): ")
        if filename.lower() == 'exit':
            return

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read()
        else:
            content = ""

        print("Opening osnakepad. Type ':w' to save and ':q' to quit.")
        lines = content.split('\n')

        while True:
            line = input()
            if line == ':q':
                break
            elif line == ':w':
                with open(filename, 'w') as file:
                    file.write('\n'.join(lines))
                print(f"File '{filename}' saved.")
            else:
                lines.append(line)

def run_osnake_file(self, line):
        try:
            filename = line.replace('run', '').strip()
            if not filename.endswith('.osnake'):
                print(f"Error: '{filename}' is not a .osnake file.")
                return
            with open(filename, 'r') as file:
                code = file.read()
            self.execute(code)
        except Exception as e:
            print(f"Error running file '{filename}': {e}")

def fix_me(self, file_path):
        try:
            with open(file_path, 'r') as file:
                code = file.readlines()

            fixed_code = []
            for line in code:
                fixed_line = self.fix_line(line.strip())
                fixed_code.append(fixed_line)

            with open(file_path, 'w') as file:
                file.write('\n'.join(fixed_code))

            print(f"File '{file_path}' has been checked and fixed if necessary.")
        except Exception as e:
            print(f"Error in FixMe feature: {e}")

def fix_line(self, line):
        # Example error checks and fixes
        if '==' not in line and 'if' in line:
            line = line.replace('=', '==')
        if 'print' in line and '(' not in line:
            line = line.replace('print ', 'print(').replace(' ', ') ')
        return line

def fix_me_shell(self):
        print("Entering FixMe shell. Type 'exit' to leave the shell.")
        while True:
            command = input("FixMe> ")
            if command == "exit":
                break
            elif command.startswith("fixme --debug"):
                file_path = command.replace("fixme --debug", "").strip()
                if os.path.exists(file_path):
                    self.fix_me(file_path)
                else:
                    print(f"File '{file_path}' not found.")
            else:
                print("Unknown FixMe command. Use 'fixme --debug <file>' to debug a script.")

def download_and_extract_osnake():
    url = "https://github.com/Banshee302/oSNAKE/releases/download/oSNAKE/osnake.zip"
    install_dir = input("Enter the directory to install oSNAKE: ")
    zip_path = os.path.join(install_dir, "osnake.zip")

    # Create the extraction directory
    os.makedirs(install_dir, exist_ok=True)

    # Use curl to download the oSNAKE zip file
    curl_command = f"curl -L {url} -o {zip_path}"
    subprocess.run(curl_command, shell=True)
    print("oSNAKE downloaded successfully.")

    # Extract the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(install_dir)
    print(f"oSNAKE extracted to {install_dir}.")

    # Remove the zip file
    os.remove(zip_path)
    print("Zip file removed after extraction.")


# Main loop
interpreter = OSnakeInterpreter()
print("oSNAKE interpreter. Type 'osnakepad' to edit scripts, 'run <filename>' to execute .osnake files, 'set --filepath <path>' to set up directories, 'fixme' to enter FixMe shell, 'exit' to quit.")
while True:
    code = input('> ')
    if code == 'fixme':
        interpreter.fix_me_shell()
    else:
        interpreter.execute(code)

# SSH Support
# INSTALL PARAMIKO
import subprocess
import os

def install_paramiko_lib():
    libs_path = "osnake/libs"
    if not os.path.exists(libs_path):
        os.makedirs(libs_path)
    subprocess.run(["pip", "install", "--target=" + libs_path, "paramiko"])

install_paramiko_lib()

# SSH
import paramiko

class OSnakeInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.ssh_client = None

def ssh_connect(self, credentials):
        try:
            host, user, password = credentials.split()
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=host, username=user, password=password)
            print(f"Connected to {host} as {user}")
        except Exception as e:
            print(f"Error connecting to SSH: {e}")

def ssh_command(self, command):
        try:
            if self.ssh_client is None:
                print("Not connected to any SSH server.")
                return
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        except Exception as e:
            print(f"Error executing SSH command: {e}")

def ssh_disconnect(self):
        if self.ssh_client is not None:
            self.ssh_client.close()
            self.ssh_client = None
            print("Disconnected from SSH server.")

import paramiko
class OSnakeInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.ssh_client = None

    # Other methods follow...


def handle_ssh_command(self, ssh_command):
        subcommands = ssh_command.split()
        if not subcommands:
            print("SSH command missing.")
            return

        command = subcommands[0]
        args = ' '.join(subcommands[1:])

        if command == 'connect':
            self.ssh_connect(args)
        elif command == 'command':
            self.ssh_command(args)
        elif command == 'disconnect':
            self.ssh_disconnect()
        else:
            print(f"Unknown SSH subcommand: {command}")

def ssh_connect(self, credentials):
        try:
            host, user, password = credentials.split()
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=host, username=user, password=password)
            print(f"Connected to {host} as {user}")
        except Exception as e:
            print(f"Error connecting to SSH: {e}")

def ssh_command(self, command):
        try:
            if self.ssh_client is None:
                print("Not connected to any SSH server.")
                return
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        except Exception as e:
            print(f"Error executing SSH command: {e}")

def ssh_disconnect(self):
        if self.ssh_client is not None:
            self.ssh_client.close()
            self.ssh_client = None
            print("Disconnected from SSH server.")

def process_line(self, line):
    if not line:
        return
    if line.startswith('DATA'):
        self.handle_data_section(line)
    elif line.startswith('data'):
        self.handle_data_declaration(line)
    elif line.startswith('print'):
        self.handle_print(line)
    elif line.startswith('if'):
        self.handle_if_statement(line)
    elif line.startswith('func'):
        self.handle_function_declaration(line)
    elif line in self.functions:
        self.execute(self.functions[line])
    elif line.startswith('dir='):
        self.handle_directory(line)
    elif line.startswith('set --filepath'):
        self.setup_directories(line)
    elif line == 'osnakepad':
        self.open_osnakepad()
    elif line.startswith('run'):
        self.run_osnake_file(line)
    elif line.endswith('.osnake'):
        self.run_osnake_file(f'run {line}')
    elif line == 'exit':
        print("Exiting osnake interpreter.")
        exit()
    elif line.startswith('fixme'):
        self.handle_fixme(line.replace('fixme', '').strip())
    elif line.startswith('module.ssh'):
        self.handle_ssh_command(line.replace('module.ssh', '').strip())
    else:
        print(f"Unknown command: {line}")

# BASIC OSNAKE LIBS
import subprocess
import os

def install_libraries():
    libs_path = "osnake/libs"
    if not os.path.exists(libs_path):
        os.makedirs(libs_path)
    libraries = ["requests", "matplotlib", "numpy", "pandas", "beautifulsoup4", "sqlite3", "scikit-learn", "cryptography", "flask", "opencv-python", "beautifultable", "socket"]
    for lib in libraries:
        subprocess.run(["pip", "install", "--target=" + libs_path, lib])

install_libraries()

# oSNAKE runtime with libraries
import sys
import os
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
from sklearn.linear_model import LinearRegression
from cryptography.fernet import Fernet
from flask import Flask, request
import cv2
from beautifultable import BeautifulTable
import socket

# requests
def handle_http_command(self, http_command):
    try:
        command, url = http_command.split()
        if command == 'get':
            response = requests.get(url)
            print(response.text)
        else:
            print(f"Unknown HTTP command: {command}")
    except Exception as e:
        print(f"Error in HTTP command: {e}")

def handle_plot_command(self, plot_command):
    try:
        parts = plot_command.split()
        if parts[0] == 'line':
            x = eval(parts[1])
            y = eval(parts[2])
            plt.plot(x, y)
            plt.show()
        else:
            print(f"Unknown plot command: {parts[0]}")
    except Exception as e:
        print(f"Error in plot command: {e}")

def handle_math_command(self, math_command):
    try:
        command, array = math_command.split(' ', 1)
        if command == 'array':
            array = eval(array)
            np_array = np.array(array)
            print(np_array)
        else:
            print(f"Unknown math command: {command}")
    except Exception as e:
        print(f"Error in math command: {e}")

def handle_dataframe_command(self, dataframe_command):
    try:
        command, file_path = dataframe_command.split()
        if command == 'read_csv':
            df = pd.read_csv(file_path)
            print(df)
        else:
            print(f"Unknown dataframe command: {command}")
    except Exception as e:
        print(f"Error in dataframe command: {e}")

def handle_web_command(self, web_command):
    try:
        command, url = web_command.split()
        if command == 'scrape':
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            print(soup.prettify())
        else:
            print(f"Unknown web command: {command}")
    except Exception as e:
        print(f"Error in web command: {e}")

def handle_database_command(self, database_command):
    try:
        command, db_path = database_command.split()
        if command == 'connect':
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print("Tables in database:", tables)
            conn.close()
        else:
            print(f"Unknown database command: {command}")
    except Exception as e:
        print(f"Error in database command: {e}")

def handle_ml_command(self, ml_command):
    try:
        command, file_path = ml_command.split()
        if command == 'train':
            df = pd.read_csv(file_path)
            X = df.iloc[:, :-1].values
            y = df.iloc[:, -1].values
            model = LinearRegression()
            model.fit(X, y)
            print("Model trained.")
        else:
            print(f"Unknown ML command: {command}")
    except Exception as e:
        print(f"Error in ML command: {e}")

def handle_crypto_command(self, crypto_command):
    try:
        command, data, password = crypto_command.split(' ', 2)
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        if command == 'encrypt':
            encrypted_text = cipher_suite.encrypt(data.encode())
            print(f"Encrypted text: {encrypted_text.decode()}")
        elif command == 'decrypt':
            decrypted_text = cipher_suite.decrypt(data.encode())
            print(f"Decrypted text: {decrypted_text.decode()}")
        else:
            print(f"Unknown crypto command: {command}")
    except Exception as e:
        print(f"Error in crypto command: {e}")

def handle_webapp_command(self, webapp_command):
    try:
        command, port = webapp_command.split()
        if command == 'start_server':
            app = Flask(__name__)
            
            @app.route('/')
            def index():
                return "Hello, this is your web app!"
            
            app.run(port=int(port))
        else:
            print(f"Unknown webapp command: {command}")
    except Exception as e:
        print(f"Error in webapp command: {e}")

def handle_cv_command(self, cv_command):
    try:
        command, file_path = cv_command.split()
        if command == 'detect_faces':
            image = cv2.imread(file_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('img', image)
            cv2.waitKey()
        else:
            print(f"Unknown CV command: {command}")
    except Exception as e:
        print(f"Error in CV command: {e}")

def handle_table_command(self, table_command):
    try:
        command, header, rows = table_command.split(' ', 2)
        if command == 'create':
            header = eval(header)
            rows = eval(rows)
            table = BeautifulTable()
            table.columns.header = header
            for row in rows:
                table.rows.append(row)
            print(table)
        else:
            print(f"Unknown table command: {command}")
    except Exception as e:
        print(f"Error in table command: {e}")

def handle_network_command(self, network_command):
    try:
        command, host, port = network_command.split()
        port = int(port)
        if command == 'create_server':
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"Server listening on {host}:{port}")
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")
            conn.close()
        else:
            print(f"Unknown network command: {command}")
    except Exception as e:
        print(f"Error in network command: {e}")

def process_line(self, line):
    if not line:
        return
    if line.startswith('DATA'):
        self.handle_data_section(line)
    elif line.startswith('data'):
        self.handle_data_declaration(line)
    elif line.startswith('print'):
        self.handle_print(line)
    elif line.startswith('if'):
        self.handle_if_statement(line)
    elif line.startswith('func'):
        self.handle_function_declaration(line)
    elif line in self.functions:
        self.execute(self.functions[line])
    elif line.startswith('dir='):
        self.handle_directory(line)
    elif line.startswith('set --filepath'):
        self.setup_directories(line)
    elif line == 'osnakepad':
        self.open_osnakepad()
    elif line.startswith('run'):
        self.run_osnake_file(line)
    elif line.endswith('.osnake'):
        self.run_osnake_file(f'run {line}')
    elif line == 'exit':
        print("Exiting osnake interpreter.")
        exit()
    elif line.startswith('fixme'):
        self.handle_fixme(line.replace('fixme', '').strip())
    elif line.startswith('module.http'):
        self.handle_http_command(line.replace('module.http', '').strip())
    elif line.startswith('module.plot'):
        self.handle_plot_command(line.replace('module.plot', '').strip())
    elif line.startswith('module.math'):
        self.handle_math_command(line.replace('module.math', '').strip())
    elif line.startswith('module.dataframe'):
        self.handle_dataframe_command(line.replace('module.dataframe', '').strip())
    elif line.startswith('module.web'):
        self.handle_web_command(line.replace('module.web', '').strip())
    elif line.startswith('module.database'):
        self.handle_database_command(line.replace('module.database', '').strip())
    elif line.startswith('module.ml'):
       self.handle_ml_command(line.replace('module.ml', '').strip())


