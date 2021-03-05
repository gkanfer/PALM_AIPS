os.chdir('/Users/kanferg/Desktop/Gil_LabWork/ANNA-PALM/Simulator/Similtor_genration/Data')
import scipy.io
oofset=scipy.io.loadmat('suboffsetmap.mat')
oofset=oofset['suboffsetmap']
var=scipy.io.loadmat('subvarmap.mat')
var=var['subvarmap']
gain=scipy.io.loadmat('subgainmap.mat')
gain=gain['subgainmap']
ims=scipy.io.loadmat('ims.mat')
ims=ims['ims']

offsetim=np.dstack([oofset]*np.shape(ims)[2])
varim=np.dstack([var]*np.shape(ims)[2])
vgainim=np.dstack([gain]*np.shape(ims)[2])
fin=(ims-offsetim)/vgainim

varim_in=var
gainim_in=gain


###testing the segmentation
allcd=[]
thresh=4
imsz=np.shape(fin)[1]
sz=(3,3,1)
filterdim1=varunif(fin,varim,sz)
sz=(9,9,1)
filterdim2=varunif(fin,varim,sz)
im_unif=filterdim1-filterdim2
sz=(5,5,1) 
max_im_temp=ndimage.maximum_filter(im_unif, size=sz)       
im_max=(im_unif>=.999*max_im_temp) & (im_unif>thresh)
a_flat=im_max.flatten()
a_ind=a_flat[]
# a=np.where(im_max==True,1,0)
# a_flat=a.flatten()
#save the index
a_ind=a_flat[a_flat==1]
a_ind=np.asarray(a_ind.T) 
a_ind=a_ind.T
#floor the results 
z=np.floor((a_ind/imsz)/imsz)
pnum=a_ind % imsz
x=pnum % imsz
y=np.floor(pnum/imsz)
