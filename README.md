## Image-based flow simulation for platelet aggregate

This repository presents the implementation of image-based flow simulation for platelet aggregate formed *in vitro* in 3D. The implementation of the finite element simulation is based on open source [FreeFEM](https://freefem.org/).

The repository contains all the necessary information/data to reproduce the results. The detailed instructions are listed in the following section.

### Experimental image processing

The experimental image processing code is implemented in Python and FreeFEM. Each steps corresponding to a .py/.edp file:

* `transform.py` contains following functions:
  - Transform the experimental image data to vtk file which could be segmented in [3D Slicer] (https://www.slicer.org/) 
  - Read fluorescence intensity from the image
  - Remember to run with `python <transform.py> output.txt` to get the number of intensity value in each case

After having the vtk file for platelet aggregate, the outline of the aggregate could be segmented in 3D Slicer. Then after uniformly remeshing the segmentation stl in [MeshLab](https://www.meshlab.net/), generate the mesh that chould be used for flow simulation in [Gmsh](https://gmsh.info/). 

* `meshData/mesh_volume_800.edp` collects the volume, height, bottom area and maximum length of the platelet aggregate meshes.
* `data.py` analyses the interesting values of the aggregates meshes
* `checkIntensity.edp` reads the fluorescence intensity to the corresponding aggregate mesh to check the minimum and maximum values of it, which could be used in estimation of platelet density

To get the density of platelet inside the platelet aggregates, the manully counting method is applied (5 measurements points). After having the data, the linear regression method is applied to estimate the relations between fluorescence intensity with platelet density:
* `linearRegression` estimate the relation of the intensity with platelet density with 95% confidence region, remember to run with `python <linearRegression.py> relation.txt` to get the coefficients of the regression line

### Flow simulation
The flow simulation code is implemented in FreeFEM. A parallel version of FreeFEM should be installed to achieve a better performance, something that is crucial for finer meshes and 3D cases.. A proper MPI runtime is required to run parallel FreeFEM (such as OpenMPI or MPICH). The PETSc module should also be installed and linked to FreeFEM (which is usually the default config for installing/compiling FreeFEM). The installation procedure can be found [here](https://doc.freefem.org/introduction/installation.html) for different platforms.

After installing the required software packages, the code can be run like this:

`$ ff-mpirun -np 4 neohook.edp -v 0`

You can specify the number of employed cores (which also implies the number of mesh sub-partitions) by the `-n` switch (it is 4 in this example). The `-v 0` switch is used to suppress the verbosity of FreeFEM. The configs (such as the input mesh or the output location) can be modified in the source files.
