from dbnd._core.configuration import environ_config, get_dbnd_project_config
from dbnd._core.plugin.dbnd_plugins import pm
from dbnd._core.utils.basics.load_python_module import _load_module
from dbnd._core.utils.seven import fix_sys_path_str


_dbnd_plugins_registered = False


def register_dbnd_plugins():
    if get_dbnd_project_config().is_no_modules:
        return

    global _dbnd_plugins_registered
    if _dbnd_plugins_registered:
        return
    _dbnd_plugins_registered = True

    fix_sys_path_str()

    pm.load_setuptools_entrypoints("dbnd")
    pm.check_pending()


def register_dbnd_user_plugins(user_plugin_modules):
    for plugin_module in user_plugin_modules:
        pm.register(_load_module(plugin_module, "plugin:%s" % plugin_module))
