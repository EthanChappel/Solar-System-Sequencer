# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedulebrain.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScheduleBrainDialog(object):
    def setupUi(self, ScheduleBrainDialog):
        ScheduleBrainDialog.setObjectName("ScheduleBrainDialog")
        ScheduleBrainDialog.resize(426, 158)
        self.gridLayout = QtWidgets.QGridLayout(ScheduleBrainDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonbox = QtWidgets.QDialogButtonBox(ScheduleBrainDialog)
        self.buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonbox.setObjectName("buttonbox")
        self.gridLayout.addWidget(self.buttonbox, 2, 1, 1, 1)
        self.object_groupbox = QtWidgets.QGroupBox(ScheduleBrainDialog)
        self.object_groupbox.setObjectName("object_groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.object_groupbox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.mercury_checkbox = QtWidgets.QCheckBox(self.object_groupbox)
        self.mercury_checkbox.setChecked(True)
        self.mercury_checkbox.setObjectName("mercury_checkbox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mercury_checkbox)
        self.saturn_checkbox = QtWidgets.QCheckBox(self.object_groupbox)
        self.saturn_checkbox.setChecked(True)
        self.saturn_checkbox.setObjectName("saturn_checkbox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.saturn_checkbox)
        self.venus_checkbox = QtWidgets.QCheckBox(self.object_groupbox)
        self.venus_checkbox.setChecked(True)
        self.venus_checkbox.setObjectName("venus_checkbox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.venus_checkbox)
        self.uranus_checkbox = QtWidgets.QCheckBox(self.object_groupbox)
        self.uranus_checkbox.setChecked(True)
        self.uranus_checkbox.setObjectName("uranus_checkbox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uranus_checkbox)
        self.mars_checkbox = QtWidgets.QCheckBox(self.object_groupbox)
        self.mars_checkbox.setChecked(True)
        self.mars_checkbox.setObjectName("mars_checkbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mars_checkbox)
        self.neptune_checkbox = QtWidgets.QCheckBox(self.object_groupbox)
        self.neptune_checkbox.setChecked(True)
        self.neptune_checkbox.setObjectName("neptune_checkbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.neptune_checkbox)
        self.jupiter_checkbox = QtWidgets.QCheckBox(self.object_groupbox)
        self.jupiter_checkbox.setChecked(True)
        self.jupiter_checkbox.setObjectName("jupiter_checkbox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.jupiter_checkbox)
        self.gridLayout.addWidget(self.object_groupbox, 1, 0, 2, 1)
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.darkness_label = QtWidgets.QLabel(ScheduleBrainDialog)
        self.darkness_label.setObjectName("darkness_label")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.darkness_label)
        self.time_label = QtWidgets.QLabel(ScheduleBrainDialog)
        self.time_label.setObjectName("time_label")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.time_label)
        self.time_layout = QtWidgets.QHBoxLayout()
        self.time_layout.setObjectName("time_layout")
        self.start_timeedit = QtWidgets.QTimeEdit(ScheduleBrainDialog)
        self.start_timeedit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 58, 0)))
        self.start_timeedit.setMaximumTime(QtCore.QTime(23, 58, 0))
        self.start_timeedit.setTimeSpec(QtCore.Qt.LocalTime)
        self.start_timeedit.setTime(QtCore.QTime(0, 0, 0))
        self.start_timeedit.setObjectName("start_timeedit")
        self.time_layout.addWidget(self.start_timeedit)
        self.time_to_label = QtWidgets.QLabel(ScheduleBrainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_to_label.sizePolicy().hasHeightForWidth())
        self.time_to_label.setSizePolicy(sizePolicy)
        self.time_to_label.setObjectName("time_to_label")
        self.time_layout.addWidget(self.time_to_label)
        self.end_timeedit = QtWidgets.QTimeEdit(ScheduleBrainDialog)
        self.end_timeedit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 0)))
        self.end_timeedit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 0)))
        self.end_timeedit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 1, 0)))
        self.end_timeedit.setMinimumTime(QtCore.QTime(0, 1, 0))
        self.end_timeedit.setTimeSpec(QtCore.Qt.LocalTime)
        self.end_timeedit.setObjectName("end_timeedit")
        self.time_layout.addWidget(self.end_timeedit)
        self.form_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.time_layout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minelevation_spinbox = QtWidgets.QSpinBox(ScheduleBrainDialog)
        self.minelevation_spinbox.setMaximum(89)
        self.minelevation_spinbox.setObjectName("minelevation_spinbox")
        self.horizontalLayout_2.addWidget(self.minelevation_spinbox)
        self.elevation_to_label = QtWidgets.QLabel(ScheduleBrainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elevation_to_label.sizePolicy().hasHeightForWidth())
        self.elevation_to_label.setSizePolicy(sizePolicy)
        self.elevation_to_label.setObjectName("elevation_to_label")
        self.horizontalLayout_2.addWidget(self.elevation_to_label)
        self.maxelevation_spinbox = QtWidgets.QSpinBox(ScheduleBrainDialog)
        self.maxelevation_spinbox.setMinimum(1)
        self.maxelevation_spinbox.setMaximum(90)
        self.maxelevation_spinbox.setProperty("value", 90)
        self.maxelevation_spinbox.setObjectName("maxelevation_spinbox")
        self.horizontalLayout_2.addWidget(self.maxelevation_spinbox)
        self.form_layout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.east_radiobutton = QtWidgets.QRadioButton(ScheduleBrainDialog)
        self.east_radiobutton.setObjectName("east_radiobutton")
        self.preference_buttongroup = QtWidgets.QButtonGroup(ScheduleBrainDialog)
        self.preference_buttongroup.setObjectName("preference_buttongroup")
        self.preference_buttongroup.addButton(self.east_radiobutton)
        self.horizontalLayout.addWidget(self.east_radiobutton)
        self.west_radiobutton = QtWidgets.QRadioButton(ScheduleBrainDialog)
        self.west_radiobutton.setObjectName("west_radiobutton")
        self.preference_buttongroup.addButton(self.west_radiobutton)
        self.horizontalLayout.addWidget(self.west_radiobutton)
        self.form_layout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtWidgets.QLabel(ScheduleBrainDialog)
        self.label.setObjectName("label")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.elevation_label = QtWidgets.QLabel(ScheduleBrainDialog)
        self.elevation_label.setObjectName("elevation_label")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.elevation_label)
        self.sunelevation_spinbox = QtWidgets.QSpinBox(ScheduleBrainDialog)
        self.sunelevation_spinbox.setMinimum(-90)
        self.sunelevation_spinbox.setMaximum(90)
        self.sunelevation_spinbox.setProperty("value", -18)
        self.sunelevation_spinbox.setObjectName("sunelevation_spinbox")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sunelevation_spinbox)
        self.gridLayout.addLayout(self.form_layout, 1, 1, 1, 1)
        self.plot_layout = QtWidgets.QHBoxLayout()
        self.plot_layout.setObjectName("plot_layout")
        self.gridLayout.addLayout(self.plot_layout, 0, 0, 1, 2)

        self.retranslateUi(ScheduleBrainDialog)
        self.buttonbox.accepted.connect(ScheduleBrainDialog.accept)
        self.buttonbox.rejected.connect(ScheduleBrainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ScheduleBrainDialog)

    def retranslateUi(self, ScheduleBrainDialog):
        _translate = QtCore.QCoreApplication.translate
        ScheduleBrainDialog.setWindowTitle(_translate("ScheduleBrainDialog", "Schedule Brain"))
        self.object_groupbox.setTitle(_translate("ScheduleBrainDialog", "Objects"))
        self.mercury_checkbox.setText(_translate("ScheduleBrainDialog", "Mercury"))
        self.saturn_checkbox.setText(_translate("ScheduleBrainDialog", "Saturn"))
        self.venus_checkbox.setText(_translate("ScheduleBrainDialog", "Venus"))
        self.uranus_checkbox.setText(_translate("ScheduleBrainDialog", "Uranus"))
        self.mars_checkbox.setText(_translate("ScheduleBrainDialog", "Mars"))
        self.neptune_checkbox.setText(_translate("ScheduleBrainDialog", "Neptune"))
        self.jupiter_checkbox.setText(_translate("ScheduleBrainDialog", "Jupiter"))
        self.darkness_label.setText(_translate("ScheduleBrainDialog", "Maximum Sun Elevation"))
        self.time_label.setText(_translate("ScheduleBrainDialog", "Time Range"))
        self.start_timeedit.setDisplayFormat(_translate("ScheduleBrainDialog", "hh:mm"))
        self.time_to_label.setText(_translate("ScheduleBrainDialog", "to"))
        self.end_timeedit.setDisplayFormat(_translate("ScheduleBrainDialog", "hh:mm"))
        self.minelevation_spinbox.setSuffix(_translate("ScheduleBrainDialog", "°"))
        self.elevation_to_label.setText(_translate("ScheduleBrainDialog", "to"))
        self.maxelevation_spinbox.setSuffix(_translate("ScheduleBrainDialog", "°"))
        self.east_radiobutton.setText(_translate("ScheduleBrainDialog", "East"))
        self.west_radiobutton.setText(_translate("ScheduleBrainDialog", "West"))
        self.label.setText(_translate("ScheduleBrainDialog", "Directional Preference"))
        self.elevation_label.setText(_translate("ScheduleBrainDialog", "Elevation Range"))
        self.sunelevation_spinbox.setToolTip(_translate("ScheduleBrainDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Night<br/></span>Sun &gt; 18° below horizon</p><p><span style=\" font-weight:600;\">Astronomical Twilight<br/></span>Sun &gt; 12° below horizon</p><p><span style=\" font-weight:600;\">Nautical Twilight<br/></span>Sun &gt; 6° below horizon</p><p><span style=\" font-weight:600;\">Civil Twilight<br/></span>Sun &gt; 0° below horizon</p></body></html>"))
        self.sunelevation_spinbox.setSuffix(_translate("ScheduleBrainDialog", "°"))

