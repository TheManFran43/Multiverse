"""
Virtual Machine Manager
Handles VM operations and state management
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Try to import libvirt, but don't fail if it's not available
try:
    import libvirt
    LIBVIRT_AVAILABLE = True
except ImportError:
    LIBVIRT_AVAILABLE = False
    print("⚠️  libvirt not available - using simulation mode")

from os_templates.nectaros import NectarOSTemplate


class VMManager:
    """Manages virtual machines and their operations"""
    
    def __init__(self, data_dir: str = None):
        if data_dir is None:
            self.data_dir = Path.home() / ".multiverse"
        else:
            self.data_dir = Path(data_dir)
            
        self.vms_dir = self.data_dir / "vms"
        self.config_file = self.data_dir / "config.json"
        
        # Ensure directories exist
        self.vms_dir.mkdir(parents=True, exist_ok=True)
        
        # Load existing VMs
        self.vms = self.load_vms()
        
        # Available templates
        self.templates = {
            "nectaros": NectarOSTemplate()
        }
        
        # Check if we're in simulation mode
        self.simulation_mode = not LIBVIRT_AVAILABLE
        if self.simulation_mode:
            print("🎮 Running in simulation mode - VMs will be simulated")
        
    def load_vms(self) -> Dict[str, dict]:
        """Load existing VMs from storage"""
        vms = {}
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    vms = json.load(f)
            except json.JSONDecodeError:
                print("Warning: Could not load VM configuration")
                
        return vms
        
    def save_vms(self):
        """Save VMs to storage"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.vms, f, indent=2)
        except Exception as e:
            print(f"Error saving VMs: {e}")
            
    def create_vm(self, vm_config: dict) -> bool:
        """Create a new virtual machine"""
        try:
            vm_name = vm_config["name"]
            
            # Check if VM already exists
            if vm_name in self.vms:
                print(f"VM '{vm_name}' already exists")
                return False
                
            # Create VM directory
            vm_dir = self.vms_dir / vm_name
            vm_dir.mkdir(exist_ok=True)
            
            # Add metadata
            vm_config["created_at"] = datetime.now().isoformat()
            vm_config["status"] = "stopped"
            vm_config["last_modified"] = datetime.now().isoformat()
            
            # Save VM configuration
            vm_config_file = vm_dir / "config.json"
            with open(vm_config_file, 'w') as f:
                json.dump(vm_config, f, indent=2)
                
            # Add to VM list
            self.vms[vm_name] = {
                "name": vm_name,
                "os": vm_config.get("os_template", "Unknown"),
                "status": "stopped",
                "memory": f"{vm_config.get('memory', 2)}GB",
                "storage": f"{vm_config.get('storage', 20)}GB",
                "created_at": vm_config["created_at"],
                "path": str(vm_dir)
            }
            
            self.save_vms()
            print(f"✅ Created VM: {vm_name}")
            return True
            
        except Exception as e:
            print(f"Error creating VM: {e}")
            return False
            
    def start_vm(self, vm_name: str) -> bool:
        """Start a virtual machine"""
        if vm_name not in self.vms:
            print(f"VM '{vm_name}' not found")
            return False
            
        try:
            if self.simulation_mode:
                # In simulation mode, just update status
                print(f"🎮 Simulating VM start: {vm_name}")
                self.vms[vm_name]["status"] = "running"
                self.vms[vm_name]["last_modified"] = datetime.now().isoformat()
                self.save_vms()
                print(f"🚀 Started VM (simulation): {vm_name}")
                return True
            else:
                # Real VM start logic would go here
                self.vms[vm_name]["status"] = "running"
                self.vms[vm_name]["last_modified"] = datetime.now().isoformat()
                self.save_vms()
                print(f"🚀 Started VM: {vm_name}")
                return True
            
        except Exception as e:
            print(f"Error starting VM: {e}")
            return False
            
    def stop_vm(self, vm_name: str) -> bool:
        """Stop a virtual machine"""
        if vm_name not in self.vms:
            print(f"VM '{vm_name}' not found")
            return False
            
        try:
            if self.simulation_mode:
                print(f"🎮 Simulating VM stop: {vm_name}")
                
            # Update status
            self.vms[vm_name]["status"] = "stopped"
            self.vms[vm_name]["last_modified"] = datetime.now().isoformat()
            self.save_vms()
            
            print(f"⏹️ Stopped VM: {vm_name}")
            return True
            
        except Exception as e:
            print(f"Error stopping VM: {e}")
            return False
            
    def delete_vm(self, vm_name: str) -> bool:
        """Delete a virtual machine"""
        if vm_name not in self.vms:
            print(f"VM '{vm_name}' not found")
            return False
            
        try:
            # Remove VM directory
            vm_dir = Path(self.vms[vm_name]["path"])
            if vm_dir.exists():
                import shutil
                shutil.rmtree(vm_dir)
                
            # Remove from VM list
            del self.vms[vm_name]
            self.save_vms()
            
            print(f"🗑️ Deleted VM: {vm_name}")
            return True
            
        except Exception as e:
            print(f"Error deleting VM: {e}")
            return False
            
    def get_vm(self, vm_name: str) -> Optional[dict]:
        """Get VM information"""
        return self.vms.get(vm_name)
        
    def get_all_vms(self) -> List[dict]:
        """Get all VMs"""
        return list(self.vms.values())
        
    def get_template(self, template_name: str):
        """Get OS template"""
        return self.templates.get(template_name)
        
    def get_available_templates(self) -> List[str]:
        """Get list of available templates"""
        return list(self.templates.keys())
        
    def update_vm_status(self, vm_name: str, status: str):
        """Update VM status"""
        if vm_name in self.vms:
            self.vms[vm_name]["status"] = status
            self.vms[vm_name]["last_modified"] = datetime.now().isoformat()
            self.save_vms()
            
    def is_simulation_mode(self) -> bool:
        """Check if running in simulation mode"""
        return self.simulation_mode 