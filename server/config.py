from configparser import ConfigParser

def resolve_db_config(filename, section):
    parser = ConfigParser()
    parser.read(filename)
    db_config = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]

    else:
        raise Exception(f'Section {section} not found in {filename} file')
    
    return db_config
