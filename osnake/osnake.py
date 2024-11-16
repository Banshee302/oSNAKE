import os

class OSnakeInterpreter:
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

# Main loop
interpreter = OSnakeInterpreter()
print("osnake interpreter. Type 'osnakepad' to edit scripts, 'run <filename>' to execute .osnake files, 'set --filepath <path>' to set up directories, 'exit' to quit.")
while True:
    code = input('> ')
    interpreter.execute(code)
