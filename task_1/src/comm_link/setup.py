from setuptools import find_packages, setup

package_name = 'comm_link'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abhay-ramasamy',
    maintainer_email='cartoonistabhay@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        	'invictus_node = comm_link.invictus_node:main',
    		'hawcker_node = comm_link.hawcker_node:main',
        ],
    },
)
