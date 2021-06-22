import pathlib
from setuptools import setup, find_packages
from docs.source.conf import release, author

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='quicktimer',
    packages=['quicktimer'],
    include_package_data=True,
    license='MIT',
    description=('Tracking code performance easily.'),
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/CribberSix/QuickTimer',
    version=release,
    python_requires=">=3.6",
    author=author,
    author_email='cribbersix@gmail.com',
    install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',
    ],
    keywords=['tracking', 'time'],
)

