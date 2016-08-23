from setuptools import setup, find_packages

setup(
    name = 'dispread',
    version = '0.0.1',
    keywords = ('dispread'),
    description = 'This is dispread',
    license = 'MIT License',
    install_requires = ['gspread==0.4.1', 'httplib2==0.9.2', 
                        'oauth2client==2.2.0','pprintpp==0.2.3',
                        'py==1.4.31','pyasn1==0.1.9','pyasn1-modules==0.0.8',
                        'pytest==2.9.2','requests==2.10.0','rsa==3.4.2','six==1.10.0'],

    author = 'Chandler Huang, Xander Li',
    author_email = 'previa@gmail.com',
    
    packages = find_packages(),
    platforms = 'any',
)
