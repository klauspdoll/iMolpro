# iMolpro

This app provides an integrated environment for the Molpro quantum chemistry package.  You can prepare inputs for jobs, launch them, and view their results.

The program works with Molpro *Projects* that are managed by [sjef](https://github.com/molpro/sjef/blob/master/README.md). Each sjef project is a filesystem directory with suffix `.molpro` that contains all files associated with the job, together with some status information.  This program allows you to create new projects, and also to work with existing projects that might have been created elsewhere (for example, with [pymolpro](https://github.com/molpro/pymolpro/blob/master/README.rst))

On launching, you will normally see the Chooser window that allows you to open or create projects. You can have as many open as you want, and each appears in its own independent project window.  Each project window has two principal panes: on the left is the job input, either as the actual Molpro input file or via a menu-driven guided input creator; on the right is the job output and/or the three-dimensional molecular structure together with any orbitals or vibrational modes that have been calculated, and an editable three-dimensional model of the input geometry.

Molecular structures can be prepared and edited within the program, or imported from an external database search ([PubChem](https://pubchem.ncbi.nlm.nih.gov) or [ChemSpider](https://www.chemspider.com))

Once the input has been prepared, the job can be submitted either locally (default) or remotely (via a configured sjef backend). The sjef backend specifications can be edited from the program. Once running, the job status and output are monitored and displayed continuously.