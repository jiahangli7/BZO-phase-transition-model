from ovito.io import import_file, export_file

# 读取原始数据文件
pipeline = import_file("BZO2.lammpstrj")

# 手动输入起始帧数
start_frame = int(input("请输入起始帧数："))

# 设置要导出的步数范围
end_frame = int(input("请输入终止帧数："))

# 设置输出文件名
output_file = "output_{}_{}.dump".format(start_frame, end_frame)

# 导出文件时使用的粒子属性列
columns = ["Particle Identifier",
           "Particle Type",
           "Position.X",
           "Position.Y",
           "Position.Z"]

# 遍历每一帧数据，将满足条件的帧数据追加写入输出文件
with open(output_file, 'w') as f:
    for frame in range(pipeline.source.num_frames):
        # 如果当前帧在目标步数范围内，则导出该帧
        if start_frame <= frame <= end_frame:
            # 导出当前帧数据
            export_file(pipeline, f, "lammps/dump",
                        frame=frame,
                        columns=columns,
                        multiple_frames=True)

        # 如果当前帧超过目标范围，则退出循环
        if frame > end_frame:
            break
