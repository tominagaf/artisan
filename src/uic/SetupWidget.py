# Form implementation generated from reading ui file 'ui/SetupWidget.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SetupWidget(object):
    def setupUi(self, SetupWidget):
        SetupWidget.setObjectName("SetupWidget")
        SetupWidget.resize(344, 305)
        SetupWidget.setWindowTitle("Form")
        SetupWidget.setToolTip("")
        SetupWidget.setAccessibleDescription("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SetupWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SetupWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditOrganization = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOrganization.sizePolicy().hasHeightForWidth())
        self.lineEditOrganization.setSizePolicy(sizePolicy)
        self.lineEditOrganization.setToolTip("")
        self.lineEditOrganization.setText("")
        self.lineEditOrganization.setObjectName("lineEditOrganization")
        self.gridLayout.addWidget(self.lineEditOrganization, 0, 1, 1, 2)
        self.lineEditOperator = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOperator.sizePolicy().hasHeightForWidth())
        self.lineEditOperator.setSizePolicy(sizePolicy)
        self.lineEditOperator.setToolTip("")
        self.lineEditOperator.setText("")
        self.lineEditOperator.setObjectName("lineEditOperator")
        self.gridLayout.addWidget(self.lineEditOperator, 1, 1, 1, 2)
        self.labelOperator = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.labelOperator.setFont(font)
        self.labelOperator.setToolTip("")
        self.labelOperator.setText("Operator")
        self.labelOperator.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelOperator.setObjectName("labelOperator")
        self.gridLayout.addWidget(self.labelOperator, 1, 0, 1, 1)
        self.labelOrganization = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.labelOrganization.setFont(font)
        self.labelOrganization.setToolTip("")
        self.labelOrganization.setText("Organization")
        self.labelOrganization.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.labelOrganization.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelOrganization.setObjectName("labelOrganization")
        self.gridLayout.addWidget(self.labelOrganization, 0, 0, 1, 1)
        self.labelOrganizationDefault = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOrganizationDefault.sizePolicy().hasHeightForWidth())
        self.labelOrganizationDefault.setSizePolicy(sizePolicy)
        self.labelOrganizationDefault.setToolTip("")
        self.labelOrganizationDefault.setAccessibleDescription("")
        self.labelOrganizationDefault.setStyleSheet("QLabel { color : grey; }")
        self.labelOrganizationDefault.setText("")
        self.labelOrganizationDefault.setObjectName("labelOrganizationDefault")
        self.gridLayout.addWidget(self.labelOrganizationDefault, 0, 3, 1, 1)
        self.labelOperatorDefault = QtWidgets.QLabel(self.groupBox)
        self.labelOperatorDefault.setToolTip("")
        self.labelOperatorDefault.setAccessibleDescription("")
        self.labelOperatorDefault.setStyleSheet("QLabel { color : grey; }")
        self.labelOperatorDefault.setText("")
        self.labelOperatorDefault.setObjectName("labelOperatorDefault")
        self.gridLayout.addWidget(self.labelOperatorDefault, 1, 3, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxMachine = QtWidgets.QGroupBox(SetupWidget)
        self.groupBoxMachine.setToolTip("")
        self.groupBoxMachine.setAccessibleDescription("")
        self.groupBoxMachine.setTitle("Machine")
        self.groupBoxMachine.setObjectName("groupBoxMachine")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxMachine)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayoutMachine = QtWidgets.QGridLayout()
        self.gridLayoutMachine.setObjectName("gridLayoutMachine")
        self.doubleSpinBoxRoasterSize = QtWidgets.QDoubleSpinBox(self.groupBoxMachine)
        self.doubleSpinBoxRoasterSize.setToolTip("")
        self.doubleSpinBoxRoasterSize.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBoxRoasterSize.setSuffix("kg")
        self.doubleSpinBoxRoasterSize.setDecimals(1)
        self.doubleSpinBoxRoasterSize.setMaximum(9999.9)
        self.doubleSpinBoxRoasterSize.setObjectName("doubleSpinBoxRoasterSize")
        self.gridLayoutMachine.addWidget(self.doubleSpinBoxRoasterSize, 0, 2, 1, 1)
        self.labelHeating = QtWidgets.QLabel(self.groupBoxMachine)
        font = QtGui.QFont()
        font.setBold(True)
        self.labelHeating.setFont(font)
        self.labelHeating.setAccessibleDescription("")
        self.labelHeating.setText("Heating")
        self.labelHeating.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelHeating.setObjectName("labelHeating")
        self.gridLayoutMachine.addWidget(self.labelHeating, 1, 0, 1, 1)
        self.labelDrumSpeed = QtWidgets.QLabel(self.groupBoxMachine)
        font = QtGui.QFont()
        font.setBold(True)
        self.labelDrumSpeed.setFont(font)
        self.labelDrumSpeed.setToolTip("")
        self.labelDrumSpeed.setText("Drum Speed")
        self.labelDrumSpeed.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelDrumSpeed.setObjectName("labelDrumSpeed")
        self.gridLayoutMachine.addWidget(self.labelDrumSpeed, 2, 0, 1, 1)
        self.lineEditDrumSpeed = QtWidgets.QLineEdit(self.groupBoxMachine)
        self.lineEditDrumSpeed.setToolTip("")
        self.lineEditDrumSpeed.setText("")
        self.lineEditDrumSpeed.setObjectName("lineEditDrumSpeed")
        self.gridLayoutMachine.addWidget(self.lineEditDrumSpeed, 2, 1, 1, 2)
        self.comboBoxHeating = QtWidgets.QComboBox(self.groupBoxMachine)
        self.comboBoxHeating.setObjectName("comboBoxHeating")
        self.gridLayoutMachine.addWidget(self.comboBoxHeating, 1, 1, 1, 2)
        self.labelMachine = QtWidgets.QLabel(self.groupBoxMachine)
        font = QtGui.QFont()
        font.setBold(True)
        self.labelMachine.setFont(font)
        self.labelMachine.setToolTip("")
        self.labelMachine.setText("Model")
        self.labelMachine.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelMachine.setObjectName("labelMachine")
        self.gridLayoutMachine.addWidget(self.labelMachine, 0, 0, 1, 1)
        self.lineEditMachine = QtWidgets.QLineEdit(self.groupBoxMachine)
        self.lineEditMachine.setToolTip("")
        self.lineEditMachine.setText("")
        self.lineEditMachine.setObjectName("lineEditMachine")
        self.gridLayoutMachine.addWidget(self.lineEditMachine, 0, 1, 1, 1)
        self.labelMachineSizeDefault = QtWidgets.QLabel(self.groupBoxMachine)
        self.labelMachineSizeDefault.setToolTip("")
        self.labelMachineSizeDefault.setAccessibleDescription("")
        self.labelMachineSizeDefault.setStyleSheet("QLabel { color : grey; }")
        self.labelMachineSizeDefault.setText("")
        self.labelMachineSizeDefault.setObjectName("labelMachineSizeDefault")
        self.gridLayoutMachine.addWidget(self.labelMachineSizeDefault, 0, 3, 1, 1)
        self.labelHeatingDefault = QtWidgets.QLabel(self.groupBoxMachine)
        self.labelHeatingDefault.setToolTip("")
        self.labelHeatingDefault.setAccessibleDescription("")
        self.labelHeatingDefault.setStyleSheet("QLabel { color : grey; }")
        self.labelHeatingDefault.setText("")
        self.labelHeatingDefault.setObjectName("labelHeatingDefault")
        self.gridLayoutMachine.addWidget(self.labelHeatingDefault, 1, 3, 1, 1)
        self.labelDrumSpeedDefault = QtWidgets.QLabel(self.groupBoxMachine)
        self.labelDrumSpeedDefault.setToolTip("")
        self.labelDrumSpeedDefault.setAccessibleDescription("")
        self.labelDrumSpeedDefault.setStyleSheet("QLabel { color : grey; }")
        self.labelDrumSpeedDefault.setText("")
        self.labelDrumSpeedDefault.setObjectName("labelDrumSpeedDefault")
        self.gridLayoutMachine.addWidget(self.labelDrumSpeedDefault, 2, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayoutMachine)
        self.verticalLayout.addWidget(self.groupBoxMachine)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SetDefaults = QtWidgets.QPushButton(SetupWidget)
        self.SetDefaults.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.SetDefaults.setToolTip("")
        self.SetDefaults.setText("Set as Defaults")
        self.SetDefaults.setObjectName("SetDefaults")
        self.horizontalLayout.addWidget(self.SetDefaults)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Defaults = QtWidgets.QPushButton(SetupWidget)
        self.Defaults.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Defaults.setToolTip("")
        self.Defaults.setText("Restore Defaults")
        self.Defaults.setObjectName("Defaults")
        self.horizontalLayout.addWidget(self.Defaults)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(SetupWidget)
        QtCore.QMetaObject.connectSlotsByName(SetupWidget)
        SetupWidget.setTabOrder(self.lineEditOrganization, self.lineEditOperator)
        SetupWidget.setTabOrder(self.lineEditOperator, self.lineEditMachine)
        SetupWidget.setTabOrder(self.lineEditMachine, self.doubleSpinBoxRoasterSize)
        SetupWidget.setTabOrder(self.doubleSpinBoxRoasterSize, self.comboBoxHeating)
        SetupWidget.setTabOrder(self.comboBoxHeating, self.lineEditDrumSpeed)

    def retranslateUi(self, SetupWidget):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetupWidget = QtWidgets.QWidget()
    ui = Ui_SetupWidget()
    ui.setupUi(SetupWidget)
    SetupWidget.show()
    sys.exit(app.exec())
