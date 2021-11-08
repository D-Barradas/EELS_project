#%%
import hyperspy.api as hs
import numpy as np
import matplotlib.pyplot as plt
#%%
# my_file = hs.load("../SI data/ADF Image (SI Survey).dm4")
my_file = hs.load("../SI data/EELS Spectrum Image (low-loss).dm4")
#EELS Spectrum Image (low-loss).dm4

# %%
## plot an example not realted to the data
hs.datasets.example_signals.EDS_TEM_Spectrum().plot()
# %%

my_file
# %%
## to check the file type 
## <class 'hyperspy._signals.signal2d.Signal2D'>
print ( type( my_file ) ) 
# %%
## shows the meta data 
### access the title , date if the image is 
### binned 
### this is better used on the notebook

print ( my_file.metadata )

# %%
### access the firts element of the y axis
##  and plot it, this is the firts strip 
## this is a plot od Electron counts vs micrometers 
my_file.isig[0].plot()

# %%
## access all the numbers of the image y axis this is raw data
my_file.isig[0].data

# %%
## plot the whole image as shown in other software
my_file.isig[1:1].plot()

# my_file.signal2d.plot()
# %%
