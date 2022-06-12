import os
import shutil
from PIL import Image
import ctypes

LocalAppData = os.environ['LocalAppData']
UserProfile = os.environ['USERPROFILE']

spotlightDir = f'{LocalAppData}\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
saveDir = f'{UserProfile}\Documents\Spotlight'
# https://en.wikipedia.org/wiki/Environment_variable?=section13#Default_values

if not os.path.exists(saveDir):
    os.makedirs(saveDir)

for files in os.listdir(spotlightDir):
    shutil.copy((f'{spotlightDir}\{files}'), (f'{saveDir}\{files}.png'))

for images in os.listdir(saveDir):
    if images.endswith('.png'):
        absPath = str(f'{saveDir}\{images}')
        width, height = 0,0
        with Image.open(absPath) as im:
            width, height = im.size
        if width < height:
            os.remove(absPath)

ctypes.windll.user32.MessageBoxW(0, f"All spotlight images found on your device have been downloaded. To check them out, head over to {saveDir}", "Spotlight Downloader", 0)