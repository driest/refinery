from .. import refinery, TestBase, NameUnknownException

__all__ = ['refinery', 'TestUnitBase', 'NameUnknownException']


class TestUnitBase(TestBase):

    def _relative_module_path(self, path, strip_test=True):
        path = path.split('.')
        path = path[1:]
        if strip_test:
            path = [x[4:].lstrip('_-.') if x.startswith('test') else x for x in path]
        return '.'.join(path)

    def load(self, *args, **kwargs):
        name = self._relative_module_path(self.__class__.__module__)
        try:
            entry = getattr(refinery, name)
        except AttributeError:
            from refinery.lib.loader import get_all_entry_points
            for entry in get_all_entry_points():
                if entry.__name__ == name:
                    break
                if self._relative_module_path(entry.__module__) == name:
                    break
            else:
                raise NameUnknownException(name)
        return entry(*args, **kwargs)
