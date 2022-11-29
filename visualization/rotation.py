"""
PyTeapot module for drawing rotating cube using OpenGL as per
quaternion or yaw, pitch, roll angles received over serial port.
"""

# output if angle is in desired range

import pygame
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import pandas as pd
import time

def main():
    video_flags = OPENGL | DOUBLEBUF
    pygame.init()
    screen = pygame.display.set_mode((640, 480), video_flags)
    pygame.display.set_caption("PhysioTrack")
    resizewin(640, 480)
    init()
    frames = 0
    ticks = pygame.time.get_ticks()
    df = pd.read_csv('multiple-raises-2.csv')
    # compensate_for_fluctuations(df['pitch (deg)'], df['roll (deg)'], df['yaw (deg)'])

    while 1:
        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            break
        #iterate through csv file
        state = 0 #keep raising arm
        prev_state = 0
        curr_reps = 0
        temp_count = 0
        error_count = 0
        error = False
        init_roll = df.iloc[0]['roll (deg)'] #initial value to compare angle to
        compare_roll = -90 #to compare start of abduction/adduction
        for index, row in df.iterrows():
            [yaw, pitch, roll] = read_data(row)
            abs_difference = roll - init_roll
            difference = roll - compare_roll
            print(state, curr_reps, temp_count, compare_roll, difference, abs_difference)

            #  CHECK ARM ANGLE too high
            if abs(abs_difference) > 90:
                state = 1 #too high
                error = True
            if (state == 1) and (abs(abs_difference) < 90): #arm was too high but is now lower
                state = 2

            # COUNT REPS
            if abs(difference) > 80:
                temp_count += 1 # increments on each end of abduction/adduction
                if (temp_count % 2) == 0: # at the bottom
                    curr_reps += 1
                    state = 0
                    compare_roll = -90 # set to new compare
                    if (error): # if at some point, was above 90
                        error_count += 1
                        error = False
                if (temp_count % 2) != 0: # at the top
                    state = 2 # lower your arm
                    compare_roll = 0 # set to new compare

            draw(1, yaw, pitch, roll, state, curr_reps, error_count)
            pygame.display.flip()
            frames += 1
    print("fps: %d" % ((frames*1000)/(pygame.time.get_ticks()-ticks)))


def resizewin(width, height):
    """
    For resizing window
    """
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0*width/height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init():
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def read_data(row):
    # yaw = float(line.split('y')[1])
    # pitch = float(line.split('p')[1])
    # roll = float(line.split('r')[1])

    # chunk size 10 is 0.1 seconds
    # chunksize = 10
    # for chunk in pd.read_csv('imu_data.csv', chunksize=chunksize):
    #     print(chunk)
    #     time.sleep(0.5)
    yaw = row['yaw (deg)']
    pitch = row['pitch (deg)']
    roll = row['roll (deg)']
    return [yaw, pitch, roll]
    

def draw(w, nx, ny, nz, state, curr_reps, error_count):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0.0, -7.0)

    drawText((-2.6, 1.8, 2), "PhysioTrack", 18)
    drawText((-2.6, 1.6, 2), "Shoulder Abduction", 16)
    drawText((-2.6, -2, 2), "Press Escape to exit.", 16)

    yaw = nx
    pitch = ny
    roll = nz

    if (state == 0):
        drawText((-2.6, -1.2, 2), "Keep raising your arm to complete the rep.", 16)
    if (state == 1):
        drawText((-2.6, -1.2, 2), "Arm is too high! Lower your arm into position.", 16)
    if (state == 2):
        drawText((-2.6, -1.2, 2), "Keep lowering your arm to complete the rep.", 16)

    drawText((-2.6, -1.4, 2), "Number of reps completed: %f of 20" %(curr_reps), 16)

    drawText((-2.6, -1.6, 2), "Number of incorrect reps: %f" %(error_count), 16)

    drawText((-2.6, -1.8, 2), "Yaw: %f, Pitch: %f, Roll: %f" %(yaw, pitch, roll), 16)

    glRotatef(-roll, 0.00, 0.00, 1.00)
    glRotatef(pitch, 1.00, 0.00, 0.00)
    glRotatef(yaw, 0.00, 1.00, 0.00)

    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.2, -1.0)
    glVertex3f(-1.0, 0.2, -1.0)
    glVertex3f(-1.0, 0.2, 1.0)
    glVertex3f(1.0, 0.2, 1.0)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, -0.2, 1.0)
    glVertex3f(-1.0, -0.2, 1.0)
    glVertex3f(-1.0, -0.2, -1.0)
    glVertex3f(1.0, -0.2, -1.0)

    glColor3f(0.5, 0.0, 1.0)
    glVertex3f(1.0, 0.2, 1.0)
    glVertex3f(-1.0, 0.2, 1.0)
    glVertex3f(-1.0, -0.2, 1.0)
    glVertex3f(1.0, -0.2, 1.0)

    glColor3f(0.5, 0.0, 1.0)
    glVertex3f(1.0, -0.2, -1.0)
    glVertex3f(-1.0, -0.2, -1.0)
    glVertex3f(-1.0, 0.2, -1.0)
    glVertex3f(1.0, 0.2, -1.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.2, 1.0)
    glVertex3f(-1.0, 0.2, -1.0)
    glVertex3f(-1.0, -0.2, -1.0)
    glVertex3f(-1.0, -0.2, 1.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, 0.2, -1.0)
    glVertex3f(1.0, 0.2, 1.0)
    glVertex3f(1.0, -0.2, 1.0)
    glVertex3f(1.0, -0.2, -1.0)
    glEnd()


def drawText(position, textString, size):
    font = pygame.font.SysFont("Courier", size, True)
    textSurface = font.render(textString, True, (255, 255, 255, 255), (0, 0, 0, 255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos3d(*position)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

#pitch roll yaw
# df['pitch_new'] = df.apply(lambda x :[(i, x[i]) for i in range(len(x))])
# print list(my_enumerate(a))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'a'), (4, 'b'), (5, 'c')]

FLUCTUATION_ANGLE = 90
def compensate_for_fluctuations(xline, yline, zline):
   for idx, x in enumerate(xline):
       if idx == 0:
           xline[idx] = 0 # Force the first angle to be zero
       else:
           if abs(x) - abs(xline[idx - 1]) >= FLUCTUATION_ANGLE:
               xline[idx] = xline[idx - 1]

   for idx, y in enumerate(yline):
       if idx == 0:
           yline[idx] = 0 # Force the first angle to be zero
       else:
           if abs(y) - abs(yline[idx - 1]) >= FLUCTUATION_ANGLE:
               yline[idx] = yline[idx - 1]

   for idx, z in enumerate(zline):

       if idx == 0:
           zline[idx] = 0 # Force the first angle to be zero
       else:
           if abs(z) - abs(zline[idx - 1]) >= FLUCTUATION_ANGLE:
               zline[idx] = zline[idx - 1]
   
   return xline, yline, zline

if __name__ == '__main__':
    main()