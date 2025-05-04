from setuptools import setup, find_packages


setup(
    name='BingxPy',
    version='1.0.0',
    author='Abbas Bachari',
    author_email='abbas-bachari@hotmail.com',
    description="This is a lightweight library that works as a connector to BingX public API.",
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/abbas-bachari/BingxPy',
    python_requires='>=3.8',
    project_urls={
    "Homepage":'https://github.com/abbas-bachari/BingxPy',
    'Documentation': 'https://github.com/abbas-bachari/BingxPy',
    'Source': 'https://github.com/abbas-bachari/BingxPy/',
    'Tracker': 'https://github.com/abbas-bachari/BingxPy/issues',
   
},
    
    install_requires=['websocket-client'],
    keywords=['Bingx', 'Bingx-sdk', 'Bingx-python', 'BingxPy',  'Bingx-api'],
    classifiers=[
        'Intended Audience :: Developers',
        "Intended Audience :: Financial and Insurance Industry",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        
        
    ],
    
    
)

