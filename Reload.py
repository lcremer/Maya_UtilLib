import sys, types

def gReloadModule(inModule):
    """Reload the given module and all children"""

    # Get a reference to each loaded module
    loaded_modules = dict([
                              (key, value) for key, value in sys.modules.items()
                              if key.startswith(inModule.__name__) and isinstance(value, types.ModuleType)])

    # Delete references to these loaded modules from sys.modules
    for key in loaded_modules:
        del sys.modules[key]

    # Load each of the modules again
    # Make old modules share state with new modules
    for key in loaded_modules:
        # print 're-loading %s' % key
        newmodule = __import__(key)
        oldmodule = loaded_modules[key]
        oldmodule.__dict__.clear()
        oldmodule.__dict__.update(newmodule.__dict__)

def all():
    gReloadModule()

    try:
        print('Reloading Maya_Rigging Module')
        Maya_UtilLib.Reload.gReloadModule(Maya_Rigging)
    except:
        pass

    try:
        print('Reloading Maya_VertexColor Module')
        Maya_UtilLib.Reload.gReloadModule(Maya_VertexColor)
    except:
        pass

    Maya_UtilLib.MainMenu.Create()