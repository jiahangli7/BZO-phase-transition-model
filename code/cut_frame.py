from ovito.io import import_file, export_file


pipeline = import_file("BZO2.lammpstrj")


start_frame = int(input("请输入起始帧数："))


end_frame = int(input("请输入终止帧数："))


output_file = "output_{}_{}.dump".format(start_frame, end_frame)


columns = ["Particle Identifier",
           "Particle Type",
           "Position.X",
           "Position.Y",
           "Position.Z"]


with open(output_file, 'w') as f:
    for frame in range(pipeline.source.num_frames):
       
        if start_frame <= frame <= end_frame:
           
            export_file(pipeline, f, "lammps/dump",
                        frame=frame,
                        columns=columns,
                        multiple_frames=True)

        if frame > end_frame:
            break
