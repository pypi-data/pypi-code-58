# Copyright 2019 Georges Racinet <georges.racinet@octobus.net>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.
"""
Server side Heptapod extension.

This extension should enclose all Mercurial modifications and commands
needed for Heptapod server operations.
"""
import json
from mercurial.i18n import _
from mercurial import (
    cmdutil,
    demandimport,
    error,
    exthelper,
    extensions,
    pycompat,
    registrar,
    scmutil,
    ui as uimod,
    util,
)
import sys

from . import (
    topic as topicmod,
    git,
    obsutil,
)

# these have conditional imports and subsequent `None` testing in
# (urllib3 and/or requests). In other words, hgdemandimport breaks `requests`
demandimport.IGNORES.update([b'brotli', b'simplejson'])

eh = exthelper.exthelper()

if util.safehasattr(registrar, 'configitem'):

    configtable = {}
    configitem = registrar.configitem(configtable)
    configitem(b'heptapod', b'repositories-root')
    configitem(b'heptapod', b'gitlab-shell')
    configitem(b'heptapod', b'mirror-path')

    # The following items affect other config items recognized by the core
    # or by extensions. The default value should be inert, i.e., would not
    # change anything, in particular would not revert to Heptapod defaults
    # (as in `required.hgrc`) what local configuration or command-line options
    # say.
    configitem(b'heptapod', b'initial-import', False)
    configitem(b'heptapod', b'allow-multiple-heads')
    configitem(b'heptapod', b'allow-bookmarks')


cmdtable = {}
command = registrar.command(cmdtable)


def uipopulate(ui):
    if ui.configbool(b'heptapod', b'initial-import'):
        ui.note(b'hgext3rd.heptapod',
                b"setting config options for initial import")
        ui.setconfig(b'experimental',
                     b'single-head-per-branch', False)
        ui.setconfig(b'experimental',
                     b'topic.publish-bare-branch', False)
        ui.setconfig(b'experimental',
                     b'hg-git.bookmarks-on-named-branches', True)
        ui.setconfig(b'experimental', b'hg-git.accept-slash-in-topic-name',
                     True)
        ui.setconfig(b'hggit', b'heptapod.initial-import', True)

    if ui.configbool(b'heptapod', b'allow-multiple-heads'):
        ui.setconfig(b'experimental', b'single-head-per-branch', False)

    if ui.configbool(b'heptapod', b'allow-bookmarks'):
        ui.setconfig(b'experimental', b'single-head-per-branch', False)
        ui.setconfig(b'experimental',
                     b'hg-git.bookmarks-on-named-branches', True)

    auto_publish = ui.config(b'heptapod', b'auto-publish')
    if auto_publish is not None:
        auto_publish = auto_publish.lower()
    if auto_publish == b'nothing':
        ui.setconfig(b'experimental', b'topic.publish-bare-branch', False)
    elif auto_publish == b'all':
        ui.setconfig(b'phases', b'publish', True)


@command(
    b"pull-force-topic",
    [(b'f', b'force', None,
      _(b'run even when remote repository is unrelated')),
     (b'r', b'rev', [], _(b'a remote changeset intended to be imported'),
      _(b'REV')),
     ] + cmdutil.remoteopts,
    _(b'[-r] [-f] TARGET_TOPIC')
)
def pull_force_topic(ui, repo, topic, source=b"default",
                     force=False, **opts):
    """Pull changesets from remote, forcing them to drafts with given topic.

    This is intended to import pull requests from an external system, such
    as Bitbucket. In many case, the changesets to import would have been
    made in a private fork, and could be public, most commonly shadowing the
    default branch.

    TARGET_TOPIC is the topic to set on the pulled changesets
    """
    pull_rev = opts.get('rev')
    logged_revs = b'' if pull_rev is None else b' [%s]' % b', '.join(pull_rev)
    ui.status(b"Pulling%s from '%s', forcing new changesets to drafts with "
              b"topic %s\n" % (logged_revs, source, topic))
    topic = topic.strip()
    if not topic:
        raise error.Abort(
            _(b"topic name cannot consist entirely of whitespace"))
    scmutil.checknewlabel(repo, topic, b'topic')
    return topicmod.pull_force(ui, repo, source, pull_rev, topic,
                               force=force, **opts)


@command(b'gitlab-mirror')
def gitlab_mirror(ui, repo):
    """Export changesets as Git commits in the GitLab repository."""
    git.HeptapodGitHandler(repo, repo.ui).export_commits()


@command(b'hpd-unique-successor',
         [(b'r', b'rev', b'', _(b'specified revision'), _(b'REV')),
          ])
def unique_successor(ui, repo, rev=None, **opts):
    """Display the node ID of the obsolescence successor of REV if unique.

    This can be useful after a simple rebase or fold, as a direct way to
    find the resulting changeset.

    If REV isn't obsolete, the output is REV.
    If there is any divergence, the command will fail.

    The same functionality can be accomplished with
    ``hg log -T {successorsets}`` but the latter

    1. won't fail on divergence
    2. will present as with ``{rev}:{node|short}``, making a second ``hg log``
       call necessary to get the full hash.

    In the context of the Rails app 1) could be almost acceptable by
    detecting multiple results and refusing them (that's already some parsing),
    but together with 2) that's too much, we'll have a
    better robustness with this simple, fully tested command.

    See also: https://foss.heptapod.net/mercurial/evolve/issues/13
    """
    if not rev:
        raise error.Abort(_(b"Please specify a revision"))
    # rev would typically be an obsolete revision, we need to see them
    ctx = scmutil.revsingle(repo.unfiltered(), rev)
    succ_ctx = obsutil.latest_unique_successor(ctx)
    ui.write(succ_ctx.hex())


@command(b'hpd-versions',
         [],
         norepo=True,
         intents={registrar.INTENT_READONLY},
         )
def versions(ui):
    """Output most relevant version information as JSON.

    The provided versions are those we deemed to be of interest for
    the Rails application:
    Python, Mercurial, important extensions.
    """
    py_tuple = tuple(sys.version_info)[:3]
    sysstr = pycompat.sysstr
    versions = dict(python='.'.join(str(i) for i in py_tuple),
                    mercurial=sysstr(util.version()),
                    )
    all_exts = {sysstr(name): sysstr(extensions.moduleversion(module))
                for name, module in extensions.extensions()}
    for ext in ('evolve', 'topic', 'hggit'):
        versions[ext] = all_exts.get(ext)
    ui.write(pycompat.sysbytes(json.dumps(versions)))


def runsystem(orig, ui, cmd, environ, cwd, out):
    heptapod_env = {k: v for k, v in ui.environ.items()
                    if k.startswith(b'HEPTAPOD_')}
    if environ is None:
        environ = heptapod_env
    else:
        heptapod_env.update(environ)
    return orig(ui, cmd, environ=heptapod_env, cwd=cwd, out=out)


extensions.wrapfunction(uimod.ui, b'_runsystem', runsystem)
