from os import walk, path, linesep
from colored import attr, fg

# get modules in a directory
def getModulesAvail(module_dirs, f={}):
    for base_module_name, dir in module_dirs.items():
        basename_dir = path.basename(dir)
        for (dirpath, dirnames, filenames) in walk(dir):
            module_name_id = base_module_name+"."+dirpath[len(dir)+1:].replace(path.sep,".")
            import_path = basename_dir+"."+dirpath[len(dir)+1:].replace(path.sep,".")

            # empty module id is not allowed
            if len(module_name_id) == 0:
                continue

            # ignore sub directories
            if path.exists(path.join(dirpath,".ignoredir")) or path.basename(dirpath).startswith("."):
                dirnames[:] = []
                continue

            # ignore no real moules
            if ".module" not in filenames:
                continue

            # module found
            f[module_name_id] = {
                'id': module_name_id,
                'lowpriority': path.exists(path.join(dirpath,".lowpriority")),
                'importpath': import_path
            }
    return f

# coloring
highlight_error = lambda: fg('red')+attr('bold')+"Error:"+attr('reset')+" "
highlight_name = lambda x: fg('blue')+attr('bold')+x+attr('reset')
highlight_module = lambda x: fg('green')+attr('bold')+x+attr('reset')
highlight_loading = lambda x: "Load Module ... "+highlight_module(x)
highlight_loading_default = lambda y,x: "Load Default Module ... "+highlight_module(x)+" (for regex "+attr('dim')+y+attr('reset')+")"
highlight_loaded_none = lambda x: fg('red')+x+attr('reset')
highlight_loaded = lambda x, y: attr('underlined')+x+attr('reset')+" "+fg('green')+attr('bold')+", ".join(y)+attr('reset')
highlight_event = lambda x: fg('light_yellow')+x+attr('reset')
highlight_blue_line = lambda x: fg('blue')+attr('bold')+x+attr('reset')
highlight_type = lambda x: fg('cyan')+x+attr('reset')
highlight_val = lambda x: fg('white')+x+attr('reset')
highlight_val_overwrite = lambda x: fg('red')+attr('bold')+x+attr('reset')


import argparse
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
