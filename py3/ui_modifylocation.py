# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifylocation.ui'
#
# Created: Sun Feb 12 19:56:55 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LocationDialog(object):
    def setupUi(self, LocationDialog):
        LocationDialog.setObjectName("LocationDialog")
        LocationDialog.resize(436, 111)
        self.verticalLayout = QtWidgets.QVBoxLayout(LocationDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.earth_proj = QtWidgets.QWidget(LocationDialog)
        self.earth_proj.setObjectName("earth_proj")
        self.verticalLayout.addWidget(self.earth_proj)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(9, -1, 9, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_box = QtWidgets.QDialogButtonBox(LocationDialog)
        self.button_box.setOrientation(QtCore.Qt.Vertical)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout_2.addWidget(self.button_box, 0, 6, 2, 1)
        self.long_label = QtWidgets.QLabel(LocationDialog)
        self.long_label.setObjectName("long_label")
        self.gridLayout_2.addWidget(self.long_label, 1, 0, 1, 1)
        self.lat_label = QtWidgets.QLabel(LocationDialog)
        self.lat_label.setObjectName("lat_label")
        self.gridLayout_2.addWidget(self.lat_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 2, 1)
        self.line = QtWidgets.QFrame(LocationDialog)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 5, 2, 1)
        self.long_m_spin = QtWidgets.QSpinBox(LocationDialog)
        self.long_m_spin.setMaximum(59)
        self.long_m_spin.setObjectName("long_m_spin")
        self.gridLayout_2.addWidget(self.long_m_spin, 1, 2, 1, 1)
        self.lat_m_spin = QtWidgets.QSpinBox(LocationDialog)
        self.lat_m_spin.setMaximum(59)
        self.lat_m_spin.setObjectName("lat_m_spin")
        self.gridLayout_2.addWidget(self.lat_m_spin, 0, 2, 1, 1)
        self.long_s_spin = QtWidgets.QSpinBox(LocationDialog)
        self.long_s_spin.setMaximum(59)
        self.long_s_spin.setObjectName("long_s_spin")
        self.gridLayout_2.addWidget(self.long_s_spin, 1, 3, 1, 1)
        self.lat_s_spin = QtWidgets.QSpinBox(LocationDialog)
        self.lat_s_spin.setMaximum(59)
        self.lat_s_spin.setObjectName("lat_s_spin")
        self.gridLayout_2.addWidget(self.lat_s_spin, 0, 3, 1, 1)
        self.lat_d_spin = QtWidgets.QSpinBox(LocationDialog)
        self.lat_d_spin.setMinimum(-90)
        self.lat_d_spin.setMaximum(90)
        self.lat_d_spin.setObjectName("lat_d_spin")
        self.gridLayout_2.addWidget(self.lat_d_spin, 0, 1, 1, 1)
        self.long_d_spin = QtWidgets.QSpinBox(LocationDialog)
        self.long_d_spin.setMinimum(-180)
        self.long_d_spin.setMaximum(180)
        self.long_d_spin.setObjectName("long_d_spin")
        self.gridLayout_2.addWidget(self.long_d_spin, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(LocationDialog)
        self.button_box.accepted.connect(LocationDialog.accept)
        self.button_box.rejected.connect(LocationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LocationDialog)

    def retranslateUi(self, LocationDialog):
        _translate = QtCore.QCoreApplication.translate
        LocationDialog.setWindowTitle(_translate("LocationDialog", "Solar System Sequencer - Location"))
        self.long_label.setText(_translate("LocationDialog", "Longitude"))
        self.lat_label.setText(_translate("LocationDialog", "Latitude"))
        self.long_m_spin.setSuffix(_translate("LocationDialog", "m"))
        self.lat_m_spin.setSuffix(_translate("LocationDialog", "m"))
        self.long_s_spin.setSuffix(_translate("LocationDialog", "s"))
        self.lat_s_spin.setSuffix(_translate("LocationDialog", "s"))
        self.lat_d_spin.setSuffix(_translate("LocationDialog", "°"))
        self.long_d_spin.setSuffix(_translate("LocationDialog", "°"))

