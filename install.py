import subprocess

modules = ['simple_term_menu','colorama']

for module in modules:
    try:
        subprocess.check_call(["pip","install",module])
        print(f"Successfully installed {module}.")
    except subprocess.CalledProcessError:
        print(f"Error when installing {module}.")
        
        