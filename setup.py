from setuptools import setup, find_packages

setup(name='django-dictpatterns',
      version='0.1',
      description='This makes your application be able to write simple urlpatterns with dictionary for Django',
      author='luyikei',
      author_email='luyikei.qmltu@gmail.com',
      url='https://github.com/luyikei/django-dictpatterns',
      download_url='temporary',
      package_dir={'dictpatterns': 'dictpatterns'},
      packages=find_packages(),
      include_package_data=True,
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
)
