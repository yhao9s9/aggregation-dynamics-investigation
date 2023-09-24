## Image-based flow simulation for platelet aggregate

This repository presents the implementation of image-based flow simulation for *in vitro* platelet aggregates in 3D. The implementation of the finite element simulation is based on open source [FreeFEM](https://freefem.org/).

The repository contains all the necessary information/data to reproduce the results. The detailed instructions are listed in the following section.

### Experimental image processing

The experimental image processing code is implemented in Python and FreeFEM, organized into several steps, each corresponding to a .py or .edp file:

* `transform.py` contains the following functions:
  - Transform the experimental image data to vtk file which could be further segmented in [3D Slicer](https://www.slicer.org/)  
  - Read fluorescence intensity from the image
  - Remember to run with `python <transform.py> output.txt` to get the number of intensity values in each case

After having the vtk file for platelet aggregate, the outline of the aggregate could be segmented in 3D Slicer. Then after uniformly remeshing the segmentation stl in [MeshLab](https://www.meshlab.net/), generate the mesh that will be used for flow simulation in [Gmsh](https://gmsh.info/). 

To determine the density of platelets within the platelet aggregates, a manual counting method is applied at five measurement points. Once we have the data, the linear regression method is applied to estimate the relationship between fluorescence intensity and platelet density:
* `checkIntensity.edp` reads the fluorescence intensity to the corresponding aggregate mesh to check the minimum and maximum values, which will be used in linear regression
* `linearRegression.py` estimates the relation between intensity and platelet density with a 95% confidence region. Remember to run with `python <linearRegression.py> relation.txt` to get the coefficients of the regression line

After establishing this relationship, the fluorescence intensity values need to be re-read for the aggregate mesh and transformed into corresponding platelet density and permeability:
* `interpolation.edp` contains the following functions:
  - Read the intensity value to the aggregate mesh, and transform it into the platelet density using the relationships of fluorescence intensity & density
  - Calculate the permeability of the aggregate via the Kozeny-Carman equation
  - Remesh the aggregate mesh according to the volume factor
  - Interpolate all data to fluid mesh and remesh the fluid mesh according to the platelet density
  - Save the new meshes & sol data for NS simulation

All the preparations are NOW done. The flow simulation could start.

### Data analysis

The data analysis scripts are all stored in `\analysis`. This directory consists of the following files:
* `meshData/mesh_volume_800.edp` collects the volume, height, bottom area and maximum length of the platelet aggregate meshes
* `meshdata.py` analyses the interesting values of the aggregate meshes
* `densityData/tranDensity.py` collects the density data of all study cases (`tranPermea.py` is for permeability and `tranInten.py` is for fluorescence intensity)
* `density.py` plots the average density under different WSRs
* `permeability.py` plots the average permeability under different WSRs

### Flow simulation
The flow simulation code is implemented in FreeFEM. A parallel version of FreeFEM should be installed to achieve a better performance, something that is crucial for finer meshes and 3D cases. A proper MPI runtime is required to run parallel FreeFEM (such as OpenMPI or MPICH). The PETSc module should also be installed and linked to FreeFEM (which is usually the default config for installing/compiling FreeFEM). The installation procedure can be found [here](https://doc.freefem.org/introduction/installation.html) for different platforms.

After installing the required software packages, the code can be run like this:

`$ ff-mpirun -np 128 ns_3d.edp -v 0`

You can specify the number of employed cores (which also implies the number of mesh sub-partitions) by the `-n` switch (it is 128 in this example). The `-v 0` switch is used to suppress the verbosity of FreeFEM. The configs (such as the input mesh or the output location) can be modified in the source files.

Additionally, if you have access to a supercomputer, you can submit a job to run the code using the following command: `$ sbatch run.sl`.

### Flow simulation
Flow simulation results are saved in vtk file, which can be processed in [Paraview](https://www.paraview.org/). In order to process the result more efficiently, it's recommended to import the resultsProcess.py script as a macro within Paraview. This script offers several essential functions, including:
- Calculation of velocity magnitude, shear rate, shear stress, and elongational rate within platelet aggregates.
- Access to all simulation results from the faceward, backward, top, and entire surface of platelet aggregates.
- The ability to export these results into CSV files for subsequent utilization.
