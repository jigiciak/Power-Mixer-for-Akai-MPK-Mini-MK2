from ctypes import POINTER, cast
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from gui import Ui_MainWindow
import rtmidi
import sys
from functools import partial


class PowerMixer(QtWidgets.QMainWindow):
    def __init__(self):
        super(PowerMixer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.ui.pushMIDI.clicked.connect(self.control_timer)
        self.ui.listProcess0.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess0))
        self.ui.listProcess1.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess1))
        self.ui.listProcess2.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess2))
        self.ui.listProcess3.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess3))
        self.ui.listProcess4.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess4))
        self.ui.listProcess5.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess5))
        self.ui.listProcess6.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess6))
        self.ui.listProcess7.popupAboutToBeShown.connect(partial(self.scan_processes, self.ui.listProcess7))

        self.ui.listProcess0.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess0.currentText(),
                                                                                     self.ui.sliderProcess0,
                                                                                     self.ui.processValue0))
        self.ui.listProcess1.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess1.currentText(),
                                                                                     self.ui.sliderProcess1,
                                                                                     self.ui.processValue1))
        self.ui.listProcess2.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess2.currentText(),
                                                                                     self.ui.sliderProcess2,
                                                                                     self.ui.processValue2))
        self.ui.listProcess3.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess3.currentText(),
                                                                                     self.ui.sliderProcess3,
                                                                                     self.ui.processValue3))
        self.ui.listProcess4.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess4.currentText(),
                                                                                     self.ui.sliderProcess4,
                                                                                     self.ui.processValue4))
        self.ui.listProcess5.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess5.currentText(),
                                                                                     self.ui.sliderProcess5,
                                                                                     self.ui.processValue5))
        self.ui.listProcess6.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess6.currentText(),
                                                                                     self.ui.sliderProcess6,
                                                                                     self.ui.processValue6))
        self.ui.listProcess7.currentTextChanged.connect(lambda x: self.assign_slider(self.ui.listProcess7.currentText(),
                                                                                     self.ui.sliderProcess7,
                                                                                     self.ui.processValue7))
        self.ui.sliderProcess0.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess0,
                                                                                 self.processList.index(self.ui.listProcess0.currentText()),
                                                                                 self.ui.processValue0))
        self.ui.sliderProcess1.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess1,
                                                                                 self.processList.index(self.ui.listProcess1.currentText()),
                                                                                 self.ui.processValue1))
        self.ui.sliderProcess2.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess2,
                                                                                 self.processList.index(self.ui.listProcess2.currentText()),
                                                                                 self.ui.processValue2))
        self.ui.sliderProcess3.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess3,
                                                                                 self.processList.index(self.ui.listProcess3.currentText()),
                                                                                 self.ui.processValue3))
        self.ui.sliderProcess4.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess4,
                                                                                 self.processList.index(self.ui.listProcess4.currentText()),
                                                                                 self.ui.processValue4))
        self.ui.sliderProcess5.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess5,
                                                                                 self.processList.index(self.ui.listProcess5.currentText()),
                                                                                 self.ui.processValue5))
        self.ui.sliderProcess6.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess6,
                                                                                 self.processList.index(self.ui.listProcess6.currentText()),
                                                                                 self.ui.processValue6))
        self.ui.sliderProcess7.valueChanged.connect(lambda x: self.update_volume(self.ui.sliderProcess7,
                                                                                 self.processList.index(self.ui.listProcess7.currentText()),
                                                                                 self.ui.processValue7))
        self.midiIn = rtmidi.MidiIn()
        self.timer.timeout.connect(self.read_midi)
        self.processList = ["None"]
        self.volumeList = ["None"]

    def control_timer(self):
        if not self.timer.isActive():
            self.timer.start(1)
            self.midiIn.open_port(0)
            self.ui.pushMIDI.setText("Close MIDI Port")
        else:
            self.timer.stop()
            self.midiIn.close_port()
            self.ui.pushMIDI.setText("Open MIDI Port")

    def read_midi(self):
        message = self.midiIn.get_message()
        if message:
            if message[0][1] == 1 and self.ui.listProcess0.currentText() != 'None':
                self.ui.sliderProcess0.setValue(message[0][2]/127*100)
            if message[0][1] == 2 and self.ui.listProcess1.currentText() != 'None':
                self.ui.sliderProcess1.setValue(message[0][2]/127*100)
            if message[0][1] == 3 and self.ui.listProcess2.currentText() != 'None':
                self.ui.sliderProcess2.setValue(message[0][2]/127*100)
            if message[0][1] == 4 and self.ui.listProcess3.currentText() != 'None':
                self.ui.sliderProcess3.setValue(message[0][2]/127*100)
            if message[0][1] == 5 and self.ui.listProcess4.currentText() != 'None':
                self.ui.sliderProcess4.setValue(message[0][2]/127*100)
            if message[0][1] == 6 and self.ui.listProcess5.currentText() != 'None':
                self.ui.sliderProcess5.setValue(message[0][2]/127*100)
            if message[0][1] == 7 and self.ui.listProcess6.currentText() != 'None':
                self.ui.sliderProcess6.setValue(message[0][2]/127*100)
            if message[0][1] == 8 and self.ui.listProcess7.currentText() != 'None':
                self.ui.sliderProcess7.setValue(message[0][2]/127*100)

    def scan_processes(self, processes):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process:
                self.volumeList.append(cast(session.SimpleAudioVolume, POINTER(ISimpleAudioVolume)))
                if session.Process.name() not in self.processList:
                    self.processList.append(session.Process.name())
        processes.clear()
        processes.addItems(self.processList)

    @staticmethod
    def assign_slider(process, slider, value):
        if process != "None":
            slider.setEnabled(1)
            value.setEnabled(1)
        else:
            slider.setDisabled(1)
            value.setDisabled(1)

    def update_volume(self, slider, volume, value):
        self.volumeList[volume].SetMasterVolume(slider.value()/100, None)
        value.setText(str(slider.value()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = PowerMixer()
    application.show()
    sys.exit(app.exec_())
