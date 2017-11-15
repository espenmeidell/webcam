import pygame
import pygame.camera
import threading
import datetime


def log(msg: str, level: str = "INFO"):
    print("[%s][%s]: %s" % (level, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg))


def capture_image():
    log("Taking picture")
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video1")
    cam.start()
    img = cam.get_image()
    pygame.image.save(img,"pictures/%s.jpg" % datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
    threading.Timer(10, capture_image).start()
    cam.stop()


capture_image()