def read_toml_config(path):
  """
  Reading a TOML config file
  
  Args:
    path (str): Location of the config file
    
  Returns:
    dictionary: Config file as a dictionary
  """
  return toml.load(path)