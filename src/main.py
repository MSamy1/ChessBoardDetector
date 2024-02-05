import gui as gui
def main():
    gui.browse_GUI()
    gui.buildimg_GUI()
    imgc=gui.transform_img()
    gui.ImageC_GUI(imgc)
    gui.predictpositions()

if __name__ == "__main__":
    main()
