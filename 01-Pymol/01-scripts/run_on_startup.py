# Add paths to sys.path so PyMOL can find modules and scripts
import sys, os
pymol_git = os.path.abspath(os.path.join(os.environ['PYMOL_PATH'], 'Pymol-script-repo'))
os.environ['PYMOL_GIT_MOD'] = os.path.join(pymol_git,'modules')
sys.path.append(pymol_git)
sys.path.append(os.environ['PYMOL_GIT_MOD'])

# Make setting changes to Plugin Manager
import pymol.plugins
pymol.plugins.preferences = {'instantsave': False, 'verbose': False}
pymol.plugins.autoload = {'apbs_tools': False}
pymol.plugins.set_startup_path([os.path.join(pymol_git, 'plugins'), os.path.join(sys.prefix, 'Lib', 'site-packages', 'pmg_tk', 'startup')])
pymol.plugins.preferences = {'instantsave': True, 'verbose': False}