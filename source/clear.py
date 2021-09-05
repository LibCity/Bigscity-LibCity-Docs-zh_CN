import os
import re


def modify_doc_title_dir(abspath_rstfiles_dir):
    rst_files = os.listdir(abspath_rstfiles_dir)
    del_nodes = ['Submodules', 'Module contents', 'Subpackages']
    del_str = [' module', ' package']
    del_file = ['libcity.rst', 'modules.rst']
    for rst_file in rst_files:
        if rst_file in del_file:
            os.remove(os.path.join(abspath_rstfiles_dir, rst_file))
            continue
        f = open(os.path.join(abspath_rstfiles_dir, rst_file), 'r')
        file_lines = f.readlines()
        f.close()
        write_con = []
        flag = 0
        for file_line in file_lines:
            if file_line.strip() in del_nodes:
                flag = 1
                continue
            if flag:
                flag = 0
                continue
            if re.search(del_str[0], file_line):
                modify_line = file_line.replace(del_str[0], '')
                write_con.append(modify_line)
                continue
            if re.search(del_str[1], file_line):
                modify_line = file_line.replace(del_str[1], '')
                write_con.append(modify_line)
                continue
            write_con.append(file_line)
        f = open(os.path.join(abspath_rstfiles_dir, rst_file), 'w')
        f.writelines(write_con)
        f.close()
    solve_list = [
        'libcity.model.traffic_flow_prediction.rst',
        'libcity.model.traffic_demand_prediction.rst',
        'libcity.model.traffic_speed_prediction.rst',
        'libcity.model.trajectory_loc_prediction.rst',
        'libcity.data.dataset.trajectory_encoder.rst',
        'libcity.config.rst',
        'libcity.data.rst',
        'libcity.data.dataset.rst',
        'libcity.evaluator.rst',
        'libcity.executor.rst',
        'libcity.model.rst',
        'libcity.pipeline.rst',
        'libcity.utils.rst',
    ]
    for rst_file in rst_files:
        if rst_file in solve_list:
            print(rst_file)
            f = open(os.path.join(abspath_rstfiles_dir, rst_file), 'r')
            file_lines = f.readlines()
            f.close()
            write_con = []
            i=0
            while i < (len(file_lines)):
                if 'automodule' in file_lines[i]:
                    i=i+4  # 连跳4行
                else:
                    write_con.append(file_lines[i])
                    i=i+1
            f = open(os.path.join(abspath_rstfiles_dir, rst_file), 'w')
            f.writelines(write_con)
            f.close()



if __name__ == '__main__':
    modify_doc_title_dir('./source/libcity')
