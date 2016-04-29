from setuptools import setup, find_packages

setup(
    name='django-two-factor-auth',
    version='1.3.1',
    description='Complete Two-Factor Authentication for Django',
    long_description=open('README.rst').read(),
    author='Bouke Haarsma',
    author_email='bouke@haarsma.eu',
    url='https://github.com/altanawealth/django-two-factor-auth.git',
    download_url='https://github.com/altanawealth/django-two-factor-auth.git',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests')),
    install_requires=[
        'Django>=1.8,<1.9.99',
        'django_otp>=0.3.5',
        'qrcode>=4.0.0,<4.99',
        'phonenumbers>=7.0.9,<7.99',
        'django-phonenumber-field>=0.7.2,<0.99',
        'django-formtools',
    ],
    dependency_links = [
        'https://github.com/altanawealth/django-otp.git#egg=django_otp-0.3.5',
    ]
    extras_require={
        'Call': ['twilio'],
        'SMS': ['twilio'],
        'YubiKey': ['django-otp-yubikey'],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
)
