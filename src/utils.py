import toml
import pickle

def read_toml_config(path: str) -> dict:
  """
  Reading a TOML config file
  
  Args:
    path (str): Location of the config file
    
  Returns:
    dictionary: Config file as a dictionary
  """
  return toml.load(path)


def dump_pickle(obj, filename: str) -> None:
    """Save object as pickle file.

    Args:
        obj (object): The object to be saved
        filename (str): The filename of the pickle file to be saved
    """
    with open(filename, "wb") as f_out:
        return pickle.dump(obj, f_out)


def load_pickle(filename: str) -> None:
    """Load a pickle file.

    Args:
        filename (str): The path of the pickle file to be loaded
    """
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)