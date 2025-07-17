"""
Create VM Dialog for setting up new virtual machines
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QComboBox, QSpinBox, QPushButton, QFrame, QFormLayout,
    QTextEdit, QCheckBox, QGroupBox, QSlider
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class CreateVMDialog(QDialog):
    """Dialog for creating new virtual machines"""
    
    vm_created = pyqtSignal(dict)  # VM configuration data
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Virtual Machine")
        self.setModal(True)
        self.setMinimumSize(500, 600)
        self.setup_ui()
        self.apply_style()
        
    def setup_ui(self):
        """Setup the dialog interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("Create New Virtual Machine")
        title.setObjectName("dialog-title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # VM Configuration Form
        form_group = QGroupBox("Virtual Machine Configuration")
        form_group.setObjectName("form-group")
        form_layout = QFormLayout(form_group)
        
        # VM Name
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter VM name (e.g., My NectarOS)")
        self.name_edit.setObjectName("form-input")
        form_layout.addRow("VM Name:", self.name_edit)
        
        # OS Template
        self.os_combo = QComboBox()
        self.os_combo.addItems(["NectarOS (Recommended)", "Custom Template"])
        self.os_combo.setObjectName("form-combo")
        form_layout.addRow("OS Template:", self.os_combo)
        
        # Memory
        self.memory_spin = QSpinBox()
        self.memory_spin.setRange(1, 32)
        self.memory_spin.setValue(2)
        self.memory_spin.setSuffix(" GB")
        self.memory_spin.setObjectName("form-spin")
        form_layout.addRow("Memory:", self.memory_spin)
        
        # Storage
        self.storage_spin = QSpinBox()
        self.storage_spin.setRange(10, 1000)
        self.storage_spin.setValue(20)
        self.storage_spin.setSuffix(" GB")
        self.storage_spin.setObjectName("form-spin")
        form_layout.addRow("Storage:", self.storage_spin)
        
        # CPU Cores
        self.cpu_spin = QSpinBox()
        self.cpu_spin.setRange(1, 16)
        self.cpu_spin.setValue(2)
        self.cpu_spin.setObjectName("form-spin")
        form_layout.addRow("CPU Cores:", self.cpu_spin)
        
        layout.addWidget(form_group)
        
        # NectarOS Features
        features_group = QGroupBox("NectarOS Features")
        features_group.setObjectName("form-group")
        features_layout = QVBoxLayout(features_group)
        
        # Feature checkboxes
        self.frosted_glass = QCheckBox("Enable Frosted Glass Effects")
        self.frosted_glass.setChecked(True)
        self.frosted_glass.setObjectName("feature-checkbox")
        features_layout.addWidget(self.frosted_glass)
        
        self.animations = QCheckBox("Enable Smooth Animations")
        self.animations.setChecked(True)
        self.animations.setObjectName("feature-checkbox")
        features_layout.addWidget(self.animations)
        
        self.essential_apps = QCheckBox("Include Essential Apps (Settings, File Manager)")
        self.essential_apps.setChecked(True)
        self.essential_apps.setObjectName("feature-checkbox")
        features_layout.addWidget(self.essential_apps)
        
        layout.addWidget(features_group)
        
        # Description
        desc_group = QGroupBox("Description")
        desc_group.setObjectName("form-group")
        desc_layout = QVBoxLayout(desc_group)
        
        self.desc_edit = QTextEdit()
        self.desc_edit.setPlaceholderText("Optional: Add a description for this VM...")
        self.desc_edit.setMaximumHeight(80)
        self.desc_edit.setObjectName("form-text")
        desc_layout.addWidget(self.desc_edit)
        
        layout.addWidget(desc_group)
        
        # Buttons
        buttons_layout = QHBoxLayout()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("dialog-button-cancel")
        cancel_btn.clicked.connect(self.reject)
        buttons_layout.addWidget(cancel_btn)
        
        buttons_layout.addStretch()
        
        create_btn = QPushButton("Create Virtual Machine")
        create_btn.setObjectName("dialog-button-create")
        create_btn.clicked.connect(self.create_vm)
        buttons_layout.addWidget(create_btn)
        
        layout.addLayout(buttons_layout)
        
    def apply_style(self):
        """Apply neumorphic styling to the dialog"""
        style = """
        QDialog {
            background: #1a1a1a;
            color: #ffffff;
            font-family: 'Segoe UI', 'SF Pro Display', 'Ubuntu', sans-serif;
        }
        
        #dialog-title {
            font-size: 24px;
            font-weight: bold;
            color: #4a9eff;
            margin-bottom: 20px;
        }
        
        #form-group {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #2a2a2a, stop:1 #3a3a3a);
            border: 1px solid #404040;
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            font-weight: bold;
            color: #ffffff;
        }
        
        #form-group::title {
            color: #4a9eff;
            font-size: 16px;
            font-weight: bold;
        }
        
        #form-input, #form-combo, #form-spin, #form-text {
            background: #1a1a1a;
            border: 1px solid #404040;
            border-radius: 8px;
            padding: 10px;
            color: #ffffff;
            font-size: 14px;
        }
        
        #form-input:focus, #form-combo:focus, #form-spin:focus, #form-text:focus {
            border-color: #4a9eff;
            outline: none;
        }
        
        #form-combo::drop-down {
            border: none;
        }
        
        #form-combo::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid #4a9eff;
        }
        
        #feature-checkbox {
            color: #b0b0b0;
            font-size: 14px;
            font-weight: normal;
            spacing: 10px;
        }
        
        #feature-checkbox::indicator {
            width: 18px;
            height: 18px;
            border: 2px solid #404040;
            border-radius: 4px;
            background: #1a1a1a;
        }
        
        #feature-checkbox::indicator:checked {
            background: #4a9eff;
            border-color: #4a9eff;
        }
        
        #dialog-button-cancel {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #3a3a3a, stop:1 #2a2a2a);
            border: 1px solid #404040;
            border-radius: 10px;
            padding: 12px 24px;
            color: #ffffff;
            font-size: 14px;
            font-weight: 500;
        }
        
        #dialog-button-cancel:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #f87171, stop:1 #e86161);
            border-color: #f87171;
        }
        
        #dialog-button-create {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #4ade80, stop:1 #3ade70);
            border: none;
            border-radius: 10px;
            padding: 12px 24px;
            color: white;
            font-size: 14px;
            font-weight: bold;
        }
        
        #dialog-button-create:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #5aee90, stop:1 #4ade80);
        }
        """
        self.setStyleSheet(style)
        
    def create_vm(self):
        """Create the virtual machine with current settings"""
        if not self.name_edit.text().strip():
            # TODO: Show error message
            return
            
        vm_config = {
            "name": self.name_edit.text().strip(),
            "os_template": self.os_combo.currentText(),
            "memory": self.memory_spin.value(),
            "storage": self.storage_spin.value(),
            "cpu_cores": self.cpu_spin.value(),
            "description": self.desc_edit.toPlainText(),
            "features": {
                "frosted_glass": self.frosted_glass.isChecked(),
                "animations": self.animations.isChecked(),
                "essential_apps": self.essential_apps.isChecked()
            }
        }
        
        self.vm_created.emit(vm_config)
        self.accept() 