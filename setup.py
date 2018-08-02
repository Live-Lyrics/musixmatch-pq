import setuptools

setuptools.setup(
    name="musixmatch-pq",
    version="0.0.1",
    author="andriyor",
    author_email="andriyorehov@gmail.com",
    description="musixmatch scraper",
    install_requires=[
        'requests',
        'pyquery',
        'fake_useragent'
    ],
)
