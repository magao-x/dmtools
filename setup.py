# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
NAME = 'magpyx'

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get version
with open(path.join(here, NAME, 'VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(
    name=NAME,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description="Python DM tools for MagAO-X",
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/magao-x/magpyx',

    # Author details
    author='Kyle Van Gorkom',
    author_email='kvangorkom@email.arizona.edu',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # add shell scripts here
    entry_points = {
        'console_scripts': ['dm_project_zernikes=magpyx.dm.project_zernikes:main',
                            'dm_offload_matrix=magpyx.dm.t2w_offload:main',
                            'dm_eye_doctor=magpyx.dm.eye_doctor:console_comprehensive',
                            #'dm_eye_doctor_mode=magpyx.dm.eye_doctor:console_modal',
                            'dm_save_flat=magpyx.dm.eye_doctor:console_write_new_flat',
                            'dm_zero_all_modes=magpyx.dm.eye_doctor:console_zero_all_modes',
                            'dm_eye_doctor_update_flat=magpyx.dm.eye_doctor:console_update_flat',
                            'dm_send_poke=magpyx.utils:console_send_dm_poke',
                            'tweeter_V2um=magpyx.utils:console_tweeter_V2um',
                            'tweeter_um2V=magpyx.utils:console_tweeter_um2V',
                            'send_fits_to_shmim=magpyx.utils:console_send_fits_to_shmim',
                            'send_shmim_to_fits=magpyx.utils:console_send_shmim_to_fits',
                            'send_zeros_to_shmim=magpyx.utils:console_send_zeros_to_shmim',
                            'pyindi_send_preset=magpyx.presets:main',
                            'pyindi_send_triplet=magpyx.presets:send_indi_triplet',
                            'auto_focus=magpyx.focus_stage:main',
                            'fdpr_estimate_response=magpyx.phase_retrieval.console:console_estimate_response_matrix',
                            'fdpr_measure_response=magpyx.phase_retrieval.console:console_measure_response_matrix',
                            'fdpr_compute_control_matrix=magpyx.phase_retrieval.console:console_compute_control_matrix',
                            'fdpr_close_loop=magpyx.phase_retrieval.console:console_close_loop',
                            'fdpr_oneshot=magpyx.phase_retrieval.console:console_estimate_oneshot',
                            'fdpr_rsync_remote=magpyx.phase_retrieval.console:console_rsync_calibration_directory',
                            'fdpr2_estimate_response=magpyx.fdpr2.console:console_estimate_response_matrix',
                            'fdpr2_measure_response=magpyx.fdpr2.console:console_measure_response_matrix',
                            'fdpr2_compute_control_matrix=magpyx.fdpr2.console:console_compute_control_matrix',
                            'fdpr2_close_loop=magpyx.fdpr2.console:console_close_loop',
                            'fdpr2_oneshot=magpyx.fdpr2.console:console_estimate_oneshot',
                            'fdpr2_test_defocus=magpyx.fdpr2.console:console_test_defocus',]
    },
    
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy','astropy', 'poppy'],
)