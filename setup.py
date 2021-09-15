from distutils.core import setup
setup(
  name = 'ossy',         # How you named your package folder (MyLib)
  packages = ['ossy'],   # Chose the same as "name"
  version = '0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Ossy detects "risky" Python PyPi packages in your software supply chain',   # Give a short description about your library
  author = 'Ossillate Inc.',                   # Type in your name
  author_email = 'oss@ossillate.com',      # Type in your E-Mail
  url = 'https://github.com/ossillate-inc/ossy-pypi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ossillate-inc/ossy-pypi/archive/refs/tags/placeholder.tar.gz', # I explain this later on
  keywords = ['software supply chain attacks', 'typo-squatting', 'python', 'open-source software', 'software composition analysis'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 1 - Planning',      # Chose either "1 - Planning, 2 - Pre-Alpha, 3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
