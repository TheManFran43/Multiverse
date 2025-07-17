"""
Main window for Multiverse application
Dark neumorphic design with VM management interface
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QScrollArea, QFrame, QGridLayout,
    QStackedWidget, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize, pyqtSignal, QTimer
from PyQt6.QtGui import QFont, QPalette, QColor, QPixmap

from ui.vm_card import VMCard
from ui.create_vm_dialog import CreateVMDialog
from ui.neumorphic_style import NeumorphicStyle
from utils.animation_manager import AnimationManager


class MainWindow(QMainWindow):
    """Main application window with dark neumorphic design"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiverse - Virtual OS Hub")
        self.setMinimumSize(1200, 800)
        
        # Initialize animation manager
        self.animation_manager = AnimationManager()
        
        self.setup_ui()
        self.apply_neumorphic_style()
        
        # Start entrance animations
        QTimer.singleShot(100, self.start_entrance_animations)
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # Main content area
        content_area = self.create_content_area()
        main_layout.addWidget(content_area, 1)
        
    def create_sidebar(self):
        """Create the sidebar with navigation"""
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setObjectName("sidebar")
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(15)
        
        # Logo/title
        title = QLabel("Multiverse")
        title.setObjectName("app-title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Navigation buttons
        nav_buttons = [
            ("🏠 Dashboard", "dashboard"),
            ("🖥️ Virtual Machines", "vms"),
            ("📦 Templates", "templates"),
            ("⚙️ Settings", "settings"),
            ("❓ Help", "help")
        ]
        
        for text, action in nav_buttons:
            btn = QPushButton(text)
            btn.setObjectName("nav-button")
            btn.clicked.connect(lambda checked, a=action: self.navigate_to(a))
            layout.addWidget(btn)
        
        layout.addStretch()
        
        # Create VM button
        create_btn = QPushButton("➕ Create New VM")
        create_btn.setObjectName("create-vm-button")
        create_btn.clicked.connect(self.show_create_vm_dialog)
        
        # Add click handler
        create_btn.clicked.connect(self.show_create_vm_dialog)
        
        layout.addWidget(create_btn)
        
        return sidebar
        
    def create_content_area(self):
        """Create the main content area"""
        content = QFrame()
        content.setObjectName("content-area")
        
        layout = QVBoxLayout(content)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Header
        header = QLabel("Dashboard")
        header.setObjectName("content-header")
        layout.addWidget(header)
        
        # Scrollable content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setObjectName("content-scroll")
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(20, 20, 20, 20)
        scroll_layout.setSpacing(20)
        
        # Welcome section
        welcome = self.create_welcome_section()
        scroll_layout.addWidget(welcome)
        
        # Quick actions
        quick_actions = self.create_quick_actions()
        scroll_layout.addWidget(quick_actions)
        
        # VM grid
        vm_grid = self.create_vm_grid()
        scroll_layout.addWidget(vm_grid)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        return content
        
    def create_welcome_section(self):
        """Create welcome section"""
        welcome = QFrame()
        welcome.setObjectName("welcome-section")
        welcome.setMinimumHeight(150)
        
        layout = QVBoxLayout(welcome)
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Welcome to Multiverse! 🌟")
        title.setObjectName("welcome-title")
        layout.addWidget(title)
        
        subtitle = QLabel("Create and manage your virtual operating system environments")
        subtitle.setObjectName("welcome-subtitle")
        layout.addWidget(subtitle)
        
        return welcome
        
    def create_quick_actions(self):
        """Create quick actions section"""
        actions = QFrame()
        actions.setObjectName("quick-actions")
        
        layout = QVBoxLayout(actions)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        title = QLabel("Quick Actions")
        title.setObjectName("section-title")
        layout.addWidget(title)
        
        # Action buttons grid
        grid = QGridLayout()
        grid.setSpacing(15)
        
        action_buttons = [
            ("🚀 Launch NectarOS", "launch-nectaros"),
            ("📦 Install Template", "install-template"),
            ("⚙️ VM Settings", "vm-settings"),
            ("📊 System Monitor", "system-monitor")
        ]
        
        for i, (text, action) in enumerate(action_buttons):
            btn = QPushButton(text)
            btn.setObjectName("quick-action-button")
            btn.clicked.connect(lambda checked, a=action: self.handle_quick_action(a))
            grid.addWidget(btn, i // 2, i % 2)
            
        layout.addLayout(grid)
        return actions
        
    def create_vm_grid(self):
        """Create virtual machine grid"""
        vm_section = QFrame()
        vm_section.setObjectName("vm-section")
        
        layout = QVBoxLayout(vm_section)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        title = QLabel("Your Virtual Machines")
        title.setObjectName("section-title")
        layout.addWidget(title)
        
        # VM cards grid
        grid = QGridLayout()
        grid.setSpacing(20)
        
        # Sample VM cards (will be populated dynamically)
        sample_vms = [
            {
                "name": "NectarOS Demo",
                "os": "NectarOS",
                "status": "running",
                "memory": "2GB",
                "storage": "20GB"
            },
            {
                "name": "Test Environment",
                "os": "NectarOS",
                "status": "stopped",
                "memory": "1GB",
                "storage": "10GB"
            }
        ]
        
        for i, vm_data in enumerate(sample_vms):
            vm_card = VMCard(vm_data)
            grid.addWidget(vm_card, i // 2, i % 2)
            
        layout.addLayout(grid)
        return vm_section
        
    def apply_neumorphic_style(self):
        """Apply neumorphic styling"""
        style = NeumorphicStyle()
        self.setStyleSheet(style.get_main_window_style())
        
    def navigate_to(self, section):
        """Navigate to different sections"""
        print(f"Navigating to: {section}")
        
        # Update content header
        header = self.findChild(QLabel, "content-header")
        if header:
            if section == "dashboard":
                header.setText("Dashboard")
            elif section == "vms":
                header.setText("Virtual Machines")
            elif section == "templates":
                header.setText("OS Templates")
            elif section == "settings":
                header.setText("Settings")
            elif section == "help":
                header.setText("Help")
                
        # TODO: Implement full navigation logic with stacked widget
        
    def show_create_vm_dialog(self):
        """Show create VM dialog"""
        dialog = CreateVMDialog(self)
        dialog.exec()
        
    def start_entrance_animations(self):
        """Start entrance animations for the UI"""
        # Simple fade in
        self.setWindowOpacity(0.0)
        QTimer.singleShot(100, lambda: self.setWindowOpacity(1.0))
            
    def handle_quick_action(self, action):
        """Handle quick action button clicks"""
        print(f"Quick action: {action}")
        
        # Simple button feedback
        sender = self.sender()
        if sender:
            print(f"Button clicked: {sender.text()}")
            
        # Implement quick actions
        if action == "launch-nectaros":
            self.show_create_vm_dialog()
        elif action == "install-template":
            print("📦 Template installation dialog would open here")
        elif action == "vm-settings":
            print("⚙️ VM settings dialog would open here")
        elif action == "system-monitor":
            print("📊 System monitor would open here") 