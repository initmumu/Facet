import os
from konlpy import utils


javadir = '%s%sjava' % (utils.installpath, os.sep)
args = [javadir, os.sep]
folder_suffix = ['{0}{1}open-korean-text-2.1.0.jar']
classpath = [f.format(*args) for f in folder_suffix]

print('javadir  : {}'.format(javadir))
print('os.sep   : {}'.format(os.sep))
print('classpath: {}'.format(classpath[0]))


print('jvmpath: ', jvmpath)