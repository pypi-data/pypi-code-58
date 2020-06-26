# package modules
from .event import event, event_obj
from .state import state, like
from .dummy import miniflask_dummy
from .util import getModulesAvail
from .util import highlight_error, highlight_name, highlight_module, highlight_loading, highlight_loading_default, highlight_loaded_none, highlight_loaded, highlight_event, highlight_blue_line, highlight_type, highlight_val, highlight_val_overwrite, str2bool


from .modules import registerPredefined
from .modules.settings import listsettings

# global modules
import sys
from os import path, listdir, linesep
from colored import fg, bg, attr
from importlib import import_module
from copy import copy
from argparse import ArgumentParser, SUPPRESS as argparse_SUPPRESS
from queue import Queue
import re

def print_info(*args,color=fg('green'),msg="INFO"):
    print(color+attr('bold')+msg+attr('reset')+color+": "+attr('reset'),*args,attr('reset'))

# ================ #
# MiniFlask Kernel #
# ================ #

class miniflask():
    def __init__(self, module_dirs):
        if not module_dirs:
            return

        # module dir to be read from
        if isinstance(module_dirs,list):
            self.module_dirs = {path.basename(m):m for m in module_dirs}
        elif isinstance(module_dirs,str):
            self.module_dirs = {path.basename(module_dirs):module_dirs}
        elif isinstance(module_dirs,dict):
            self.module_dirs = module_dirs
        else:
            raise ValueError("Only dict or list allowed for `module_dirs'. Found type '%s'." % type(module_dirs))
        for dir in self.module_dirs.values():
            sys.path.insert(0,dir+path.sep+path.pardir)

        # arguments from cli-stdin
        self.settings_parser = ArgumentParser(usage=sys.argv[0]+" modulelist [optional arguments]")
        self.settings_parse_later = {}
        self.settings_parse_later_overwrites = {}
        self.settings_parser_required_arguments = []
        self.default_modules = []

        # internal
        self.halt_parse = False
        self.event_objs = {}
        self.event = event(self, optional=False)
        self.event.optional = event(self, optional=True)
        self.state = {}
        self.state_default = {}
        self.modules_loaded = {}
        self.modules_avail = getModulesAvail(self.module_dirs)
        self.miniflask_objs = {} # local modified versions of miniflask
        registerPredefined(self.modules_avail)



    # ==================== #
    # module introspection #
    # ==================== #

    # module event
    def getModuleEvents(self, module, dummy=None):
        if not dummy:
            dummy = miniflask_dummy()

        # load module
        mod = import_module(self.modules_avail[module]["id"])
        if not hasattr(mod,"register"):
            return []

        mod.register(dummy)
        return dummy.getEvents()

    # pretty print of all available modules
    def showModules(self, dir=None, prepend="", id_pre=None, with_event=True):
        if not dir:
            for basename, dir in self.module_dirs.items():
                self.showModules(dir, prepend=prepend, id_pre=basename if id_pre is None else id_pre+"."+basename, with_event=with_event)
            return

        if id_pre is None:
            id_pre = path.basename(dir)
        if len(prepend) == 0:
            print()
            print(highlight_name(path.basename(id_pre)))
        dirs = [d for d in listdir(dir) if path.isdir(path.join(dir,d)) and not d.startswith("_")]
        for i, d in enumerate(dirs):
            if d.startswith("."):
                continue
            if path.exists(path.join(dir,d,".ignoredir")):
                continue
            module_id = id_pre + "." + d if id_pre != "" else d

            is_module = path.exists(path.join(dir,d,".module"))
            is_lowpriority_module = path.exists(path.join(dir,d,".lowpriority"))
            if is_module:
                shortestid = self.getModuleShortId(module_id)
            has_shortid = is_module and shortestid == d

            if i == len(dirs)-1:
                tree_symb = "└── "
                is_last = True
            else:
                tree_symb = "├── "
                is_last = False
            append = " "+fg('blue')+"("+shortestid+")"+attr('reset') if is_module and not has_shortid else ""
            append += attr('dim')+" (low-priority module)"+attr('reset') if is_lowpriority_module else ""
            print(prepend+tree_symb+(highlight_name(d) if is_module else d)+append)

            tree_symb_next = "     " if is_last else "│    "
            if is_module:
                if with_event:
                    events = self.getModuleEvents(module_id)
                    if len(events) > 0:
                        for e in events:
                            unique_flag = "!" if e[1] else ">"
                            print(prepend+tree_symb_next+unique_flag+" "+highlight_event(e[0]))
                continue
            self.showModules(path.join(dir,d),prepend=prepend+tree_symb_next, id_pre=module_id, with_event=with_event)

    # pretty print loaded modules
    def __str__(self):
        if len(self.modules_loaded) == 0:
            return highlight_loaded_none("No Loaded Modules")
        return highlight_loaded("Loaded Modules:", self.modules_loaded.keys())


    # =================== #
    # module registration #
    # =================== #

    # get unique id of a moodule
    def getModuleId(self, module_id):
        module_ids = self.modules_avail.keys()
        module = module_id.replace(".","\.(.*\.)*")

        # first search for a default module
        r = re.compile("^(.*\.)?%s(\..*)?\.(default|%s)$" % (module, module_id.split(".")[-1]))
        found_modules = list(filter(r.match, module_ids))

        # if no default module found, check for direct identifier
        if len(found_modules) == 0:
            r = re.compile("^(.*\.)?%s$" % module)
            found_modules = list(filter(r.match, module_ids))

        # if no default module found, check for related identifier
        if len(found_modules) == 0:
            r = re.compile("^(.*\.)?%s(\..*)?$" % module)
            found_modules = list(filter(r.match, module_ids))

        # if more than one module found, exclude all low-priority modules
        if len(found_modules) > 1:
            found_modules = list(filter(lambda mid: not self.modules_avail[mid]["lowpriority"], found_modules))

        # if more than one module found let the user know
        if len(found_modules) > 1:
            raise ValueError(highlight_error()+"Module-Identifier '%s' is not unique. Found %i modules:\n\t%s" % (highlight_module(module_id), len(found_modules), "\n\t".join(found_modules)))

        # no module found with both variants
        elif len(found_modules) == 0:
            raise ValueError(highlight_error()+"Module '%s' not known." % highlight_module(module_id))

        # module_id is a unique identifier
        module = found_modules[0]
        return self.modules_avail[module]["id"]

    # get short id of a moodule
    def getModuleShortId(self, module):
        if not module in self.modules_avail:
            raise ValueError(highlight_error()+"Module '%s' not known." % highlight_module(module))
        uniqueId = self.modules_avail[module]["id"].split(".")

        # modA.default -> modA
        if uniqueId[-1] == "default":
            uniqueId = uniqueId[:-1]

        # find the shortest substring to match a module uniquely
        for i in range(len(uniqueId)-1,0,-1):
            shortid = ".".join(uniqueId[i:])
            try:
                if module == self.getModuleId(shortid):
                    return shortid
                else:
                    pass
            except ValueError as e:
                pass
        return None

    # maps 'folder.subfolder.module.list.of.vars' to 'folder.subfoldder.module'
    def _getModuleIdFromVarId(self, varid, varid_list, scope=None):

        # try to use scope.default as module id
        try:
            module_id = self.getModuleId(scope+".default")
            if varid.startswith(scope):
                varid = varid[len(scope)+1:]
            return module_id, varid
        except ValueError as e:
            pass

        # try to use scope as module id
        try:
            module_id = self.getModuleId(scope)
            if varid.startswith(scope):
                varid = varid[len(scope)+1:]
            return module_id, varid
        except ValueError as e:
            pass

        # no we have to work out which module may be meant
        for i in range(len(varid_list)-1,0,-1):
            test_id = ".".join(varid_list[:i])
            try:
                return self.getModuleId(test_id), ".".join(varid_list[i:])
            except ValueError as e:
                pass

        # no id could be derived
        return None, ".".join(varid_list)

    # loads module (once)
    def load(self, module_name, verbose=True, auto_query=True, loading_text=highlight_loading):

        # load list of modules
        if isinstance(module_name,list):
            for m in module_name:
                self.load(m)
            return

        # get id
        if auto_query:
            module_name = self.getModuleId(module_name)
        elif not module_name in self.modules_avail:
            raise ValueError(highlight_error()+"Module '%s' not known." % highlight_module(module_name))

        # check if already loaded
        if module_name in self.modules_loaded:
            return

        # loading message
        prepend = self._loadprepend if hasattr(self,'_loadprepend') else ""
        print(prepend+loading_text(module_name))

        # load module
        mod = import_module(self.modules_avail[module_name]["importpath"])
        if not hasattr(mod,"register"):
            raise ValueError(highlight_error()+"Module '%s' does not register itself." % module_name)

        # remember loaded modules
        self.modules_loaded[module_name] = mod

        # register events
        mod.miniflask_obj = miniflask_wrapper(module_name, self)
        mod.miniflask_obj._loadprepend = prepend + "  ├── "
        mod.register(mod.miniflask_obj)

    # register default module that is loaded if none of glob is matched
    def register_default_module(self, glob, module):
        self.default_modules.append((glob, module))

    # saves function to a given (event-)name
    def register_event(self,name,fn,unique=False):

        # check if is unique event. if yes, check if event already registered
        if name in self.event_objs and (unique or self.event_objs[name].unique):
            eobj = self.event_objs[name].modules if not self.event_objs[name].unique else [self.event_objs[name].modules]
            raise ValueError(highlight_error()+"Event '%s' is unique, and thus, cannot be imported twice.\n\t(Imported by %s)" % (highlight_event(name),", ".join(["'"+highlight_module(e.module_name)+"'" for e in eobj])))

        # register event
        if name in self.event_objs:
            self.event_objs[name].fn.append(fn)
            self.event_objs[name].modules.append(self)
        else:
            self.event_objs[name] = event_obj(fn, unique, self)

    # overwrite state defaults
    # Note: the problem lies in the fact that the true id of a variable is defined as scope.key,
    #       however scope can be empty if key is meant as a reference in the global scope=="".
    #       Otherwise, this function would be a lot simpler.
    def register_defaults(self, defaults, scope="", overwrite=False, cliargs=True, parsefn=True):
        if scope is None:
            scope = ""

        for key, val in defaults.items():

            # unique & full varname is fully defined using scope
            varname = scope+"."+key if len(scope) > 0 else key
            key_split = varname.split(".")

            # short name is only given iff corresponding module has a unique short id
            varname_short = None

            # get module id from global varname identifier
            module_id, key = self._getModuleIdFromVarId(varname,key_split,scope=scope)
            if module_id is not None:

                # retrieve real local key name
                module_short_id = self.getModuleShortId(module_id)
                if module_short_id is not None:
                    varname_short = module_short_id+"."+key

                # recreate actual key
                module_id = self.getModuleId(module_id)
                varname = module_id + "." + key

            # ignore if short varname is varname
            if varname_short == varname:
                varname_short = None

            # pre-initialize variable for possible lambda expressions in second pass
            if hasattr(self.state,"all"):
                self.state.all[varname] = val
            else:
                self.state[varname] = val

            # actual initialization is done when all modules has been parsed
            if overwrite:
                self.settings_parse_later_overwrites[varname] = (varname_short, val, cliargs, parsefn)
            else:
                self.settings_parse_later[varname] = (varname_short, val, cliargs, parsefn)

    def _settings_parser_add(self, varname, varname_short, val, nargs=None, default=None):

        # lists are just multiple arguments
        if isinstance(val,list):
            self._settings_parser_add(varname, varname_short, val[0], nargs="+", default=val)
            return

        # get argument type from value (this an be int, but also 42 for instance)
        if type(val) == type:
            argtype = val if val != bool else str2bool
        else:
            argtype = type(val) if type(val) != bool else str2bool
        kwarg_long  = {'dest': varname, 'type': argtype, 'nargs': nargs}
        kwarg_short = {'dest': varname, 'type': argtype, 'nargs': nargs, 'help': argparse_SUPPRESS}

        # we know the default argument, if the value is given
        # otherwise the value is a required argument (to be tested later)
        if type(val) != type:
            kwarg_long["default"] = kwarg_short["default"] = default if default is not None else val
        else:
            if varname_short:
                self.settings_parser_required_arguments.append([varname,varname_short])
            else:
                self.settings_parser_required_arguments.append([varname])

        # for bool: enable --varname as alternative for --varname true
        if argtype == str2bool and nargs != '+':
            kwarg_long["nargs"]  = kwarg_short["nargs"] = '?'
            kwarg_long["const"]  = kwarg_short["const"] = True

        # define the actual arguments
        if argtype in [int,str,float,str2bool]:
            self.settings_parser.add_argument( "--"+varname, **kwarg_long)
            if varname_short:
                self.settings_parser.add_argument( "--"+varname_short, **kwarg_short)
        else:
            raise ValueError("Type '%s' not supported. (Used for setting '%s')" % (type(val), varname))

        # for bool: enable --no-varname as alternative for --varname false
        # Note: this has to be defined AFTER --varname
        if argtype == str2bool and nargs != '+':
            self.settings_parser.add_argument('--no-'+varname, dest=varname, action='store_false')
            if varname_short:
                self.settings_parser.add_argument('--no-'+varname_short, dest=varname, action='store_false', help=argparse_SUPPRESS)

    # ======= #
    # runtime #
    # ======= #
    def stop_parse(self):
        self.halt_parse = True

    def parse_args(self, argv=None, optional=True):
        self.halt_parse = False

        if not argv:
            argv = sys.argv#[1:]
        else:
            argv = [None]+argv

        parser = ArgumentParser()
        parser.add_argument('cmds', default='info', nargs=1 if not optional else "?")
        args = parser.parse_args(argv[1:2])

        # load modules
        if args.cmds:
            if optional:
                cmds = args.cmds.split(',')
            else:
                cmds = args.cmds[0].split(',')
            for cmd in cmds:
                if self.halt_parse:
                    break

                # try:
                self.load(cmd)
                # except Exception as e:
                #     print(e)

        # ensure default_modules are loaded
        keys = self.modules_loaded.keys()
        for glob, module in self.default_modules:
            found = [x for x in keys if re.search(glob, x)]
            if len(found) == 0:
                self.load(module, loading_text=lambda x: highlight_loading_default(glob,x))

        # add variables to argparse and remember defaults
        for settings in [self.settings_parse_later,self.settings_parse_later_overwrites]:
            overwrite = settings == self.settings_parse_later_overwrites 
            for varname, (varname_short, val, cliargs, parsefn) in settings.items():

                # check if exists
                if overwrite and varname not in self.settings_parse_later:
                    raise ValueError("Variable '%s' is not registered yet, however it seems like you wold like to overwrite it." % varname)

                # eval dependencies/like expressions
                if callable(val) and type(val) != type and parsefn:
                    try:
                        the_val = val
                        while callable(the_val) and type(the_val) != type:
                            the_val = the_val(self.state,self.event)
                    except RecursionError as e:
                        raise RecursionError("In parsing of value '%s'." % varname)
                else:
                    the_val = val

                if cliargs:

                    # add to argument parser
                    # Note: the the last value (an overwrite-variable) should be the one that generates the argparser)
                    if overwrite or varname not in self.settings_parse_later_overwrites:
                        self._settings_parser_add(varname, varname_short, the_val)

                    # remember default state
                    if isinstance(val,like):
                        val.default = the_val
                        self.state_default[varname] = val
                    else:
                        self.state_default[varname] = the_val

        # add help message
        self.settings_parser.print_help = lambda: (print("usage: modulelist [optional arguments]"),print(),print("optional arguments (and their defaults):"),print(listsettings(state("",self.state,self.state_default),self.event)))

        # parse user overwrites (first time, s.t. lambdas change adaptively)
        settings_args = self.settings_parser.parse_args(argv[2:])
        for varname, val in vars(settings_args).items():
            self.state[varname] = val

        # check if required arguments are given by now
        missing_arguments = []
        for variables  in self.settings_parser_required_arguments:
            if self.state[variables[0]] is None:
                missing_arguments.append(variables)
        if len(missing_arguments) > 0:
            self.settings_parser.error(linesep+linesep.join(["The following argument is required: "+" or ".join(["--"+arg for arg in reversed(args)]) for args in missing_arguments]))

        # finally parse lambda-dependencies
        for varname, (varname_short, val, cliargs, parsefn) in self.settings_parse_later.items():
            # Note: if current state equals state_default it has not been overwritten by user, thus lambda can be evaluated again
            # Three cases exist in wich lambda expression shall be recalculated:
            # The value is a function AND one of
            # 1. was helper variable, thus no cli-argument can overwrite it anyway
            # 2. the value has not been overwritten by user and the value is a normal lambda/function
            # 3. the value has not been overwritten by user and the value is a like expression
            while callable(val) and type(val) != type and parsefn and (not cliargs or self.state[varname] == self.state_default[varname] or (isinstance(self.state_default[varname], like) and self.state[varname] == self.state_default[varname].default)):
                val = val(self.state,self.event)
                self.state[varname] = val

        print(highlight_blue_line("-"*50))

    def run(self, call="main"):
        # check if all requested modules are loaded
        if not self.halt_parse:

            # optional init event
            self.event.optional.init()

            # call event if exists
            if hasattr(self.event, call):
                getattr(self.event, call)()
            else:
                print("No event '{0}' registered. "
                      "Please make sure to register the event '{0}', "
                      "or provide a suitable event to call.".format(call))


relative_import_re = re.compile("(\.+)(.*)")
class miniflask_wrapper(miniflask):
    def __init__(self, module_name, mf):
        self.module_id = module_name
        self.module_name = module_name.split(".")[-1]
        self.module_base = module_name.split(".")[0]
        self.wrapped_class = mf.wrapped_class if hasattr(mf, 'wrapped_class') else mf
        self.state = state(module_name, self.wrapped_class.state, self.wrapped_class.state_default)

    def _get_relative_module_id(self, module_name, offset=0):
        was_relative = False
        m = relative_import_re.match(module_name)
        if m is not None:
            upmodule = len(m[1])
            relative_module = m[2]
            if upmodule == offset:
                module_name = self.module_id + ("." + relative_module if relative_module else "")
            else:
                module_name = ".".join(self.module_id.split(".")[:-upmodule+offset]) + ("." + relative_module if relative_module else "")
            was_relative = True
        return module_name, was_relative

    def __getattr__(self,attr):
        orig_attr = super().__getattribute__('wrapped_class').__getattribute__(attr)
        if callable(orig_attr):
            def hooked(*args, **kwargs):
                result = orig_attr(*args, **kwargs)
                # prevent wrapped_class from becoming unwrapped
                if result == self.wrapped_class:
                    return self
                return result
            return hooked
        else:
            return orig_attr

    def redefine_scope(self,new_module_name):
        old_module_name = self.module_id
        new_module_name = self.set_scope(new_module_name)
        if new_module_name in self.modules_avail:
            raise ValueError("Scope `%s` already used. Cannot define multiple modules using `redefine_scope`. Did you maybe mean to use `set_scope`?" % new_module_name)
        m = self.modules_avail[old_module_name]
        del self.modules_avail[old_module_name]
        m["id"] = new_module_name
        self.modules_avail[new_module_name] = m

    def set_scope(self,new_module_name):
        new_module_name, was_relative = self._get_relative_module_id(new_module_name)
        if not was_relative:
            new_module_name = self.module_base + "." + new_module_name
        self.module_id = new_module_name
        self.state.module_id = new_module_name
        return new_module_name

    # like with relative imports
    def like(self, varname, alt, scope="."):
        scope_name = scope
        if scope is not None:
            scope, was_relative = self._get_relative_module_id(scope)
        return like(varname, alt, scope=scope, scope_name=scope_name)

    # enables relative imports
    def load(self, module_name, auto_query=True, **kwargs):

        # if list given, iterate over list
        if isinstance(module_name, list):
            for mname in module_name:
                self.load(mname, auto_query=auto_query, **kwargs)
            return

        # parse relative imports first
        module_name, was_relative = self._get_relative_module_id(module_name)
        auto_query = not was_relative

        # call load (but ensure no querying is made if relative imports were given)
        super().load(module_name, auto_query=auto_query, **kwargs)

    # overwrite state defaults
    def register_defaults(self, defaults, scope=None, **kwargs):
        # default behaviour is to use current module-name
        if scope is None:
            scope = self.module_id
        scope, was_relative = self._get_relative_module_id(scope, offset=1)
        super().register_defaults(defaults, scope=scope, **kwargs)

    # helper variables are not added to argument parser
    def register_helpers(self, defaults, **kwargs):
        self.register_defaults(defaults, cliargs=False, **kwargs)

    # does not add scope of module
    def register_globals(self, defaults, **kwargs):
        self.register_defaults(defaults, scope="", **kwargs)

    # overwrites previously registered variables
    def overwrite_globals(self, defaults, scope="", **kwargs):
        self.register_defaults(defaults, scope=scope, overwrite=True, **kwargs)

    # overwrites previously registered variables
    def overwrite_defaults(self, defaults, scope=None, **kwargs):
        self.register_defaults(defaults, scope=scope, overwrite=True, **kwargs)

