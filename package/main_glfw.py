import os.path

import resources

import glfw
import live2d.v3 as live2d


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
    window = init_window(270, 200, "glfw")
    if not window:
        print("Failed to create GLFW window")
        return

    live2d.init()

    live2d.glewInit()
    live2d.setGLProperties()

    model = live2d.LAppModel()
    model.LoadModelJson(os.path.join(resources.RESOURCES_DIRECTORY, "v3/波奇酱2.0/波奇酱2.0.model3.json"))

    model.StartMotion("TapBody", 3, 3, onStartMotionHandler=None, onFinishMotionHandler=lambda: print("end 1"))

    model.StartMotion("TapBody", 4, 3, onFinishMotionHandler=lambda: print("end 2"))

    model.StartRandomMotion("TapBody", 3, onStartMotionHandler=lambda group, no: print(f"start 1 {group} {no}"),
                            onFinishMotionHandler=lambda: print("end 3"))

    read = False

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
