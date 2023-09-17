"""config service."""

from typing import Mapping, Any, Dict
from types import ModuleType
from errno import ENOENT, EISDIR, ENOTDIR
from pathlib import Path
from os.path import join


class Config(dict):
    """Class to manage application configurations."""

    def __init__(self, root_path: str | None = None):
        """Config constructor.

        :param root_path: Path to which files are read relative from (Default: None).
        :type root_path: str | None
        """
        super().__init__()
        self.root_path = root_path if root_path else Path().resolve()

    def from_dict(self, obj: object) -> None:
        """Updates the values from the given object.

        :param obj: Object to import.
        :type obj: object
        """
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)

    def from_pyfile(self, filename: str, silent: bool = False) -> bool:
        """Updates the values from the given python file.

        :param filename: The filename of the config.
        :type filename: str
        :param silent: Set to True if you want silent failure for missing file.
        :type silent: bool
        :return: True if the file was loaded successfully.
        :rtype: bool
        """
        filename = join(self.root_path, filename)
        module = ModuleType('config')
        module.__file__ = filename
        try:
            with open(filename, mode='rb') as config_file:
                exec(compile(config_file.read(), filename, 'exec'), module.__dict__)  # pylint: disable=exec-used
        except OSError as ex:
            if silent and ex.errno in (ENOENT, EISDIR, ENOTDIR):
                return False
            ex.strerror = f'Unable to load configuration file ({ex.strerror})'
            raise
        self.from_dict(module)
        return True

    def from_mapping(self, mapping: Mapping[str, Any] | None = None, **kwargs: Any):
        """Updates the config like :meth:`update` ignoring items with non-upper keys.

        :param mapping: Mapping to import (Default: None).
        :type mapping: Mapping[str, Any] | None
        :param kwargs: kwargs
        :type kwargs: Any
        """
        mappings: Dict[str, Any] = {}
        if mapping is not None:
            mappings.update(mapping)
        mappings.update(kwargs)
        for key, value in mappings.items():
            if key.isupper():
                self[key] = value
