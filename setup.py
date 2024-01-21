from setuptools import setup 
  
setup( 
    name='gaussian_splatting', 
    version='0.1', 
    description='Splatting for Modal experiment', 
    author='Matthew Kaufer', 
    author_email='mjkaufer@gmail.com', 
    packages=['.'], 
    install_requires=[ 
        'numpy', 
        'pandas', 
    ], 
) 