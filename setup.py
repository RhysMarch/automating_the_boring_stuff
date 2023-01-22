from setuptools import setup

APP = ['court_booking.py']
DATA_FILES = [('', ['config.json'])]
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'Court Booking',
        'CFBundleDisplayName': 'Court Booking',
        'CFBundleGetInfoString': 'Court Booking',
        'CFBundleIdentifier': 'com.court.booking',
        'CFBundleVersion': '0.1',
        'CFBundleShortVersionString': '0.1',
        'CFBundleSignature': '????',
        'LSMinimumSystemVersion': '10.9.0',
        'LSApplicationCategoryType': 'public.app-category.utilities',
    },
    'includes': ['selenium', 'webdriver_manager', 'schedule', 'logging', 'json'],
    'excludes': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
