# Form implementation generated from reading ui file 'SanPham.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import Dataconnection
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableView, QLineEdit, QPushButton
from NhapThemHangDialog import NhapThemHangDialog  # Import the dialog class

class Ui_DanhSachSanPham(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1483, 851)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(820, 10, 641, 231))
        self.groupBox.setObjectName("groupBox")
        self.btnThem = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnThem.setGeometry(QtCore.QRect(160, 10, 261, 51))
        self.btnThem.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnThem.setObjectName("btnThem")
        self.btnSua = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnSua.setGeometry(QtCore.QRect(160, 80, 261, 51))
        self.btnSua.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnSua.setObjectName("btnSua")
        self.btnXoa = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnXoa.setGeometry(QtCore.QRect(160, 160, 261, 51))
        self.btnXoa.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnXoa.setObjectName("btnXoa")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 310, 1461, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.tableView_SanPham = QtWidgets.QTableView(parent=self.frame)
        self.tableView_SanPham.setGeometry(QtCore.QRect(0, 20, 1461, 471))
        self.tableView_SanPham.setMaximumSize(QtCore.QSize(1461, 471))
        self.tableView_SanPham.setObjectName("tableView_SanPham")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 801, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(40, 40, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(410, 40, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(410, 100, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(410, 180, 101, 16))
        self.label_6.setObjectName("label_6")
        self.txtMaSanPham = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtMaSanPham.setGeometry(QtCore.QRect(160, 40, 161, 22))
        self.txtMaSanPham.setObjectName("txtMaSanPham")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label_8.setObjectName("label_8")
        self.txtTenSanPham = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtTenSanPham.setGeometry(QtCore.QRect(160, 110, 161, 22))
        self.txtTenSanPham.setObjectName("txtTenSanPham")
        self.txtMoTa = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtMoTa.setGeometry(QtCore.QRect(160, 180, 161, 22))
        self.txtMoTa.setObjectName("txtMoTa")
        self.txtGiaTien = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtGiaTien.setGeometry(QtCore.QRect(520, 30, 161, 22))
        self.txtGiaTien.setObjectName("txtGiaTien")
        self.txtSoluong = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtSoluong.setGeometry(QtCore.QRect(520, 100, 161, 22))
        self.txtSoluong.setObjectName("txtSoluong")
        self.comboBox_MaNhaCungCap = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.comboBox_MaNhaCungCap.setGeometry(QtCore.QRect(520, 180, 161, 22))
        self.comboBox_MaNhaCungCap.setObjectName("comboBox_MaNhaCungCap")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 260, 371, 41))
        self.label_7.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(880, 270, 101, 16))
        self.label_9.setObjectName("label_9")
        self.txtTimKiem = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtTimKiem.setGeometry(QtCore.QRect(990, 260, 161, 31))
        self.txtTimKiem.setObjectName("txtTimKiem")
        self.btnTimKiem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTimKiem.setGeometry(QtCore.QRect(1160, 260, 91, 31))
        self.btnTimKiem.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnTimKiem.setObjectName("btnTimKiem")
        self.btnLamMoi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLamMoi.setGeometry(QtCore.QRect(10, 250, 111, 41))
        self.btnLamMoi.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnLamMoi.setObjectName("btnLamMoi")
        self.btnNhapSP = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnNhapSP.setGeometry(QtCore.QRect(200, 250, 111, 41))
        self.btnNhapSP.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnNhapSP.setObjectName("btnNhapSP")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1483, 21))
        self.menubar.setObjectName("menubar")
        self.menuManager = QtWidgets.QMenu(parent=self.menubar)
        self.menuManager.setObjectName("menuManager")
        self.menuSetting = QtWidgets.QMenu(parent=self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHome = QtGui.QAction(parent=MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionSanPham = QtGui.QAction(parent=MainWindow)
        self.actionSanPham.setObjectName("actionSanPham")
        self.actionBanHang = QtGui.QAction(parent=MainWindow)
        self.actionBanHang.setObjectName("actionBanHang")
        self.actionNhanVien = QtGui.QAction(parent=MainWindow)
        self.actionNhanVien.setObjectName("actionNhanVien")
        self.actionNhaCungCap = QtGui.QAction(parent=MainWindow)
        self.actionNhaCungCap.setObjectName("actionNhaCungCap")
        self.actionThongKe = QtGui.QAction(parent=MainWindow)
        self.actionThongKe.setObjectName("actionThongKe")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLogout = QtGui.QAction(parent=MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.actionHoTro = QtGui.QAction(parent=MainWindow)
        self.actionHoTro.setObjectName("actionHoTro")
        self.menuManager.addAction(self.actionHome)
        self.menuManager.addAction(self.actionSanPham)
        self.menuManager.addAction(self.actionBanHang)
        self.menuManager.addAction(self.actionNhanVien)
        self.menuManager.addAction(self.actionNhaCungCap)
        self.menuManager.addAction(self.actionThongKe)
        self.menuSetting.addAction(self.actionExit)
        self.menuSetting.addAction(self.actionLogout)
        self.menuSetting.addAction(self.actionHoTro)
        self.menubar.addAction(self.menuManager.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
         # Khởi tạo model cho QTableView
        self.model = QtGui.QStandardItemModel()
        self.btnThem.clicked.connect(self.themSanPham)
        self.btnSua.clicked.connect(self.suaSanPham)
        self.btnXoa.clicked.connect(self.xoaSanPham)
       
      
        self.tableView_SanPham.clicked.connect(self.table_clicked)
        self.btnLamMoi.clicked.connect(self.lamMoi)
        self.btnTimKiem.clicked.connect(self.timKiemSanPham)
        self.btnNhapSP.clicked.connect(self.NhapMOISL)
       
        self.loadTableData()
        self.loadMaNCC()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản lý nông sản"))
        self.groupBox.setTitle(_translate("MainWindow", "Chức Năng"))
        self.btnThem.setText(_translate("MainWindow", "ThÊM NÔNG SẢN MỚI"))
        self.btnSua.setText(_translate("MainWindow", "SỬA THÔNG TIN "))
        self.btnXoa.setText(_translate("MainWindow", "XÓA NÔNG SẢN"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_2.setText(_translate("MainWindow", "Tên Sản Phẩm"))
        self.label_3.setText(_translate("MainWindow", "Mô Tả"))
        self.label_4.setText(_translate("MainWindow", "Giá Tiền"))
        self.label_5.setText(_translate("MainWindow", "Số Lượng"))
        self.label_6.setText(_translate("MainWindow", "Nhà Cung Cấp"))
        self.label_8.setText(_translate("MainWindow", "Mã Sản Phẩm"))
        self.label_7.setText(_translate("MainWindow", "DANH SÁCH NÔNG SẢN "))
        self.label_9.setText(_translate("MainWindow", "Nhập Nông Sản"))
        self.btnTimKiem.setText(_translate("MainWindow", "search"))
        self.btnLamMoi.setText(_translate("MainWindow", "Làm Mới"))
        self.btnNhapSP.setText(_translate("MainWindow", "Nhập Thêm SL"))
        self.menuManager.setTitle(_translate("MainWindow", "Manager"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionSanPham.setText(_translate("MainWindow", "SanPham"))
        self.actionBanHang.setText(_translate("MainWindow", "BanHang"))
        self.actionNhanVien.setText(_translate("MainWindow", "NhanVien"))
        self.actionNhaCungCap.setText(_translate("MainWindow", "NhaCungCap"))
        self.actionThongKe.setText(_translate("MainWindow", "ThongKe"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.actionHoTro.setText(_translate("MainWindow", "HoTro"))
    
    
    def loadTableData(self):
        try:
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SanPham")
            rows = cursor.fetchall()

            self.model.clear()
            self.model.setColumnCount(6)
            self.model.setHorizontalHeaderLabels(["Mã Sản Phẩm", "Tên Sản Phẩm", "Mô Tả", "Giá ", "Số Lượng","Nhà Cung Cấp"])
            
            for row_number, row_data in enumerate(rows):
                for column_number, data in enumerate(row_data):
                    item = QtGui.QStandardItem(str(data))
                    self.model.setItem(row_number, column_number, item)

            self.tableView_SanPham.setModel(self.model)
            header = self.tableView_SanPham.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.tableView_SanPham.verticalHeader().setDefaultSectionSize(55)
            conn.close()
        except Exception as e:
            print(f"Error loading data: {e}")
            
    def loadMaNCC(self):
        try:
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT MaNCC, TenNCC FROM NhaCungCap")
            rows = cursor.fetchall()
            conn.close()

            # Xóa danh sách cũ trong combobox
            self.comboBox_MaNhaCungCap.clear()

            # Thêm danh sách mã nhà cung cấp vào combobox
            for row in rows:
                maNCC = row[0]
                # tenNCC = row[1]
                self.comboBox_MaNhaCungCap.addItem(f"{maNCC}")

        except Exception as e:
            print(f"Lỗi khi tải danh sách mã nhà cung cấp: {e}")
            
    def themSanPham(self):
        try:
            maSP = int(self.txtMaSanPham.text())
            tenSP = self.txtTenSanPham.text()
            moTa = self.txtMoTa.text()
            gia = self.txtGiaTien.text()
            soLuong = self.txtSoluong.text()
            maNCC = int(self.comboBox_MaNhaCungCap.currentText())  # Chuyển đổi thành số nguyên

        # Kiểm tra các điều kiện
            if maSP == '' or tenSP == '' or moTa == '' or gia == '' or soLuong == '':
               QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin sản phẩm!")
               return

            gia = float(gia.replace(',', '.'))  # Chuyển đổi giá thành số

        # Thực hiện thêm vào cơ sở dữ liệu
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SanPham (MaSP, TenSP, MoTa, Gia, SoLuong, MaNCC) VALUES (%s, %s, %s, %s, %s, %s)",
                       (maSP, tenSP, moTa, gia, soLuong, maNCC))
            conn.commit()
            conn.close()

            self.loadTableData()
            self.lamMoi()
            QMessageBox.information(None, "Thông báo", "Thêm sản phẩm thành công!")
        except Exception as e:
            QMessageBox.warning(None, "Lỗi", f"Lỗi: {e}")

    def suaSanPham(self):
    # Sửa thông tin sản phẩm trong cơ sở dữ liệu
        try:
            maSP = int(self.txtMaSanPham.text())
            tenSP = self.txtTenSanPham.text()
            moTa = self.txtMoTa.text()
            gia = self.txtGiaTien.text()
            soLuong = self.txtSoluong.text()
            maNCC = int(self.comboBox_MaNhaCungCap.currentText())  # Chuyển đổi thành số nguyên

        # Kiểm tra các điều kiện
            if maSP == '' or tenSP == '' or moTa == '' or gia == '' or soLuong == '':
                QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin sản phẩm!")
                return

            gia = float(gia.replace(',', '.'))  # Chuyển đổi giá thành số

        # Thực hiện cập nhật vào cơ sở dữ liệu
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            cursor.execute("UPDATE SanPham SET TenSP=%s, MoTa=%s, Gia=%s, SoLuong=%s, MaNCC=%s WHERE MaSP=%s",
                       (tenSP, moTa, gia, soLuong, maNCC, maSP))
            conn.commit()
            conn.close()

            self.loadTableData()
            self.lamMoi()
            QMessageBox.information(None, "Thông báo", "Sửa thông tin sản phẩm thành công!")
        except Exception as e:
            QMessageBox.warning(None, "Lỗi", f"Lỗi: {e}")

    def xoaSanPham(self):
    # Xóa sản phẩm khỏi cơ sở dữ liệu
        maSP = int(self.txtMaSanPham.text())
        conn = Dataconnection.connectdatabase()
        try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM SanPham WHERE MaSP=%s", (maSP,))
                conn.commit()
                conn.close()

                self.loadTableData()
                self.lamMoi()
                QMessageBox.information(None, "Thông báo", "Xóa sản phẩm thành công!")
        except Exception as e:
                QMessageBox.warning(None, "Lỗi", f"Lỗi: {e}")


    def search_product(self):
        search_term = self.txtTimKiem.text()
        query = f"SELECT * FROM SanPham WHERE TenSP LIKE '%{search_term}%' OR MoTa LIKE '%{search_term}%'"
        
        connection = Dataconnection.connectdatabase()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            self.model.removeRows(0, self.model.rowCount())
            for row in records:
                items = [QtGui.QStandardItem(str(field)) for field in row]
                self.model.appendRow(items)
            cursor.close()
            Dataconnection.close_connection(connection)

    def table_clicked(self, index):
        row = index.row()
        self.txtMaSanPham.setText(self.model.item(row, 0).text())
        self.txtTenSanPham.setText(self.model.item(row, 1).text())
        self.txtMoTa.setText(self.model.item(row, 2).text())
        self.txtGiaTien.setText(self.model.item(row, 3).text())
        self.txtSoluong.setText(self.model.item(row, 4).text())
        self.comboBox_MaNhaCungCap.setCurrentText(self.model.item(row, 5).text()) 

    def lamMoi(self):
        try:
            self.clearFields()
            self.loadTableData()
            self.loadMaNCC()
        
        except Exception as e:
            print(f"Lỗi khi làm mới dữ liệu: {e}")
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi làm mới dữ liệu: {e}")

    def timKiemSanPham(self):
        try:
            keyword = self.txtTimKiem.text()
            
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM SanPham WHERE TenSP LIKE %s OR MaSP=%s", (f"%{keyword}%", keyword))
            rows = cursor.fetchall()
            
            self.model.clear()
            self.model.setColumnCount(6)
            self.model.setHorizontalHeaderLabels(["Mã Sản Phẩm", "Tên Sản Phẩm", "Mô Tả", "Giá ", "Số Lượng", "Nhà Cung Cấp"])
            
            for row_number, row_data in enumerate(rows):
                for column_number, data in enumerate(row_data):
                    item = QtGui.QStandardItem(str(data))
                    self.model.setItem(row_number, column_number, item)

            self.tableView_SanPham.setModel(self.model)
            header = self.tableView_SanPham.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.tableView_SanPham.verticalHeader().setDefaultSectionSize(55)
            conn.close()
        
        except Exception as e:
            print(f"Lỗi khi tìm kiếm sản phẩm: {e}")
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tìm kiếm sản phẩm: {e}")

    
    def clearFields(self):
        self.txtMaSanPham.clear()
        self.txtTenSanPham.clear()
        self.txtMoTa.clear()
        self.txtGiaTien.clear()
        self.txtSoluong.clear()
        self.comboBox_MaNhaCungCap.setCurrentIndex(0) 
        self.loadTableData()
        

    def NhapMOISL(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = NhapThemHangDialog()
        self.ui.setupUi(self.window)
        self.window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DanhSachSanPham()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())