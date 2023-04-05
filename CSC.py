#!/usr/bin/env python
# coding: utf-8

# In[16]:


import time
import numpy as np
import cv2
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal

class WallhackSettings:
def init(self, low_hsv, high_hsv, show_walls, bunny_hop):
self.low_hsv = low_hsv
self.high_hsv = high_hsv
self.show_walls = show_walls
self.bunny_hop = bunny_hop

class WallhackThread(QThread):
# Define a signal that emits a boolean value when the thread finishes processing
finished = pyqtSignal(bool)
def __init__(self, settings, parent=None):
    super().__init__(parent)
    self._stopped = False
    self.settings = settings
    self.output_image = None

def run(self):
    with ImageGrab.grab() as img:
        width, height = img.size

    while not self._stopped:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('w'):
            self.settings.show_walls = not self.settings.show_walls
            print("Showing walls" if self.settings.show_walls else "Hiding walls")

        if cv2.waitKey(1) & 0xFF == ord('e'):
            self.settings.bunny_hop = not self.settings.bunny_hop
            print("Bunny hop enabled" if self.settings.bunny_hop else "Bunny hop disabled")

        img = np.array(ImageGrab.grab(bbox=(0, 0, width, height)))

        edges = cv2.Canny(img, 50, 150)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.settings.low_hsv, self.settings.high_hsv)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if self.settings.show_walls:
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if self.settings.bunny_hop:
            # Perform bunny hop logic here
            pass

        self.output_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    self.finished.emit(True)
import time
import numpy as np
import cv2
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal

class WallhackSettings:
def init(self, low_hsv, high_hsv, show_walls, bunny_hop):
self.low_hsv = low_hsv
self.high_hsv = high_hsv
self.show_walls = show_walls
self.bunny_hop = bunny_hop

class WallhackThread(QThread):
# Define a signal that emits a boolean value when the thread finishes processing
finished = pyqtSignal(bool)

python
Copy code
def __init__(self, settings, parent=None):
    super().__init__(parent)
    self._stopped = False
    self.settings = settings
    self.output_image = None

def run(self):
    with ImageGrab.grab() as img:
        width, height = img.size

    while not self._stopped:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('w'):
            self.settings.show_walls = not self.settings.show_walls
            print("Showing walls" if self.settings.show_walls else "Hiding walls")

        if cv2.waitKey(1) & 0xFF == ord('e'):
            self.settings.bunny_hop = not self.settings.bunny_hop
            print("Bunny hop enabled" if self.settings.bunny_hop else "Bunny hop disabled")

        img = np.array(ImageGrab.grab(bbox=(0, 0, width, height)))

        edges = cv2.Canny(img, 50, 150)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.settings.low_hsv, self.settings.high_hsv)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if self.settings.show_walls:
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if self.settings.bunny_hop:
            # Perform bunny hop logic here
            pass

        self.output_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    self.finished.emit(True)
class Wallhack(QWidget):
def init(self):
super().init()
self.settings = WallhackSettings(
low_hsv=np.array([20, 50, 50]),
high_hsv=np.array([30, 255, 255]),
show_walls=True,
bunny_hop=False
)
self.init_ui()
def init_ui(self):
    # Create a label widget to display the wallhack output
    self.wallhack_label = QLabel(self)
    self.wallhack_label.setAlignment(Qt.AlignCenter)
    self.wallhack_label.setFixedSize(640, 480)

    # Create a button to start and stop the wallhack thread
    self.start_stop_button = QPushButton("Stop Wallhack", self)
    self.start_stop_button.setFixedSize(120, 40)
    self.start_stop_button.clicked.connect(self.toggle_wallhack_thread)

    # Create a button to toggle bunny hop
    self.bunny_hop_button = QPushButton("Enable Bunny Hop", self)
    self.bunny_hop_button.setFixedSize(120, 40)
class Wallhack(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = WallhackSettings(
            low_hsv=np.array([20, 50, 50]),
            high_hsv=np.array([30, 255, 255]),
            show_walls=True,
            bunny_hop=False
        )
        self.init_ui()

    def init_ui(self):
        # Create a label widget to display the wallhack output
        self.wallhack_label = QLabel(self)
        self.wallhack_label.setAlignment(Qt.AlignCenter)
        self.wallhack_label.setMinimumSize(640, 480)

        # Create a start button to start the wallhack thread
        self.start_button = QPushButton('Start Wallhack', self)
        self.start_button.clicked.connect(self.start_wallhack_thread)

        # Create a stop button to stop the wallhack thread
        self.stop_button = QPushButton('Stop Wallhack', self)
        self.stop_button.clicked.connect(self.stop_wallhack_thread)
        self.stop_button.setEnabled(False)

        # Create a vbox layout and add the label and buttons to it
        vbox = QVBoxLayout()
        vbox.addWidget(self.wallhack_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)

        # Set the main layout of the window to the vbox layout
        self.setLayout(vbox)

        # Create a timer to update the label with the wallhack output
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_wallhack_label)

        # Create the wallhack thread and connect its finished signal to a slot that stops the timer and buttons
        self.wallhack_thread = WallhackThread(self.settings)
        self.wallhack_thread.finished.connect(self.wallhack_thread_finished)

    def start_wallhack_thread(self):
        # Start the wallhack thread and the timer
        self.wallhack_thread.start()
        self.timer.start(16)

        # Enable the stop button and disable the start button
        self.stop_button.setEnabled(True)
        self.start_button.setEnabled(False)

    def stop_wallhack_thread(self):
        # Stop the wallhack thread and the timer
        self.wallhack_thread._stopped = True
        self.timer.stop()

        # Disable the stop button and enable the start button
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)

    def update_wallhack_label(self):
        # Check if there is a new output image from the wallhack thread and update the label with it
        if self.wallhack_thread.output_image is not None:
            qimage = QImage(
                self.wallhack_thread.output_image.data,
                self.wallhack_thread.output_image.shape[1],
                self.wallhack_thread.output_image.shape[0],
                self.wallhack_thread.output_image.shape[1] * 3,
                QImage.Format_RGB888
            )
            pixmap = QPixmap(qimage)
            self.wallhack_label.setPixmap(pixmap)

    def wallhack_thread_finished(self, result):
        # Stop the timer and reset the wallhack thread
        self.timer.stop()
        self.wallhack_thread = WallhackThread(self.settings)

        # Disable the stop button and enable the start button
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)
class WallhackThread(QThread):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.output_image = None
        self._stopped = False

    def run(self):
        # Create a window to capture the game screen
        game_window = WindowCapture('Game Window')

        while not self._stopped:
            # Capture the game screen and apply the wallhack
            game_image = game_window.capture()
            output_image = apply_wallhack(game_image, self.settings)

            # Set the output image
            self.output_image = output_image

    def stop(self):
        self._stopped = True


def apply_wallhack(image, settings):
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a mask for the walls based on the low and high HSV values
    wall_mask = cv2.inRange(hsv_image, settings.low_hsv, settings.high_hsv)

    # Apply the mask to the original image to get the wallhack output
    output_image = cv2.bitwise_and(image, image, mask=wall_mask)

    # Convert the output image to RGB for display
    output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

    # Show the walls in the output image if show_walls is True
    if settings.show_walls:
        wall_mask = cv2.cvtColor(wall_mask, cv2.COLOR_GRAY2RGB)
        output_image = cv2.addWeighted(output_image, 0.5, wall_mask, 0.5, 0)

    # Perform bunny hopping if bunny_hop is True
    if settings.bunny_hop:
        perform_bunny_hop()

    return output_image


def perform_bunny_hop():
    # TODO: Implement bunny hopping logic
    pass
class WallhackSettings:
def init(self, low_hsv, high_hsv, show_walls, bunny_hop):
self.low_hsv = low_hsv
self.high_hsv = high_hsv
self.show_walls = show_walls
self.bunny_hop = bunny_hop
def get_settings(self):
    return {
        'low_hsv': list(self.low_hsv),
        'high_hsv': list(self.high_hsv),
        'show_walls': self.show_walls,
        'bunny_hop': self.bunny_hop
    }

def set_settings(self, settings):
    self.low_hsv = np.array(settings['low_hsv'])
    self.high_hsv = np.array(settings['high_hsv'])
    self.show_walls = settings['show_walls']
    self.bunny_hop = settings['bunny_hop']
class WindowCapture:
def init(self, window_name):
self.window_name = window_name
self.hwnd = win32gui.FindWindow(None, self.window_name)
if not self.hwnd:
raise Exception(f'Window "{self.window_name}" not found')
def capture(self):
    # Get the dimensions of the window
    window_rect = win32gui.GetWindowRect(self.hwnd)
    left, top, right, bottom = window_rect
    width = right - left
    height = bottom - top

    # Get the device context of the window
    hwnd_dc = win32gui.GetWindowDC(self.hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()

    # Create a bitmap to hold the screenshot
    save_bitmap = win32ui.CreateBitmap()
    save_bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
    save_dc.SelectObject(save_bitmap)

    # Copy the screen into the bitmap
    result = windll.user32.PrintWindow(self.hwnd, save_dc.GetSafeHdc(), 0)
    bmp_info = save_bitmap.GetInfo()
    bmp_str = save_bitmap.GetBitmapBits(True)

    # Convert the bitmap to an image
    image = np.fromstring(bmp_str, dtype='uint8')
    image = image.reshape((bmp_info['bmHeight'], bmp_info['bmWidth'], 4))
    image = image[..., :3]

    # Clean up
    win32gui.DeleteObject(save_bitmap.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(self.hwnd, hwnd_dc)

    return image

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout,
QPushButton, QCheckBox, QSlider, QSpinBox, QMessageBox, QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import Qt, QTimer

class WallhackApp(QMainWindow):
def init(self):
super().init()
    # Initialize the UI
    self.init_ui()

    # Initialize the wallhack settings
    self.settings = WallhackSettings(
        low_hsv=np.array([0, 0, 0]),
        high_hsv=np.array([180, 255, 60]),
        show_walls=False,
        bunny_hop=False
    )

    # Initialize the wallhack thread
    self.wallhack_thread = WallhackThread(self.settings)

    # Connect signals and slots
    self.start_button.clicked.connect(self.start_wallhack)
    self.stop_button.clicked.connect(self.stop_wallhack)
    self.settings_button.clicked.connect(self.open_settings)
    self.save_settings_button.clicked.connect(self.save_settings)
    self.load_settings_button.clicked.connect(self.load_settings)
    self.show_walls_check_box.stateChanged.connect(self.update_settings_show_walls)
    self.bunny_hop_check_box.stateChanged.connect(self.update_settings_bunny_hop)
    self.low_hue_slider.valueChanged.connect(self.update_settings_low_hsv)
    self.low_sat_slider.valueChanged.connect(self.update_settings_low_hsv)
    self.low_val_slider.valueChanged.connect(self.update_settings_low_hsv)
    self.high_hue_slider.valueChanged.connect(self.update_settings_high_hsv)
    self.high_sat_slider.valueChanged.connect(self.update_settings_high_hsv)
    self.high_val_slider.valueChanged.connect(self.update_settings_high_hsv)

    # Start the update timer
    self.update_timer = QTimer(self)
    self.update_timer.setInterval(50)
    self.update_timer.timeout.connect(self.update_display)
    self.update_timer.start()

def init_ui(self):
    # Create the main widget and layout
    self.main_widget = QWidget(self)
    self.main_layout = QVBoxLayout(self.main_widget)

    # Create the game screen label and graphics scene
    self.game_screen_label = QLabel(self.main_widget)
    self.game_screen_label.setAlignment(Qt.AlignCenter)
    self.game_screen_scene = QGraphicsScene(self)
    self.game_screen_pixmap_item = QGraphicsPixmapItem()
    self.game_screen_scene.addItem(self.game_screen_pixmap_item)
    self.game_screen_label.setPixmap(QPixmap.fromImage(QImage("game_screen_placeholder.png")))
    self.game_screen_label.setScaledContents(True)
    self.game_screen_label.setFixedSize(640, 480)

    # Create the control group box
    self.control_group_box = QGroupBox("Control", self.main_widget)

    self.start_button = QPushButton("Start Wallhack", self.control_group_box)
    self.stop_button = QPushButton("Stop Wallhack", self.control_group_box)
    self.stop_button.setEnabled(False)

    self.control_layout = QHBoxLayout(self.control_group_box)
    self.control_layout.addWidget(self.start_button)
    self.control_layout.addWidget(self.stop_button)

    # Create the settings group box
    self.settings_group_box = QGroupBox("Settings", self.main_widget)

    self.show_walls_check_box = QCheckBox("Show Walls", self.settings_group_box)
    self.show_walls_check_box.setChecked(self.settings.show_walls)

    self.bunny_hop_check_box = QCheckBox("Bunny Hop", self.settings_group_box)
    self.bunny_hop_check_box.setChecked(self.settings.bunny_hop)

    self.low_hue_slider = QSlider(Qt.Horizontal, self.settings_group_box)
    self.low_hue_slider.setRange(0, 
        # Create the layout for the low HSV sliders
        self.low_hsv_layout = QHBoxLayout()
        self.low_hue_label = QLabel("Low Hue", self.settings_group_box)
        self.low_hue_spin_box = QSpinBox(self.settings_group_box)
        self.low_hue_spin_box.setRange(0, 180)
        self.low_hue_spin_box.setValue(self.settings.low_hsv[0])
        self.low_sat_label = QLabel("Low Saturation", self.settings_group_box)
        self.low_sat_slider = QSlider(Qt.Horizontal, self.settings_group_box)
        self.low_sat_slider.setRange(0, 255)
        self.low_sat_slider.setValue(self.settings.low_hsv[1])
        self.low_val_label = QLabel("Low Value", self.settings_group_box)
        self.low_val_slider = QSlider(Qt.Horizontal, self.settings_group_box)
        self.low_val_slider.setRange(0, 255)
        self.low_val_slider.setValue(self.settings.low_hsv[2])
        self.low_hsv_layout.addWidget(self.low_hue_label)
        self.low_hsv_layout.addWidget(self.low_hue_spin_box)
        self.low_hsv_layout.addWidget(self.low_sat_label)
        self.low_hsv_layout.addWidget(self.low_sat_slider)
        self.low_hsv_layout.addWidget(self.low_val_label)
        self.low_hsv_layout.addWidget(self.low_val_slider)

        # Create the layout for the high HSV sliders
        self.high_hsv_layout = QHBoxLayout()
        self.high_hue_label = QLabel("High Hue", self.settings_group_box)
        self.high_hue_spin_box = QSpinBox(self.settings_group_box)
        self.high_hue_spin_box.setRange(0, 180)
        self.high_hue_spin_box.setValue(self.settings.high_hsv[0])
        self.high_sat_label = QLabel("High Saturation", self.settings_group_box)
        self.high_sat_slider = QSlider(Qt.Horizontal, self.settings_group_box)
        self.high_sat_slider.setRange(0, 255)
        self.high_sat_slider.setValue(self.settings.high_hsv[1])
        self.high_val_label = QLabel("High Value", self.settings_group_box)
        self.high_val_slider = QSlider(Qt.Horizontal, self.settings_group_box)
        self.high_val_slider.setRange(0, 255)
        self.high_val_slider.setValue(self.settings.high_hsv[2])
        self.high_hsv_layout.addWidget(self.high_hue_label)
        self.high_hsv_layout.addWidget(self.high_hue_spin_box)
        self.high_hsv_layout.addWidget(self.high_sat_label)
        self.high_hsv_layout.addWidget(self.high_sat_slider)
        self.high_hsv_layout.addWidget(self.high_val_label)
        self.high_hsv_layout.addWidget(self.high_val_slider)

        # Create the layout for the settings buttons
        self.settings_buttons_layout = QHBoxLayout()
        self.save_settings_button = QPushButton("Save", self.settings_group_box)
        self.load_settings_button = QPushButton("Load", self.settings_group_box)
        self.settings_buttons_layout.addWidget(self.save_settings_button)
        self.settings_buttons_layout.addWidget(self.load_settings_button)

        # Create the settings group box layout
        self.settings_layout = QVBoxLayout(self.settings_group_box)
        self.settings_layout.addWidget(self.show_walls_check_box)
        self.settings_layout.addWidget(self.bunny_hop_check_box)
        self.settings_layout.addLayout(self.low_hsv_layout)
        self.settings_layout.addLayout(self.high_hsv_layout)
        self.settings_layout.addLayout(self.settings_buttons_layout)

        # Add the widgets to the main layout
        self.main_layout.addWidget(self.game_screen_label)
        self.main_layout.addWidget(self.control_group_box)
        self.main_layout.addWidget(self.settings_group_box)

        # Set the main widget
        self.setCentral
        # Create the status bar
        self.statusBar().showMessage("Ready")

        # Connect signals and slots
        self.start_stop_button.clicked.connect(self.start_stop_game)
        self.reset_button.clicked.connect(self.reset_game)
        self.show_walls_check_box.stateChanged.connect(self.toggle_walls)
        self.bunny_hop_check_box.stateChanged.connect(self.toggle_bunny_hop)
        self.low_hue_spin_box.valueChanged.connect(self.update_low_hue)
        self.low_sat_slider.valueChanged.connect(self.update_low_saturation)
        self.low_val_slider.valueChanged.connect(self.update_low_value)
        self.high_hue_spin_box.valueChanged.connect(self.update_high_hue)
        self.high_sat_slider.valueChanged.connect(self.update_high_saturation)
        self.high_val_slider.valueChanged.connect(self.update_high_value)
        self.save_settings_button.clicked.connect(self.save_settings)
        self.load_settings_button.clicked.connect(self.load_settings)

        # Set the window properties
        self.setWindowTitle("Pong Game")
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def start_stop_game(self):
        if self.game.is_running:
            self.game.stop()
            self.start_stop_button.setText("Start")
            self.statusBar().showMessage("Game stopped")
        else:
            self.game.start()
            self.start_stop_button.setText("Stop")
            self.statusBar().showMessage("Game started")

    def reset_game(self):
        self.game.reset()
        self.statusBar().showMessage("Game reset")

    def toggle_walls(self, state):
        self.game.show_walls = (state == Qt.Checked)

    def toggle_bunny_hop(self, state):
        self.game.bunny_hop = (state == Qt.Checked)

    def update_low_hue(self, value):
        self.settings.low_hsv[0] = value

    def update_low_saturation(self, value):
        self.settings.low_hsv[1] = value

    def update_low_value(self, value):
        self.settings.low_hsv[2] = value

    def update_high_hue(self, value):
        self.settings.high_hsv[0] = value

    def update_high_saturation(self, value):
        self.settings.high_hsv[1] = value

    def update_high_value(self, value):
        self.settings.high_hsv[2] = value

    def save_settings(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Settings", "", "JSON Files (*.json)")
        if file_path:
            self.settings.save(file_path)
            self.statusBar().showMessage(f"Settings saved to {file_path}")

    def load_settings(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Settings", "", "JSON Files (*.json)")
        if file_path:
            self.settings.load(file_path)
            self.update_ui()
            self.statusBar().showMessage(f"Settings loaded from {file_path}")

    def update_ui(self):
        self.show_walls_check_box.setChecked(self.game.show_walls)
        self.bunny_hop_check_box.setChecked(self.game.bunny_hop)
        self.low_hue_spin_box.setValue(self.settings.low_hsv[0])
        self.low_sat_slider.setValue(self.settings.low_hsv[1])
        self.low_val_slider.setValue(self.settings.low_hsv[2])
        self.high_hue_spin_box.setValue(self.settings.high_hsv[0])
        self.high_sat_slider.setValue(self.settings.high_hsv[1])
        self.high_val_slider.setValue(self.settings.high_hsv[2])
def closeEvent(self, event):
    """
    This method is called when the user clicks the X button to close the window. We override it to ask the user if
    they really want to quit the application.
    """
    reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.Yes:
        self.game.stop()
        event.accept()
    else:
        event.ignore()
Part 8:

python
Copy code
def closeEvent(self, event):
    """
    This method is called when the user clicks the X button to close the window. We override it to ask the user if
    they really want to quit the application.
    """
    reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.Yes:
        self.game.stop()
        event.accept()
    else:
        event.ignore()
if name == "main":
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())


# In[ ]:





# In[ ]:




