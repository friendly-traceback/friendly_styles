from setuptools import setup, find_packages


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='friendly_styles',
    version='0.0.3',
    description='Pygments styles designed for friendly/friendly-traceback',
    long_description=read('README.md'),
    license='MIT',

    author='André Roberge',
    author_email='andre.roberge@gmail.com',

    url='https://github.com/friendly-traceback/friendly_styles',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],

    entry_points={
        "pygments.styles": [
            "friendly_light = styles.friendly_light:FriendlyLightStyle",
            "friendly_dark = styles.friendly_dark:FriendlyDarkStyle",
        ]
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

