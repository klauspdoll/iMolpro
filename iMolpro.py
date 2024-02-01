import pathlib
import shutil
from contextlib import redirect_stdout, redirect_stderr

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys

from settings import settings
from Chooser import Chooser
from ProjectWindow import ProjectWindow
from WindowManager import WindowManager
import os

if __name__ == '__main__':

    class App(QApplication):
        def event(self, e):
            if e.type() == QEvent.FileOpen and os.path.splitext(e.file())[1] == '.molpro':
                window_manager.register(ProjectWindow(e.file(), window_manager))
            else:
                return super().event(e)
            return True


    if hasattr(sys, '_MEIPASS'):
        sys.stdout = open('/tmp/iMolpro.stdout', 'w')
        sys.stderr = open('/tmp/iMolpro.stderr', 'w')

    if os.uname().sysname == 'Linux':
        if 'FONTCONFIG_PATH' not in os.environ:
            os.environ['FONTCONFIG_PATH'] = '/etc/fonts'
        if 'FONTCONFIG_FILE' not in os.environ:
            os.environ['FONTCONFIG_FILE'] = '/etc/fonts/fonts.conf'
            
    app = App(sys.argv)

    if 'Trash' not in settings:
        settings['Trash'] = str(pathlib.Path(os.path.expanduser('~')) / pathlib.Path('.molpro') / 'iMolpro.trash')
    shutil.rmtree(settings['Trash'], ignore_errors=True)

    window_manager = WindowManager()
    chooser = Chooser(window_manager)
    chooser.quitButton.clicked.connect(app.quit)
    window_manager.set_empty_action(chooser.activate)
    window_manager.set_full_action(chooser.hide)

    for arg in sys.argv[1:]:
        window_manager.register(ProjectWindow(arg, window_manager))

    app.exec()
