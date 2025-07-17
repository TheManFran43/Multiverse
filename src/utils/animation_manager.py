"""
Animation Manager for Multiverse
Provides smooth, springy animations for UI components
"""

from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, QParallelAnimationGroup, QSequentialAnimationGroup
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
import math


class AnimationManager:
    """Manages smooth animations for UI components"""
    
    def __init__(self):
        self.active_animations = []
        
    def spring_scale(self, widget: QWidget, scale_factor: float = 1.05, duration: int = 300):
        """Apply springy scale animation to widget"""
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(duration)
        
        # Spring easing curve
        curve = QEasingCurve(QEasingCurve.Type.OutBack)
        curve.setOvershoot(0.7)  # Spring overshoot
        animation.setEasingCurve(curve)
        
        # Calculate new geometry with scale
        current_rect = widget.geometry()
        center_x = current_rect.center().x()
        center_y = current_rect.center().y()
        
        new_width = int(current_rect.width() * scale_factor)
        new_height = int(current_rect.height() * scale_factor)
        new_x = center_x - new_width // 2
        new_y = center_y - new_height // 2
        
        animation.setStartValue(current_rect)
        animation.setEndValue(widget.geometry().adjusted(
            new_x - current_rect.x(),
            new_y - current_rect.y(),
            new_width - current_rect.width(),
            new_height - current_rect.height()
        ))
        
        animation.start()
        self.active_animations.append(animation)
        return animation
        
    def fade_in(self, widget: QWidget, duration: int = 400):
        """Fade in animation"""
        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(duration)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        
        curve = QEasingCurve(QEasingCurve.Type.OutCubic)
        animation.setEasingCurve(curve)
        
        animation.start()
        self.active_animations.append(animation)
        return animation
        
    def slide_in(self, widget: QWidget, direction: str = "left", duration: int = 500):
        """Slide in animation from specified direction"""
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(duration)
        
        current_rect = widget.geometry()
        start_rect = current_rect
        
        if direction == "left":
            start_rect.moveLeft(current_rect.x() - current_rect.width())
        elif direction == "right":
            start_rect.moveLeft(current_rect.x() + current_rect.width())
        elif direction == "up":
            start_rect.moveTop(current_rect.y() - current_rect.height())
        elif direction == "down":
            start_rect.moveTop(current_rect.y() + current_rect.height())
            
        animation.setStartValue(start_rect)
        animation.setEndValue(current_rect)
        
        curve = QEasingCurve(QEasingCurve.Type.OutBack)
        curve.setOvershoot(0.3)
        animation.setEasingCurve(curve)
        
        animation.start()
        self.active_animations.append(animation)
        return animation
        
    def bounce(self, widget: QWidget, intensity: float = 0.1, duration: int = 600):
        """Bounce animation"""
        group = QSequentialAnimationGroup()
        
        # Scale up
        scale_up = QPropertyAnimation(widget, b"geometry")
        scale_up.setDuration(duration // 3)
        scale_up.setStartValue(widget.geometry())
        
        current_rect = widget.geometry()
        center_x = current_rect.center().x()
        center_y = current_rect.center().y()
        
        new_width = int(current_rect.width() * (1 + intensity))
        new_height = int(current_rect.height() * (1 + intensity))
        new_x = center_x - new_width // 2
        new_y = center_y - new_height // 2
        
        scale_up.setEndValue(widget.geometry().adjusted(
            new_x - current_rect.x(),
            new_y - current_rect.y(),
            new_width - current_rect.width(),
            new_height - current_rect.height()
        ))
        
        curve = QEasingCurve(QEasingCurve.Type.OutBack)
        curve.setOvershoot(0.5)
        scale_up.setEasingCurve(curve)
        
        # Scale down
        scale_down = QPropertyAnimation(widget, b"geometry")
        scale_down.setDuration(duration // 3)
        scale_down.setStartValue(scale_up.endValue())
        scale_down.setEndValue(widget.geometry())
        
        curve2 = QEasingCurve(QEasingCurve.Type.InOutQuad)
        scale_down.setEasingCurve(curve2)
        
        # Final settle
        settle = QPropertyAnimation(widget, b"geometry")
        settle.setDuration(duration // 3)
        settle.setStartValue(widget.geometry())
        settle.setEndValue(widget.geometry())
        
        curve3 = QEasingCurve(QEasingCurve.Type.OutElastic)
        curve3.setPeriod(0.3)
        settle.setEasingCurve(curve3)
        
        group.addAnimation(scale_up)
        group.addAnimation(scale_down)
        group.addAnimation(settle)
        
        group.start()
        self.active_animations.append(group)
        return group
        
    def pulse(self, widget: QWidget, cycles: int = 3, duration: int = 1000):
        """Pulse animation with multiple cycles"""
        group = QSequentialAnimationGroup()
        
        for i in range(cycles):
            # Scale up
            scale_up = QPropertyAnimation(widget, b"geometry")
            scale_up.setDuration(duration // (cycles * 2))
            
            current_rect = widget.geometry()
            center_x = current_rect.center().x()
            center_y = current_rect.center().y()
            
            scale_factor = 1.0 + (0.05 * (1 - i / cycles))  # Decreasing intensity
            new_width = int(current_rect.width() * scale_factor)
            new_height = int(current_rect.height() * scale_factor)
            new_x = center_x - new_width // 2
            new_y = center_y - new_height // 2
            
            scale_up.setStartValue(current_rect)
            scale_up.setEndValue(widget.geometry().adjusted(
                new_x - current_rect.x(),
                new_y - current_rect.y(),
                new_width - current_rect.width(),
                new_height - current_rect.height()
            ))
            
            # Scale down
            scale_down = QPropertyAnimation(widget, b"geometry")
            scale_down.setDuration(duration // (cycles * 2))
            scale_down.setStartValue(scale_up.endValue())
            scale_down.setEndValue(current_rect)
            
            group.addAnimation(scale_up)
            group.addAnimation(scale_down)
            
        group.start()
        self.active_animations.append(group)
        return group
        
    def ripple_effect(self, widget: QWidget, center_point=None):
        """Create a ripple effect from a center point"""
        if center_point is None:
            center_point = widget.rect().center()
            
        # Create a temporary overlay for the ripple
        overlay = RippleOverlay(widget)
        overlay.show_ripple(center_point)
        
        # Clean up after animation
        QTimer.singleShot(1000, overlay.deleteLater)
        
    def stagger_children(self, parent_widget: QWidget, animation_type: str = "fade_in", delay: int = 100):
        """Animate child widgets with staggered timing"""
        children = parent_widget.findChildren(QWidget)
        animations = []
        
        for i, child in enumerate(children):
            if child != parent_widget:
                timer = QTimer()
                timer.setSingleShot(True)
                timer.timeout.connect(lambda c=child: self._animate_child(c, animation_type))
                timer.start(i * delay)
                animations.append(timer)
                
        return animations
        
    def _animate_child(self, child: QWidget, animation_type: str):
        """Animate a single child widget"""
        if animation_type == "fade_in":
            self.fade_in(child, 300)
        elif animation_type == "slide_in":
            self.slide_in(child, "up", 400)
        elif animation_type == "bounce":
            self.bounce(child, 0.1, 500)
            
    def cleanup(self):
        """Clean up all active animations"""
        for animation in self.active_animations:
            if animation.state() == QPropertyAnimation.State.Running:
                animation.stop()
        self.active_animations.clear()


class RippleOverlay(QWidget):
    """Overlay widget for ripple effects"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(QWidget.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(QWidget.WidgetAttribute.WA_TranslucentBackground)
        self.ripple_center = None
        self.ripple_radius = 0
        self.ripple_alpha = 255
        
    def show_ripple(self, center_point):
        """Show ripple animation"""
        self.ripple_center = center_point
        self.ripple_radius = 0
        self.ripple_alpha = 255
        
        # Animate ripple
        self.ripple_animation = QPropertyAnimation(self, b"ripple_radius")
        self.ripple_animation.setDuration(1000)
        self.ripple_animation.setStartValue(0)
        self.ripple_animation.setEndValue(100)
        
        curve = QEasingCurve(QEasingCurve.Type.OutCubic)
        self.ripple_animation.setEasingCurve(curve)
        
        self.ripple_animation.valueChanged.connect(self.update)
        self.ripple_animation.start()
        
    def paintEvent(self, event):
        """Paint the ripple effect"""
        if self.ripple_center and self.ripple_radius > 0:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            # Calculate alpha based on radius
            alpha = max(0, 255 - (self.ripple_radius * 2))
            
            # Create ripple color
            ripple_color = QColor(74, 158, 255, alpha)  # Blue with transparency
            
            # Draw ripple circle
            painter.setPen(QPen(ripple_color, 2))
            painter.setBrush(ripple_color)
            painter.drawEllipse(self.ripple_center, self.ripple_radius, self.ripple_radius)
            
    @property
    def ripple_radius(self):
        return self._ripple_radius
        
    @ripple_radius.setter
    def ripple_radius(self, value):
        self._ripple_radius = value
        self.update() 