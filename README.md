# Scripts_MD_BCN_repo
The main scripts i will be using to analyse and customise the BCN meshes for the MD simulations.
1. Customize_graphene_layer.ipynb
   Here, we can use ASE package to customise the graphene mesh. I am using this to get different compositions of the BCN network.
   One issue as of noe is that we have to input the index of the atoms to be replaced. This can be visualised from the jupyter script itself.


   <img width="365" height="275" alt="image" src="https://github.com/user-attachments/assets/426183c4-930c-4b4c-a0c4-2a608241f94d" />

2. fix_Poscar -
   This code can be used to fix the POSCAR in case the elements are not alligned properly, as this could have adverse effect while choosing the POTCAR file. I am using this to because when I am exchanging the atoms in the POSCAR, it is just changing the coordinate point and inserting a new code like N001 ec. This script can be used to change this.
