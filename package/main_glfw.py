import os.path
import resouces

import glfw
import live2d.v2 as live2d


# 窗口初始化
def init_window(width, height, title):
    if not glfw.init():
        return None

    window = glfw.create_window(width, height, title, None, None)
    if not window:
        glfw.terminate()
        return None

    glfw.make_context_current(window)
    return window


# 渲染循环
def main():
    window = init_window(270, 200, "Simple GLFW Window")
    if not window:
        print("Failed to create GLFW window")
        return

    live2d.init()

    model = live2d.LAppModel()
    if live2d.LIVE2D_VERSION == 3:
        model.LoadModelJson(os.path.join(resouces.RESOURCES_DIRECTORY, "v3/Haru/Haru.model3.json"))
    else:
        model.LoadModelJson(os.path.join(resouces.RESOURCES_DIRECTORY, "v2/kasumi2/kasumi2.model.json"))

    while not glfw.window_should_close(window):
        glfw.poll_events()

        live2d.clearBuffer()
        model.Update()
        model.Draw()

        glfw.swap_buffers(window)

    glfw.terminate()
    live2d.dispose()


if __name__ == "__main__":
    main()
