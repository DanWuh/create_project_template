'''
Charalambos Themistocleous
2018

Project/
|-- writing/
|   |-- figures
|   |-- bib
|
|-- statistics/
|   |-- data/
|   |   |-- data.csv
|   |-- figures/
|
|--speech
|   |-- sounds/
|   |-- textgrids/
|   |-- texts/
|
|-- README.md
'''
import os
import sys
import datetime


def main():
    # detect the current working directory and print it
    path = os.getcwd()
    print("The current working directory is %s" % path)
    # as the user to provide a name for the file.
    project_name = input("Provide project's name: ")
    project_name = str(project_name)
    answer = input(
        "A new project will be created in the %s proceed? (yes or no) " % path)
    if answer.lower() in ["yes", "y", "ok"]:
        try:
            os.mkdir(path + "/" + project_name)
            f = open(path + "/" + project_name + "/" + "README.md", "w+")
            f.write("# " + project_name + "\n" + str(datetime.date.today()))
            f.close()
            print("%s" + "%s" % path, project_name)
            os.mkdir(path + "/" + project_name + "/m_model/")
            os.mkdir(path + "/" + project_name + "/m_model/autosave/")
            os.mkdir(path + "/" + project_name + "/m_model/cache/")
            os.mkdir(path + "/" + project_name + "/m_model/clips/")
            os.mkdir(path + "/" + project_name + "/m_model/data/")
            os.mkdir(path + "/" + project_name + "/m_model/images/")
            os.mkdir(path + "/" + project_name + "/m_model/movies/")
            os.mkdir(path + "/" + project_name + "/m_model/renderData/")
            os.mkdir(path + "/" + project_name + "/m_model/sceneAssembly")
            os.mkdir(path + "/" + project_name + "/m_model/scenes/")
            os.mkdir(path + "/" + project_name + "/m_model/scripts/")
            os.mkdir(path + "/" + project_name + "/m_model/sound/")
            os.mkdir(path + "/" + project_name + "/m_model/sourceimages/")
            os.mkdir(path + "/" + project_name + "/m_model/TimeEditor/")
            os.mkdir(path + "/" + project_name + "/m_model/fbx/")
            os.mkdir(path + "/" + project_name + "/m_model/obj/")
            os.mkdir(path + "/" + project_name + "/t_texture/")
            os.mkdir(path + "/" + project_name + "/t_texture/substance/")
            os.mkdir(path + "/" + project_name + "/t_texture/substance/model/")
            os.mkdir(path + "/" + project_name + "/t_texture/substance/source/")
            os.mkdir(path + "/" + project_name + "/t_texture/output/")
            os.mkdir(path + "/" + project_name + "/t_texture/mudbox/")
            os.mkdir(path + "/" + project_name + "/t_texture/reference/")
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)


if __name__ == "__main__":
    main()
