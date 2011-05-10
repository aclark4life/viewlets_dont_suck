from setuptools import setup, find_packages

setup(
    name='viewlets_dont_suck',
    packages=find_packages(),
    namespace_packages=[
        'they',
        'they.are',
        'they.are.just',
        'they.are.just.really',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """
)
