from setuptools import setup

setup(name='nose2complete',
      version='0.1.0',
      description='nose2complete is a plugin used for completing test names from the command line. Heavily inspired by nosecomplete',
      author='Tim Sampson',
      author_email='littlesanga@gmail.com',
      url='https://github.com/sanga/nose2complete',
      license='MIT',
      py_modules=['nose2complete'],
      entry_points={'console_scripts': ['nose2complete=nose2complete:main']})
