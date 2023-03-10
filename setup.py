from setuptools import setup, find_packages


setup(name='CWTVLAD',
      version='1.0',
      description='Open-source toolbox for Visual Place Recognition',
      author_email='yifanxu98@163.com',
      url='https://github.com/cvprw-22/TVLAD',
      license='MIT',
      install_requires=[
          'numpy', 'torch', 'torchvision', 'opencv-python',
          'six', 'h5py', 'Pillow', 'scipy',
          'scikit-learn', 'metric-learn'],
      packages=find_packages(),
      keywords=[
        'Viusal Place Recognition',
        'Image Retrieval'  
      ])
