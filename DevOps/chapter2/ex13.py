import os

def find_rc(rc_name=".examplerc"):
    
    # проверка переменной среды
    var_name = "EXAMPLE_DIR"
    if var_name in os.environ:
        var_path = os.path.join(f"${var_name}",rc_name)
        config_path = os.path.expandvars(var_path)
        print(f"Checking {config_path}")
        if os.path.exists(config_path):
            return config_path

    # ищем в рабочем каталоге
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path
    
    # поиск в домашнем каталоге
    home_dir = os.path.expanduser("~")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path
    
    # поиск в исполняймом каталоге
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path
    
    print(f"File {rc_name} не найден")

find_rc()