from pybuilder.core import use_plugin,init

use_plugin("python.core")
use_plugin("python.unittest")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on('mockito')

