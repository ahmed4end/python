# made by a.s.a
import sys , subprocess  , os
from PyQt5.QtWidgets import (QWidget,QApplication,QLabel,QSlider,QLineEdit,QPushButton,QCheckBox,QHBoxLayout,QVBoxLayout,QDesktopWidget,QMessageBox)
from PyQt5.QtGui import QIcon

class window(QWidget):
	def __init__(self):
		super().__init__()
		self.ckboxValues = 0
		self.ui()

	def ui(self):
		
		self.shutdown = QPushButton('Shutdown')
		self.shutdown.setMinimumSize(0,35)
		self.cancel = QPushButton('Cancel !')
		self.cancel.setMinimumSize(0,25)
		self.lineEdit = QLineEdit()
		self.lineEdit.setTextMargins(50,10,0,10)
		self.label = QLabel('input as minutes !')
		
		#Slider options .
		self.slider = QSlider()
		self.slider.setValue(0)
		self.slider.setMinimum(0)
		self.slider.setMaximum(180)
		self.slider.setTickInterval(15)
		self.slider.setTickPosition(QSlider.TicksBelow)

		#checkboxes column 1.
		self.checkbox_15m = QCheckBox('15 min')
		self.checkbox_30m = QCheckBox('30 min')
		self.checkbox_45m = QCheckBox('45 min')
		self.checkbox_60m = QCheckBox('60 min')

		#checkboxes column 2.
		self.checkbox_2h = QCheckBox('2 hours')
		self.checkbox_3h = QCheckBox('3 hours')
		self.checkbox_4h = QCheckBox('4 hours')
		self.checkbox_5h = QCheckBox('5 hours')


		#checkboxes column 1 layout.
		ckbx_c1 = QVBoxLayout()
		ckbx_c1.addWidget(self.checkbox_15m)
		ckbx_c1.addWidget(self.checkbox_30m)
		ckbx_c1.addWidget(self.checkbox_45m)
		ckbx_c1.addWidget(self.checkbox_60m)
		
		#checkboxes column 2 layout.
		ckbx_c2 = QVBoxLayout()
		ckbx_c2.addWidget(self.checkbox_2h)
		ckbx_c2.addWidget(self.checkbox_3h)
		ckbx_c2.addWidget(self.checkbox_4h)
		ckbx_c2.addWidget(self.checkbox_5h)

		#checkboxes horizontal layout (both the recent two columns) .
		checkboxes_vlayout = QHBoxLayout()
		checkboxes_vlayout.addLayout(ckbx_c1)
		checkboxes_vlayout.addLayout(ckbx_c2)

		#more widgeting....
		vbox = QVBoxLayout()
		vbox.addWidget(self.lineEdit)
		vbox.addWidget(self.shutdown)
		vbox.addWidget(self.cancel)
		vbox.addLayout(checkboxes_vlayout)

		#label stretching from both sides :"D
		lbox = QHBoxLayout()
		lbox.addStretch()
		lbox.addWidget(self.label)
		lbox.addStretch()
		vbox.addLayout(lbox)

		hbox = QHBoxLayout()
		hbox.addWidget(self.slider)
		hbox.addLayout(vbox)

		self.setLayout(hbox)

		self.slider.valueChanged.connect(self.slide)

		#connecting checkboxes to slots to start ...
		self.checkbox_15m.stateChanged.connect(self.checkboxes)
		self.checkbox_30m.stateChanged.connect(self.checkboxes)
		self.checkbox_45m.stateChanged.connect(self.checkboxes)
		self.checkbox_60m.stateChanged.connect(self.checkboxes)
		self.checkbox_2h.stateChanged.connect(self.checkboxes)
		self.checkbox_3h.stateChanged.connect(self.checkboxes)
		self.checkbox_4h.stateChanged.connect(self.checkboxes)
		self.checkbox_5h.stateChanged.connect(self.checkboxes)



		#connecting slots to signals.
		self.shutdown.clicked.connect(lambda: self.btnClicked(self.shutdown))
		self.cancel.clicked.connect(lambda: self.btnClicked(self.cancel))



		size = QDesktopWidget().screenGeometry()

		self.setMaximumSize(50,50)
		self.setGeometry( (size.width()/2 - 150),(size.height()/2 - 150),50,50)
		self.setWindowIcon(QIcon('icon.ico'))  #optional icon.ico
		self.setWindowTitle('CS')
		self.show()





	def slide(self):
		self.lineEdit.setText( str( self.slider.value() + self.ckboxValues ) )


	def checkboxes(self):

		self.ckboxValues = 0

		self.label.setText('you can select more (!).')

		if self.checkbox_15m.isChecked():
			self.ckboxValues += 15
		if self.checkbox_30m.isChecked():
			self.ckboxValues += 30
		if self.checkbox_45m.isChecked():
			self.ckboxValues += 45
		if self.checkbox_60m.isChecked():
			self.ckboxValues += 60
		if self.checkbox_2h.isChecked():
			self.ckboxValues += 120
		if self.checkbox_3h.isChecked():
			self.ckboxValues += (60*3)
		if self.checkbox_4h.isChecked():
			self.ckboxValues += (60*4)
		if self.checkbox_5h.isChecked():
			self.ckboxValues += (60*5)

		self.lineEdit.setText( str( self.slider.value() + self.ckboxValues ) )

	def btnClicked(self , button):
		try:
			fromSButton = False

			if button.text() == 'Shutdown':
				if int(self.lineEdit.text()) == 0:
					warning = QMessageBox.question(self, 'Warning', "Your Pc will shutdown right now , are you sure ?", QMessageBox.Yes | QMessageBox.Cancel ,QMessageBox.Cancel  )
					if warning == QMessageBox.Yes:
						self.label.setText('Shutdown is confirmed')
					elif warning == QMessageBox.Cancel:
						self.label.setText('Shutdown is cancelled')
						fromSButton = True
						raise Error('Lol')    #this is a tricky damn way to escape python bullshit , hope you got it.

				subprocess.call(f'shutdown -s -f -t "{str(int(self.lineEdit.text()) * 60 )}" ', shell=True)
				
				self.label.setText(f'Pc will shutdown in { str( round( int( self.lineEdit.text() ) / 60  , 2)) } h.')

			if button.text()  == 'Cancel !':
				subprocess.call(f'shutdown -a' , shell=True)
				self.label.setText('shutdown is cancelled !')
				self.lineEdit.clear()
				self.checkbox_15m.setChecked(False)
				self.checkbox_45m.setChecked(False)
				self.checkbox_30m.setChecked(False)
				self.checkbox_60m.setChecked(False)
				self.checkbox_2h.setChecked(False)
				self.checkbox_3h.setChecked(False)
				self.checkbox_4h.setChecked(False)
				self.checkbox_5h.setChecked(False)
		except:
			if not fromSButton:
				self.label.setText('please, enter only numbers.')
				warning = QMessageBox.question(self, 'Warning', "Please, Enter only numbers (minutes).?!", QMessageBox.Ok | QMessageBox.No ,QMessageBox.Ok )
				if warning == QMessageBox.Ok:
					self.lineEdit.setText('0')
				if warning == QMessageBox.No:
					self.label.setText('sorry , you can\'t go further !')


app = QApplication(sys.argv)

w = window()

sys.exit(app.exec_())