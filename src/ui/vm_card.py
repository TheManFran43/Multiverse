"""
VM Card component for displaying virtual machine information
"""

from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QProgressBar
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QFont

from utils.animation_manager import AnimationManager


class VMCard(QFrame):
    """Card component for displaying VM information"""
    
    # Signals
    start_clicked = pyqtSignal(str)  # VM name
    stop_clicked = pyqtSignal(str)
    settings_clicked = pyqtSignal(str)
    
    def __init__(self, vm_data):
        super().__init__()
        self.vm_data = vm_data
        self.animation_manager = AnimationManager()
        self.setup_ui()
        self.apply_style()
        
        # Add hover animations
        self.setup_animations()
        
    def setup_ui(self):
        """Setup the VM card interface"""
        self.setObjectName("vm-card")
        self.setMinimumSize(300, 200)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Header with name and status
        header = QHBoxLayout()
        
        # VM name
        name_label = QLabel(self.vm_data["name"])
        name_label.setObjectName("vm-name")
        header.addWidget(name_label)
        
        header.addStretch()
        
        # Status indicator
        status_label = QLabel(self.vm_data["status"].title())
        status_label.setObjectName(f"vm-status-{self.vm_data['status']}")
        header.addWidget(status_label)
        
        layout.addLayout(header)
        
        # OS info
        os_label = QLabel(f"OS: {self.vm_data['os']}")
        os_label.setObjectName("vm-os")
        layout.addWidget(os_label)
        
        # Resource info
        resources_layout = QHBoxLayout()
        
        # Memory
        memory_label = QLabel(f"Memory: {self.vm_data['memory']}")
        memory_label.setObjectName("vm-resource")
        resources_layout.addWidget(memory_label)
        
        # Storage
        storage_label = QLabel(f"Storage: {self.vm_data['storage']}")
        storage_label.setObjectName("vm-resource")
        resources_layout.addWidget(storage_label)
        
        layout.addLayout(resources_layout)
        
        # Progress bar for resource usage (placeholder)
        progress = QProgressBar()
        progress.setObjectName("vm-progress")
        progress.setValue(65)  # Example value
        progress.setFormat("CPU: 65%")
        layout.addWidget(progress)
        
        # Action buttons
        buttons_layout = QHBoxLayout()
        
        if self.vm_data["status"] == "running":
            stop_btn = QPushButton("⏹️ Stop")
            stop_btn.setObjectName("vm-stop-button")
            stop_btn.clicked.connect(lambda: self.stop_clicked.emit(self.vm_data["name"]))
            buttons_layout.addWidget(stop_btn)
        else:
            start_btn = QPushButton("▶️ Start")
            start_btn.setObjectName("vm-start-button")
            start_btn.clicked.connect(lambda: self.start_clicked.emit(self.vm_data["name"]))
            buttons_layout.addWidget(start_btn)
        
        settings_btn = QPushButton("⚙️ Settings")
        settings_btn.setObjectName("vm-settings-button")
        settings_btn.clicked.connect(lambda: self.settings_clicked.emit(self.vm_data["name"]))
        buttons_layout.addWidget(settings_btn)
        
        layout.addLayout(buttons_layout)
        
    def apply_style(self):
        """Apply neumorphic styling to the VM card"""
        style = """
        #vm-card {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #2a2a2a, stop:1 #3a3a3a);
            border: 1px solid #404040;
            border-radius: 15px;
            box-shadow: 3px 3px 10px #0a0a0a,
                        -3px -3px 10px #4a4a4a;
        }
        
        #vm-card:hover {
            box-shadow: 5px 5px 15px #0a0a0a,
                        -5px -5px 15px #4a4a4a;
        }
        
        #vm-name {
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
        }
        
        #vm-os {
            font-size: 14px;
            color: #b0b0b0;
        }
        
        #vm-resource {
            font-size: 12px;
            color: #808080;
        }
        
        #vm-status-running {
            color: #4ade80;
            font-weight: bold;
            font-size: 12px;
        }
        
        #vm-status-stopped {
            color: #f87171;
            font-weight: bold;
            font-size: 12px;
        }
        
        #vm-status-paused {
            color: #fbbf24;
            font-weight: bold;
            font-size: 12px;
        }
        
        #vm-progress {
            background: #1a1a1a;
            border: 1px solid #404040;
            border-radius: 8px;
            text-align: center;
            color: #ffffff;
        }
        
        #vm-progress::chunk {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #4a9eff, stop:1 #5aaeff);
            border-radius: 7px;
        }
        
        #vm-start-button, #vm-stop-button, #vm-settings-button {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #3a3a3a, stop:1 #2a2a2a);
            border: 1px solid #404040;
            border-radius: 8px;
            padding: 8px 12px;
            color: #ffffff;
            font-size: 12px;
            font-weight: 500;
        }
        
        #vm-start-button:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #4ade80, stop:1 #3ade70);
            border-color: #4ade80;
        }
        
        #vm-stop-button:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #f87171, stop:1 #e86161);
            border-color: #f87171;
        }
        
        #vm-settings-button:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #4a9eff, stop:1 #3a8eef);
            border-color: #4a9eff;
        }
        """
        self.setStyleSheet(style)
        
    def setup_animations(self):
        """Setup hover and click animations"""
        # Add hover effect
        self.enterEvent = self.on_enter
        self.leaveEvent = self.on_leave
        
        # Add click animations to buttons
        for button in self.findChildren(QPushButton):
            button.clicked.connect(self.on_button_click)
            
    def on_enter(self, event):
        """Handle mouse enter event"""
        self.animation_manager.spring_scale(self, 1.02, 200)
        
    def on_leave(self, event):
        """Handle mouse leave event"""
        self.animation_manager.spring_scale(self, 1.0, 200)
        
    def on_button_click(self):
        """Handle button click with animation"""
        sender = self.sender()
        if sender:
            self.animation_manager.bounce(sender, 0.15, 300) 