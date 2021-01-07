# -*- coding: utf-8 -*-

name = 'ocio'

version = '1.1.1-ta.1.1.0'

authors = [
    'benjamin.skinner',
]

requires = [
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-6']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    ['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.OCIO_VERSION.set(split_versions[0])
    env.OCIO_PACKAGE_VERSION.set(split_versions[1])

    env.OCIO_ROOT.set("{root}")
    env.OCIO_LOCATION.set("{root}")


    env.OCIO_INCLUDE_DIR.set("{root}/include")
    env.OCIO_LIBRARY_DIR.set("{root}/lib")
    env.OCIO_BINARY_DIR.set("{root}/bin")

    import sys
    if 'win' not in str(sys.platform):
        env.LD_LIBRARY_PATH.append( '{root}/lib64' )

    env.PATH.append( str(env.OCIO_BINARY_DIR) )
