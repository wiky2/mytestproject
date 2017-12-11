###########################################
######  Written by:  Gary Strangman  ######
######  Last modified: Dec 10, 2002  ######
###########################################

"""
### A set of python functions useful for fMRI analysis.  Requires python1.5,
###     PIL (python imaging library) and Numeric
###
### CLUSTERING FUNCTIONS:
###   ijk_to_xyz(ijk,voxelsize): converts ijk triple to xyz triple
###   ijk_to_three(ijk,x,y,z): converts SINGLE index (ijk) to ijk triple
###             using max x/y/z coords
###   create_spherical_mask(radius): returns list of offsets w/i 'radius' units
###   threemaps(map1,map2,threshold): returns map1&map2, map1&~map2, ~map1&map2
###   cluster: class ... holds all voxels in a single cluster
###      members ... valcolumn, basesnape, peak, peakindex, peaklocation,
###             com, min, max, voxels, volume, voxelsize
###      methods ... add, toarray, idealized, lastijk, getnext, report,
###             compare2clusters
###   clustmap: class ... holds group of clusters
###      members ... clustmap, maxvol, totalvol, n, baseshape
###      methods ... add, toarray, getlocalmaxima, idealized, report,
###             compare2clusters
###   grouped_clustmaps: class ... holds multiple clustmaps (for "both" map)
###      members ... nclust, nmaps, maps
###      methods ... addclust, add (clustmap), toarray, report
###   findlocalmax(data,localradius,threshold,voxelsize): returns lmax loc/peak
###   findclust(data,threshold,radius,volumethresh,voxelsize): axe small activ.
###   mapcompare(map1,map2,threshold,clustradius,clustvolume,compareradius,
###              test_type='peaks'): or 'com', returns both, map1only, map2only
###
### PARADIGM FILE CREATION:
###   makeepochs(infile,outfile): takes time-file and makes num_slices file
###   makeparadigm(infile): takes num_slices file and makes paradigm file
###   makePvsT(inpara,outpara): converts para for 1 run and makes 2 14-blockers
###   correct_for_lag(p,killnumber=1): convert a paradigm, killing overlap pts
###   make10paras(inepochs,outparaprefix,shift=1): make a bunch for motor MRI
###
### IMAGE STATISTICS:
###   finddistances(kslogpimagestack,threshold,...): returns a list of
###      Euclidean distances between all pairs of points where p-val<threshold
###   do_tstats(pixelarray,paradigm): does the stats for pmap
###   do_ksstats(pixelarray,paradigm): does the stats for pmap
###   pmap(imagestack,paradigm): returns a p-map and -log(p) map for a fMRI run
###   pcmap(pixelarray,paradigm,threshold=300,dtim=0): returns a percent-
###      change map using -1s in paradigm as baseline
###   squash(imagestack,paradigm): multiplies stack times paradigm, then adds
###      all resulting images in the stack
###   fixmotion(stack,maxchange): remove motion-artif>maxchange, by subtraction
###   fixmotionattimes(stack,maxchange,timepts): as above, but only for timepts
###   elimmotionattimes(stack,start,end): subtract-out artifacts btw start/end
###   correlationmap(a,fcn,threshold=300): Pearson between pixels in a and fcn
###   corr3maps(filepattern,threshold_on=2.5e-5,threshold_off=1e-4): calculates
###      three correlation maps ... PvsR, TvsR, PvsT
###   log2p(a): calculates -exp(a), safe even for signed values of a
###   p2log(a): calculates -ln(a), safe even for signed values of a
###   safelog(a): calculates ln(a), returning 0 for zeros/neg numbers in a
###   sn_bypara(stack,para,compareval=-1): calcs signal-to-noise on image
###      stack, using images where para=compareval
###   roi_timecourse(inarray,mask,dims=0): mean of inarray dims where mask<>0
###   varmap(a,windowsize): calc variance map (2D or 3D)
"""

##
## CHANGE LOG:
## ==========
## 02-12-02:  Added @@@
## 02-10-21:  Fixed safelog() to work more generally
## 01-18-01:  Merged code from multiple (ugh) copies of fmri.py
## 00-10-31:  Added safelog(a)
## 00-07-31:  Fixed cluster-related classes to deal with pos/neg clusters
## 00-06-02:  Changed createmask() name to create_spherical_mask()
##            Fixed varmap() to handle 2D OR 3D arrays
## 00-03-05:  Added mapcompare(), and cluster, clustmap and grouped_clustmaps
## 00-03-02:  Added findclust() function (adapted from AFNI edt_clust.c)
## 00-02-28:  Added createmask() function (adapted from AFNI edt_mask.c)
## 99-08-30:  Moved varmap in here from fun.py, moved getslopes() to ts.py
##            Moved all image creation/manipulation functions to im.py
## 99-08-21:  Added bilinear_interp() and smoothing options for linoverlay()
##            and logoverlay(); changed default scaling for linoverlay()
##            Also added a getslopes() function for "drift" correction
## 99-06-27:  Changed do_tstats to return both p-map (as before) AND t-map
## 99-06-26:  Added "None" option to threshold in correlationmap()
## 99-06-24:  Fixed linoverlay (some bad variable names), chgd rarray to oarray
##            Added parameter to do_tstats to allow for related-samples anal.
## 99-06-11:  Inverted colorbars in lin/logoverlay, added colormap() fcn after
##            removing same code from lin/logoverlay, improved lin/logoverlay
##            zooming
## 99-04-11:  Added roi_timecourse, sn_bypara, make10paras
## 99-04-??:  Added fixmotion, fixmotionattimes, elimmotionattimes
## 99-03-28:  Added roverlay, changed name of overlay to poverlay, log2p, p2log
##            Removed bget, bput etc. (all in io.py)
## 99-03-27:  Added fixmotion, fixmotionattimes, correlationmap, corr3maps
## 98-01-13:  Added makeepochs and makeparadigm from epochs.py (consolidate)
## 98-12-15:  Reversed array dimensions (shp) in ArrayToGreyImage (non-square
##               images didn't come out right); ArrayToColorImage too.
##            Added mr2stack function that converts stack of MR images to a
##               bshort stack.

import pstat, stats, io, support, ts
import sys, string, types, copy, struct, math, os, glob
import Image, ImageDraw, ImageFile, Numeric, ImageTk, yarn
from io import *
from support import incr
from PSDraw import PSDraw
rat = yarn.Rat
N=Numeric


#==================  CLUSTER-RELATED FUNCTIONS  ==================

def ijk_to_xyz(ijk,voxelsize=3.125):
    """
Converts an index-triple (i,j,k) to an xyz-triple.  Assumes the triple came
from a (51,61,48) array.  Note: most AFNI BRIKs come in as (48,61,51).

Usage:   ijk_to_xyz(ijk,voxelsize=3.125)
Returns: [x,y,z] corresponding to [i,j,k]
"""
    xyz = [0,0,0]
    xyz[0] = round((ijk[0]-25) *-voxelsize, 1)
    xyz[1] = round((ijk[1]-25) *-voxelsize +0.0667, 1)
    xyz[2] = round((20-ijk[2]) *-voxelsize -0.937, 1)
    return xyz

def ijk_to_three(ijk,x,y,z):
    """
Converts a single index (for a flattened 3D array) to a 3D index (a 3-element
list), using the x, y and z max-dims for a given 3D array.

Usage:   ijk_to_three(ijk,x,y,z)
Returns: [a,b,c] with a<x, b<y and c<z.
"""
    yz = y*z
    i = ijk/yz
    j = (ijk%(yz))/z
    k = ((ijk%(yz))%z)
    return [i,j,k]


def create_spherical_mask(radius):
    """
Creates a list of offsets in 3D space, one offset (row) per voxel, such
that the center of each voxel is within 'radius' units of one another.
Assumes square voxels.

Usage:   create_spherical_mask(radius)   radius units = voxels (i.e., NOT mm)
Returns: 2D array, rows=coordinate offsets, columns=[x,y,z]
"""
    mask = []
    dist_q = radius*radius
    for kk in range(-radius,radius+1):
        zq = kk*kk
        for jj in range(-radius,radius+1):
            yq = zq + (jj*jj)
            for ii in range(-radius,radius+1):
                xq = yq + (ii*ii)
                if (xq <= dist_q and xq > 0.0 ):
                    mask.append([ii,jj,kk])
    return N.array(mask)


def threemaps(map1,map2,threshold):
    """
Takes 2 activation maps and returns 3 ... a binary map where both maps show
activation (i.e., >threshold), and two non-binary maps where each map is
independently activated.

Usage:   threemaps(map1,map2,threshold)
Returns: and_map, map1_and_not_map2, map2_and_not_map2
"""
    tmap1 = N.greater(abs(map1),threshold)
    tmap2 = N.greater(abs(map2),threshold)
    and_map = tmap1*tmap2
    one_not_two = N.where(tmap1*(1-tmap2),map1,0)
    two_not_one = N.where(tmap2*(1-tmap1),map2,0)
    return and_map, one_not_two, two_not_one


class cluster:
    """
Class that holds all voxels in a single cluster.  Members include ...

baseshape = shape of the array from which the pixel came
peak      = peak value from the cluster
valcolumn = column where value of pixel appears
peakindex = the index of the peak value
peaklocation = i,j,k location of peak voxel for this cluster
com       = nearest i,j,k of cluster center-of-mass
volume    = volume of entire cluster (in ml; ASSUMES CUBIC VOXELS)
pixelsize = center-to-center distance for adjacent voxels (assumes CUBIC vox)
voxels    = the list of voxels (x,y,z,value,ijk)
"""
    def __init__(self,baseshape,firstvoxel=None,voxelsize=3.125):
        """\n__init__(self,baseshape,firstvoxel=None,voxelsize=3.125)\n"""
        self.valcolumn = 3
        self.baseshape = baseshape
        self.peak = 0
        self.peakindex = None
        self.peaklocation = None
        self.com = None
        self.min = [0,0,0]
        self.max = [0,0,0]
        self.voxels = []
        self.volume = 0
        self.voxelsize = voxelsize
        if firstvoxel:
            tmp = self.add(firstvoxel)

    def _ijk_to_three(self,ijk):
        return apply(ijk_to_three,(ijk,)+self.baseshape)

    def add(self,*args):
        """\ncluster.add([i,j,k],val) or cluster.add(ijk,val)\n"""
        if (self.peak>=0 and args[1]>=0):    # a POSITIVE cluster w/ POS addon
            if type(args[0]) == types.ListType:  # if first add-type
                self.voxels.append(args[0]+list(args[1:]))
            else:                           # a single (1D) index was provided
                triple = apply(ijk_to_three,args[0])
                self.voxels.append(triple+list(args[1:]))
            vox = self.voxels[-1]  # get most recently added voxel value
            if vox[self.valcolumn] > self.peak:
                self.peak = vox[self.valcolumn]
                self.peakindex = len(self.voxels)-1
                self.peaklocation = vox[:3]
        elif (self.peak<=0 and args[1]<0):  # a NEGATIVE cluster w/ NEG addon
            if type(args[0]) == types.ListType:  # if first add-type
                self.voxels.append(args[0]+list(args[1:]))
            else:                           # a single (1D) index was provided
                triple = apply(ijk_to_three,args[0])
                self.voxels.append(triple+list(args[1:]))
            vox = self.voxels[-1]  # get most recently added voxel value
            if abs(vox[self.valcolumn]) > abs(self.peak):
                self.peak = vox[self.valcolumn]
                self.peakindex = len(self.voxels)-1
                self.peaklocation = vox[:3]
        else:  # either POS cluster w/ NEG addon or NEG cluster with POS addon
            if args[1] > 0:
                print "Can't add POS voxel to a NEG cluster.  Skipping. ", args[1], self.peak
            else:
                print "Can't add NEG voxel to a POS cluster.  Skipping. ", args[1], self.peak
            return 0  # unsuccessful add-on
        weights = N.array(self.voxels)[:,self.valcolumn][:,N.NewAxis]
        self.com = N.sum(N.array(self.voxels)[:,:3]*weights)/N.sum(weights)
        self.com = stats.around(self.com,0).astype(N.Int)
        for i in range(3):
            self.min[i] = min(vox[i],self.min[i])
            self.max[i] = max(vox[i],self.max[i])
        self.volume = self.volume + self.voxelsize**3
        return 1  # successful add-on

    def toarray(self):
        a = N.zeros(self.baseshape,N.Float)
        for i in range(len(self.voxels)):
            idx = N.array(self.voxels[i][:3])
            a[idx] = self.voxels[i][self.valcolumn]
        return a

    def fill(self,fillvalue):
        a = N.zeros(self.baseshape,N.Float)
        for i in range(len(self.voxels)):
            idx = N.array(self.voxels[i][:3])
            a[idx] = fillvalue
        return a

    def idealized(self,radius,peakval=60,surroundval=20):
        """\nidealized(self,radius,peakval=60,surroundval=20)\n"""
        a = N.zeros(self.baseshape,N.Float)
        idx = N.array(self.voxels[self.peakindex][:3])
        a[idx] = peakval
        mask = N.array(create_spherical_mask(radius))
        for offset in mask:
            oidx = idx+offset
            if (N.sum(N.less(oidx,0))==0 and
                N.sum(N.greater_equal(oidx,self.baseshape))==0):
                a[idx+offset] = surroundval
        return a

    def lastijk(self):
        return N.array(self.voxels[-1][-1])

    def getnext(self,indx):
        return N.array(self.voxels[indx][-1])

    def report(self,header=None):
        if header:
            outstr = string.join(['Volume',
                                  'CM LR','CM PA','CM IS',
                                  'minLR','maxLR',
                                  'minPA','maxPA',
                                  'minIS','maxIS',
                                  'Mean',
                                  'Peak',
                                  'MI LR','MI PA','MI IS'],'\t')
            return outstr
        else:
            pi = N.array(self.peaklocation)[::-1]
            p = stats.around(ijk_to_xyz(pi),1)
            ci = N.array(self.com)[::-1]
            c = stats.around(ijk_to_xyz(ci),1)
            d = N.array(self.voxels)
            mins = [min(d[:,0]),min(d[:,1]),min(d[:,2])]
            maxs = [max(d[:,0]),max(d[:,1]),max(d[:,2])]
            mi = stats.around(ijk_to_xyz(mins),1)
            ma = stats.around(ijk_to_xyz(maxs),1)
            ## exchanging mi(ns) and ma(xs) here is a hack since
            ## apparently LR and AP are reversed relative to i and j
            ## PROBABLY STILL NOT RIGHT!!! (ONLY THE MIN/MAXs)
            outstr = string.join([str(int(round(self.volume,0)))]+
                                 map(str,c)+
                                 [str(ma[0]),str(mi[0])]+
                                 [str(ma[1]),str(mi[1])]+
                                 [str(mi[2]),str(ma[2])]+
                                 [str(round(stats.mean(d[:,self.valcolumn]),2))]+
                                 [str(round(self.peak,3))]+
                                 map(str,p),'\t')
            return outstr
                              

    def compare2clusters(self,other,radius,type='peak'):
        """
        compare2clusters(self,other,radius,type='peak') or 'com'

        Returns 1 if cluster peaks/center-of-masses are less than radius units
        apart, 0 if they are greater than radius units apart, and -1 if they
        are less than radius units apart BUT are of differing sign.
        """
        if type=='peak':
            xyz1 = N.array(ijk_to_xyz(self.peaklocation),N.Float)
            xyz2 = N.array(ijk_to_xyz(other.peaklocation),N.Float)
            sign1 = (self.peak>=0)*2-1  # 1 if positive, -1 if negative
            sign2 = (other.peak>=0)*2-1
        else:
            xyz1 = N.array(ijk_to_xyz(self.com),N.Float)
            xyz2 = N.array(ijk_to_xyz(other.com),N.Float)
            sign1 = (self.peak>=0)*2-1  # 1 if positive, -1 if negative
            sign2 = (other.peak>=0)*2-1
        if N.sum((xyz1-xyz2)**2) < radius**2:
            return 1*sign1*sign2  # 1 if clusters are same-sign, -1 if diff.
        else:
            return 0


class clustmap:
    """
Class that holds a group of clusters.  Members include ...

clusters  = a list of objects of class cluster
maxvol    = volume (number of voxels) in largest cluster
totalvol  = total volume of all clusters
n         = number of clusters
baseshape = shape of array inside which this cluster resides

Usage:   clustmap(self,firstcluster=None)
"""
    def __init__(self,firstcluster=None):
        """\n__init__(self,firstcluster=None)\n"""
        self.clusters = []
        self.n = 0
        self.maxvol = 0
        self.totalvol = 0
        self.baseshape = None
        self.lmax = None
        if firstcluster:
            tmp = self.add(firstcluster)

    def add(self,cluster):
        if type(self.baseshape) == NoneType:
            self.baseshape = N.array(cluster.baseshape)
        else:
            if N.sum(N.not_equal(N.array(cluster.baseshape),self.baseshape))>0:
                raise ValueError, "Tried to add a cluster of wrong shape to clustmap."
        self.n = self.n + 1
        self.clusters.append(cluster)
        if cluster.volume > self.maxvol:
            self.maxvol = cluster.volume
        self.totalvol = self.totalvol + cluster.volume

    def toarray(self):
        if type(self.baseshape) == NoneType:  # haven't added any yet
            print "Clustmap is empty."
            return
        a = N.zeros(self.baseshape)
        for i in range(self.n):
            a = a + self.clusters[i].toarray()
        return a

    def _getallvoxels(self):
        vox = []
        # loop through all clusters to append voxels from each
        for c in range(self.n):
            for v in range(len(self.clusters[c].voxels)):
                vox.append(self.clusters[c].voxels[v])
        return vox

    def computelocalmaxima(self,lmaxradius,thresh):
        lmaxbyloc, lmaxbypeak = findlocalmax(self.toarray(),lmaxradius,thresh,
                                             voxelsize=3.125)
        lmaxclustmap = clustmap()
        for row in lmaxbyloc:
            c = cluster(self.baseshape)
            c.add([row[5],row[4],row[3]],row[6]) # [z,y,x], peak-value
            lmaxclustmap.add(c)
        return lmaxclustmap

    def getlocalmaxima(self,lmaxradius):
        mask = N.array(create_spherical_mask(lmaxradius))
        # loop through all clusters to append voxels from each
        # note that voxels = (x,y,z,val,ijk)
        for c in range(self.n):
            for v in range(len(self.clusters[c].voxels)):
                loc = N.array(self.clusters[c].voxels[v][:3])
                for offset in mask:
                    newloc = loc + offset  # array (3-tuple) addition
#            if row[3]<>loc[0] and row[4]<>loc[1] and row[5]<>loc[2]:

    def idealized(self,radius):
        a = N.zeros(self.baseshape)
        for i in range(self.n):
            a = a + self.clusters[i].idealized(radius)
        return a

    def report(self,fname=None,sort=1):
        volumes = N.zeros(self.n)
        for i in range(self.n):
            volumes[i] = self.clusters[i].volume
        if sort:
            outputorder = N.argsort(volumes)
            outputorder = outputorder.tolist()
            outputorder.reverse()
        else:
            outputorder = N.arange(self.n)
        if fname <> None:
            f = open(fname,'w')
            f.write(self.clusters[0].report('header')+'\n')
            for i in range(self.n): # range(self.n-1,-1,-1):
                f.write(self.clusters[outputorder[i]].report()+'\n')
        else:
            returnlst = [self.clusters[0].report('header')+'\n']
            for i in range(self.n): # range(self.n-1,-1,-1):
                returnlst = returnlst+[self.clusters[outputorder[i]].report()+'\n']
            return returnlst

    def rank(self,rankby='size'):
        """
        rank(self,rankby='size') ... returns an array created from clustmap
           where all elements of a given cluster are replaced by their
           ranking according to 'size' or 'peak' value.
        """
        vals = []
        if rankby == 'size':
            for i in range(self.n):
                vals.append(int(self.clusters[i].volume))
        elif rankby == 'peak':
            for i in range(self.n):
                vals.append(int(self.clusters[i].peak))
        else:
            raise ValueError, "rankby must be 'size' or 'peak' in clustmap.rank()"
        ranks = N.argsort(vals) # biggest=n, smallest=1
        a = N.zeros(self.baseshape,N.Int)
        for i in range(self.n):
#            print (self.n-i), self.clusters[ranks[i]].volume
            this = N.not_equal(self.clusters[ranks[i]].toarray(),0)
            a = a + this*(self.n-i)  # multiplier makes biggest=1, etc
        return a

    def compare_clustmaps(self,other,radius,test_type='peak'):
        """
        compare_clustmaps(self,other,radius,test_type='peak')

        Important:  If clusters are close enough together but of different
        sign (i.e., one positive, one negative), they are NOT part of the
        'both' map.\n"""
        both = grouped_clustmaps(2)
        c1_only = clustmap()
        c2_only = clustmap()
        c1counts = N.zeros(self.n)
        c2counts = N.zeros(other.n)
        print 'Map1 clusters:',self.n
        print 'Map2 clusters:',other.n
        for i in range(self.n):  # loop through all clusters in 'self'
            clust1 = self.clusters[i]
            for j in range(other.n): # and compare to each cluster in 'other'
                clust2 = other.clusters[j]
                result = clust1.compare2clusters(clust2,radius,test_type)
                if result>0:  # 0 if not close enough, 1 if close enough, -1 if
                              # close enough but of differing sign
                    c1counts[i] = c1counts[i] + 1
                    c2counts[j] = c2counts[j] + 1
                    both.addclust(clust1,clust2)
                elif result<0:
                    print 'compare2clusters() found close pair w/ diff signs', ijk_to_xyz(clust1.peaklocation),ijk_to_xyz(clust2.peaklocation), '  ... adding to individual maps'
            if c1counts[i]==0:
#               print "added to c1"
                c1_only.add(clust1)
        for j in range(other.n):
            if c2counts[j] == 0:
#                print "Adding clust2[",j,"] to c2"
                c2_only.add(other.clusters[j])
        print 'both:',both.nclust, ' c1_only:',c1_only.n, ' c2_only:',c2_only.n, 'total: ',both.nclust+c1_only.n+c2_only.n
        return both, c1_only, c2_only


class grouped_clustmaps:
    """
Class for grouping together clustmaps (e.g., for a "both" map, where you want
to keep elements from each original map).  Members include:

nclust = number of clusters in the yoked maps
nmaps  = number of maps in this group
maps   = the maps themselves (each is a clustmap instance)

Note that the toarray() function will replace fcnl values of map1 with 20,
fcnl values of map2 with 30, and so on.

Usage:   grouped_clustmaps(nmaps=2)  ... number of (empty) maps to start with
"""
    def __init__(self,nmaps=2):
        self.nclust = 0
        self.nmaps = nmaps
        self.maps = []
        for i in range(nmaps):
            self.maps.append(clustmap())

    def addclust(self,*args):
        if len(args) <> self.nmaps:
            raise ValueError, "Incorrect number of clusters added to grouped_clustmap"
        for i in range(len(args)):
            self.maps[i].add(args[i])
#            for j in range(self.nclust):
#                print N.array(ijk_to_xyz(self.maps[i].clusters[j].peaklocation))
#            print
        self.nclust = self.nclust + 1

    def add(self,clustmap):
        """\nadd(self,clustmap) ... adds a whole clustermap, see addclust()\n"""
        self.nmaps = self.nmaps + 1
        self.maps.append(clustmap)

    def toarray(self,mode='one'):
        """\ntoarray(self,mode='one')  or 'many' to get 4D array)\n"""
        As = []
        for i in range(self.nmaps):
            As.append(self.maps[i].toarray())
        As = N.array(As)
#        print As.shape
        if mode == 'many':
            return As
        posAs = N.greater(As,0)
        negAs = N.less(As,0)
        multipliers = N.arange(20,(self.nmaps+2)*10,10)   # 20, 30, 40 ...
        multipliers.shape = [len(multipliers)]+[1]*(len(As.shape)-1)
        return N.sum(posAs*multipliers-negAs*multipliers,0)

    def report(self,fname=None):
        def _connectem(lst):
            return string.join(lst,'\n')

        def _interleave(*args):  # takes n equal-length lists and interleaves
                                # the elements (item1 l1l2l3..., item2 l1l2l3)
            l = []
            for i in range(len(args[0])):
                for j in range(len(args)):
                    l.append(args[j][i])
            return l
        
        l = []
        for i in range(self.nmaps):
            l.append(self.maps[i].report(None,0)) # report for map1, then for map2...
#        l = apply(pstat.abut,l) # put 2 (or more) reports side-by-side
#        l = map(_connectem,l)   # convert to single-line string
        volumes = N.zeros(self.nclust)
        for i in range(self.nclust):
            volumes[i] = self.maps[0].clusters[i].volume
        outputorder = N.argsort(volumes)  # sorts on increasing volumes
        outputorder = outputorder.tolist()
        outputorder.reverse()             # makes it decreasing volumes
        l = apply(_interleave,l) # OR, interleave nmaps cluster-groups
        newl = [l[0]]  # put in header, REMEMBER, first nmaps elements of l are headers
        l = l[self.nmaps:]
        for i in range(len(outputorder)):
            for j in range(self.nmaps):
                newl.append(l[(outputorder[i])*self.nmaps+j])
        l = newl
        if fname:
            f = open(fname,'w')
            f.write(l[0])  # write header line
            i = 0
            while i<len(l)-1:
                for j in range(self.nmaps):
                    f.write(l[i+j+1])  # +1 skips header line
                f.write('\n') # skip line in file between clusters
                i = i+self.nmaps
            return
        else:
            return l


def findlocalmax(data,localradius,threshold,voxelsize=3.125):
    """
Finds local maxima in a dataset, considering only voxel values > threshold.
Two local maxima within localradius separation are considered one.

Usage:   findlocalmax(data,localradius,threshold,voxelsize=3.125)
Returns: byloc, bypeak ... lists (x/y/z/i/j/k/val) sorted by loc and peakval
"""
    origshp = N.array(data.shape)
    kdata = N.where(N.greater(abs(data),threshold),data,0) # keep orig data

    # create a mask
    # convert it from 3D to linear offsets
    mask = create_spherical_mask(localradius/float(voxelsize))

    ## go through all pixels, looking for pixels <> 0
    ## when you find one, see if surrounding voxels (within mask) are < this
    ## if so, add this voxel to the localmaxima list
    ## continue until you've checked all pixels
    print 'Starting localmax search process ...'
    localmaxima = []
    ijk = N.array([0,0,0])
    while type(ijk) == N.ArrayType:
        if N.sum(ijk) == 100:
            print ijk
        if kdata[ijk] <> 0:
            # see if this is a local max by looping through all the offsets
            # in mask and seeing if all values at those offsets are < the
            # value in the center, adjusting for edge-effects (comparecount)`
            center = kdata[ijk]
            count = 0
            comparecount = len(mask)
            for offset in mask:
                oijk = ijk+offset   # 3-tuple (array) addition
                # check to see if any of the indices are out of range
                if N.sum(N.less(oijk,0))>0 or N.sum(N.greater(oijk,origshp))>0:
                    comparecount = comparecount - 1
                    continue
                if abs(kdata[oijk]) < abs(center):
                    count = count +1
            if count == comparecount:  # must be largest in local region
                ijkafni = ijk.tolist()
                ijkafni.reverse()
                xyzafni = ijk_to_xyz(ijkafni,voxelsize)
                localmaxima.append(xyzafni+ijkafni+[round(center,3)])
        # on to check next triple
        ijk = incr(ijk,N.array(origshp)-1)
    lmax_byloc = localmaxima
    print "Total peaks found = ",len(lmax_byloc)
    # put last (value) column up front, sort on that, and reverse the
    # resulting list to get the list sorted hi-lo by peak value
    localmaxima = pstat.colex(lmax_byloc,[6,0,1,2,3,4,5])
    localmaxima.sort()
    localmaxima.reverse()
    lmax_bypeak = pstat.colex(localmaxima,[1,2,3,4,5,6,0])
    return lmax_byloc, lmax_bypeak


def findclust(data,threshold,radius,volumethresh,voxelsize=3.125):
    """
Finds clusters of activation in the given data brick, where ...

data         = 3D data brick
threshold    = minimum value-of-interest in data (sets -thresh<val<thresh to 0)
radius       = the radius of connectivity (units=mm; USES VOXELSIZE)
volumethresh = minimum cluster volume to consider (units=ml)

Usage:   findclust(data,threshold,radius,volumethresh,voxelsize=3.125)
Returns: either a list of clusters (default), or
         an array of data.shape containing only peak and 1-radius data values
"""
    origshp = N.array(data.shape)  # save orig shape
    kdata = N.where(N.greater(abs(data),threshold),data,0) # keep orig data
    kdata = kdata.flat # contains signed data, minus below-threshold items
    n = len(kdata)

    # create a mask
    # convert it from 3D to linear offsets
    mask = create_spherical_mask(radius/float(voxelsize))
    x = origshp[0]
    y = origshp[1]
    z = origshp[2]
    offsets = N.array([y*z,z,1])
    offsetlist = []
    for i in range(len(mask)):
        tmp = N.sum(mask[i]*offsets)
        offsetlist.append(tmp)

    # loop through all datapoints
    clusters = clustmap()

    ## go through all pixels, looking for pixels <> 0
    ## when you find one, build a cluster, and zero out associated pixels
    ## continue until you've checked all pixels
    for ijk in range(n):
        if kdata[ijk] <> 0:
            # start forming new cluster
            three = ijk_to_three(ijk,x,y,z)  # convert bigindex to triple
            clust = cluster(data.shape)      # START OFF A NEW CLUSTER,
            tmp = clust.add(three,kdata[ijk],ijk)  # tmp should always be 1 (success)
            signeddata = kdata[ijk]          # save it for it's sign,
            kdata[ijk] = 0                   # and then zero out added pixel
            cpix = 0           # dummy variable for while-loop
            cpixcount = 1      # counter for number of pixels in cluster
            while cpix <= n:   # start growing this cluster
                nijk = clust.getnext(cpix)    # get bigindex of this/each voxel
                for o in range(len(offsetlist)):  # and loop thru all offsets
                    offset = offsetlist[o]
                    nidx = nijk+offset # bigidx for this offset from pixel cpix
                    if (nidx>0 and nidx<n and kdata[nidx]<>0 and kdata[nidx]*signeddata>0):
                        # add it to clust list
                        three = ijk_to_three(nidx,x,y,z)
                        success = clust.add(three,kdata[nidx],nidx)
                        if success:
                            cpixcount = cpixcount + 1 #incr cluster pixel count
                            kdata[nidx] = 0       # zero out this pixel
                cpix = cpix + 1       # on to the next pixel in this cluster
                if cpix >= cpixcount: # unless there aren't any more
                    break
            if clust.volume > volumethresh:
                clusters.add(clust)
    return clusters


def quickcompare(array1,array2,threshold):
    """
Takes 2 acivation map arrays, thresholds them at given level, and returns
three arrays: one where BOTH arrays 1 and 2 are above threshold, one where
ONLY array1 is above threshold, and one where ONLY array2 is above threshold.
In the BOTH array, positive values mean array1 and array2 were the same sign,
whereas negative values mean array1 and array2 were of different signs there.

Usage:   quickcompare(array1,array2,threshold)
Returns: both, array1-only, array2-only ... done voxel-by-voxel
"""
    a1 = N.greater(abs(array1),threshold)
    a1signs = N.less(array1,0)*-1 +N.greater(array1,0)
    a2 = N.greater(abs(array2),threshold)
    a2signs = N.less(array2,0)*-1 +N.greater(array2,0)
    return a1*a1signs*a2*a2signs*30, a1*N.logical_not(a2)*array1, a2*N.logical_not(a1)*array2


def mapcompare(map1,map2,threshold,clustradius,clustvolume,
               compareradius,test_type='peaks'):
    """
Takes 2 acivation maps and starts by finding local maxima for each,
based on the values of threshold, clustradius, and clustvolume.  Then,
it loops through one clustmap to find all peaks in the other that is
less than 'compareradius' mm away.  Returns one grouped_clustmap
(peaks-in-both-clustmaps, where map1 voxels have a fcnl value of 20,
map2 voxels have a fcnl value of 30, and active-in-both-maps voxels
have a value of 50), and two clustmaps (remaining peaks in map1,
remaining peaks in map2).  If test_type is set to 'com', the compare
process is based on the center-of-mass of each cluster rather than the
location of the peak activation. IF YOU WANT VOXEL-BY-VOXEL COMPARISONS,
TRY quickcompare().

Usage:   mapcompare(map1,map2,threshold,clustradius,clustvolume,
                    compareradius,test_type='peaks'):
Returns: peaks_in_both, peaks_in_one, peaks_in_two
"""
    print "Clustering map1."
    c1 = findclust(map1,threshold,clustradius,clustvolume,voxelsize=3.125)
    print "Clustering map2."
    c2 = findclust(map2,threshold,clustradius,clustvolume,voxelsize=3.125)
    print "Starting compare process ..."
    return c1.compare_clustmaps(c2,compareradius,test_type)


#===============  PARADIGM FILE CREATION  =====================

def makeepochs (infilename,outfilename='',keepalldata='',TR=0.0):
    """
This program takes an input file of times (min:sec), one time per
line, and creates an output file with the number of images per epoch.  If
you want to throw out images that fall across timestamps, press 't'
in response to the question, otherwise press 'k'.  If you "keep"
such images, then if >=0.5 of that image falls in an epoch, that's where
it gets counted.

Usage:   makeepochs(infilename,outfilename='blank',keepalldata='',TR=0.0)
Returns: None
"""

    print
    while keepalldata not in ['k','t','K','T']:
        keepalldata = raw_input('(K)eep all data, or (T)oss images crossing condition boundaries (k,t): ')
    print
    while TR == 0:
        TR = input('Input the TR for this experiment: ')
    TR = float(TR)

    times = io.getstrings(infilename)
    if outfilename == '':
        outfilename = infilename + '.e'

    totalsec = [0] * len(times)
    for i in range(len(times)):
        indx = string.index(times[i][0],':')
        min = string.atoi(times[i][0][0:indx])
        sec = string.atoi(times[i][0][indx+1:])
        totalsec[i] = min*60 + sec
    if totalsec[-1] <> 0:
        print 'Adding a zero timepoint'
        totalsec.append(0)

    epochnum = 0
    carryover = 0
    imagesperepoch = [0]*1000
    print '\nAll times in seconds.'
    lofl = ['\n',
            ['Start','End','CarryIn(sec)','Diff','# Images','Leftover(im)']]
    for i in range(len(totalsec)-1):
        if totalsec[i+1] == '':
            print 'Whitespace in input file !!!'
        diff = totalsec[i] - totalsec[i+1] - carryover   # rat(rat(12.5))=12!!
        images = diff/rat(TR)               # diff is Rat if carryover is
        leftover = images%1
        print i, totalsec[i],totalsec[i+1],carryover, diff, rat(diff), images, leftover
        lofl.append(totalsec[i],totalsec[i+1],carryover,diff,int(images),images%1)
        if leftover <> 0:
            if keepalldata in ['k','K']:
                if leftover >= 0.5:
                    imagesperepoch[epochnum] = [int(images)+1, '']
                    carryover = (1-leftover)*TR
                    epochnum = epochnum + 1
                elif leftover < 0.5:
                    imagesperepoch[epochnum] = [int(images),'']
                    carryover = - (leftover*TR)
                    epochnum = epochnum + 1
            else:       # keepalldata in ['t','T']
                imagesperepoch[epochnum] = [int(images),'']
                epochnum = epochnum + 1
                imagesperepoch[epochnum] = [1,0]
                epochnum = epochnum + 1
                carryover = (1-leftover)*TR
        else:
            imagesperepoch[epochnum] = [int(images),'']
            epochnum = epochnum + 1
            carryover = 0
    print 'Done.\n'
    imagesperepoch = imagesperepoch[0:epochnum]
    io.writedelimited(imagesperepoch,'\t',outfilename)
    return None


def makepara(offon, sample_rate, run_length=-1):
    """
  [paradigm] = makepara(

    offon,        # -xx for fixed off/on/off blocking at xx sec intervals, OR
                  # [-xx yy -zz aa ...] for irregular paradigm (xx in sec, - means off)
    sample_rate,  # in Hz
    run_length)   # length of entire run, in seconds

    returns paradigm      # vector of zeros for OFF, ones for ON
"""
    offon = N.array(offon)
    if len(offon)==1:
        if (offon<0): # when offon is integer<0, assume blocked data
            blockpoints = abs(offon*sample_rate)
            ttrig = range(blockpoints,run_length*sample_rate+1,blockpoints*2)
            trigs = N.zeros(run_length*sample_rate) # assumes start with OFF
            for idx in ttrig:
                trigs[idx:idx+blockpoints] = 1
            trigs = trigs[0:run_length*sample_rate]
        else:
            sprintf('offon should be negative, OR a 2+ element array in fmri.makepara.py')
    elif len(offon) == 2: # must be [off, on]
        if run_length <0:
            print 'Need a run length for [off, on] pairs in fmri.makepara'
            return
        trigs = N.zeros(run_length*sample_rate)
        for i in range(N.ceil(run_length*sample_rate/(N.sum(abs(offon))))):
            offstart = i*sample_rate*(N.sum(abs(offon)))
            onstart = offstart + sample_rate*offon[1]
            onend = onstart + sample_rate*offon[1]
            trigs[offstart:onstart] = 0  # OFF
            trigs[onstart:onend] = 1     # ON
    elif len(offon) == 4: # must be [presec, off, on, postsec]
        pass
    else: # must be a list of off(neg), on(pos) times, in seconds
        blockpoints = abs(offon[0]*sample_rate)
        if offon[0]<0:
            trigs = N.zeros(blockpoints)
        else:
            trigs = 1*N.ones(blockpoints)
        for time in offon[1:]:
            blockpoints = abs(time*sample_rate);
            if time<0:
                trigs[len(trigs):len(trigs)+blockpoints] = N.zeros(blockpoints)
            else:
                trigs[len(trigs):len(trigs)+blockpoints] = +1*N.ones(blockpoints)
    return trigs



def makeparadigm (epochfilenames):
    """
This function takes a list of filenames [usually the edited output
from makeepochs()] and creates a paradigm file with the same filenames
plus a '.para' extension.  The input files must have 2 columns: number
of images in that epoch, and the contrast coefficient for that epoch.

Usage:   makeparadigm(epochfilenames)
Returns: None
"""
    fnames = glob.glob(epochfilenames)
    if len(fnames) == 0:
        print "NO FILENAMES MATCH PATTERN !!!"
        return None
    for inname in fnames:
        try:
            indx = string.index(inname,'.e')
            outname = inname[0:indx] + '.p'
        except ValueError:
            outname = inname + '.para'
        epochs = io.get(inname)
        outfile = open(outname,'w')

        for [numimages,contrastval] in epochs:
            for i in range(numimages):
                outfile.write(str(contrastval))
                outfile.write('\n')
    return None


def makePvsT(inpara,outpara):
    """
Takes a paradigm file for one run (=2 blocks) and converts it into a 14-block
paradigm file, Practice vs. Teach (i.e., +1s for blocks 3-7, -1s for blocks
9-13, and 0s elsewhere.

Usage:   makePvsT(inpara,outpara)      paras are 2 filenames (can overwrite)
"""
    d = io.aget(inpara).flat
    d0 = [0.0] * len(d)

    dhalf = d*1
    dhalf[len(d)/2:] = 0.0

    paradigm = d0 +d.tolist()*2 +dhalf.tolist() +(d*-1).tolist()*2 + (dhalf*-1).tolist()
    io.put(Numeric.array(paradigm)[:,Numeric.NewAxis],outpara)


def correct_for_lag(p,killnumber=1):
    """
Takes a paradigm array [time] and returns an equal-length array with
'killnumber' 1s or -1s set to 0 at the start of each new string of -1s
or 1s.  That is, [0 0 1 1 1 1 1] ==> [0 0 0 0 1 1 1] if killnumber=2.

Usage:   correct_for_lag(p,killnumber=1)
Returns: new paradigm file, killing 'killnumber' images at start of each block
"""
    p = N.asarray(p)
    newp = p*1
    last = newp[0]
    for i in range(1,len(newp)):
        if (newp[i]==0) or (last==newp[i]): # if a 0 or no change, go on
            continue
        else:          # if just changed from 1 to -1 (or vice versa)
            last = newp[i] # save the new "block" value
            newp[i:i+killnumber] = 0    # kill the first image of this block
    return newp


def make10paras(inepochs,outparaprefix,shift=1):
    """
Takes an epochs file and converts it into a 14-block paradigm files,
Practice vs. Teach (i.e., +1s for blocks 3-7, -1s for blocks 9-13, and 0s
elsewhere, as well as Practice-vs-Rest and Teaching-vs-Rest paradigm files.

Usage:   make10paras(inepochs,outparaprefix,shift=1)  2 filenames (overwrites!)
"""
    sh = str(shift)
    d = io.get(inepochs)
    epochs = pstat.colex(d,0)
    for i in range(len(d)):
        if d[i][0] > max(epochs)-2:
            d[i] = [d[i][0],1]         # 1 for both ON blocks in a run
        else:
            d[i] = [d[i][0],0]         # 0 otherwise
    PvsTpara = []
    for [numimages,contrastval] in d:
        for i in range(numimages):
            PvsTpara = PvsTpara + [contrastval]
    
    d0 = [0.0] * len(PvsTpara)
    dhalf = N.array(PvsTpara*1)
    dhalf[len(PvsTpara)/2+1:] = 0.0
    PTparadigm = d0 +PvsTpara*2 +dhalf.tolist() +(N.array(PvsTpara)*-1).tolist()*2 + (dhalf*-1).tolist()
    io.put(N.array(PTparadigm)[:,N.NewAxis],outparaprefix+'PvsT.p')
    io.put(N.array(correct_for_lag(PTparadigm))[:,N.NewAxis],outparaprefix+'PvsTshift'+sh+'.p')

    for i in range(len(d)):
        if d[i][0] > max(epochs)-2:
            d[i] = [d[i][0],1]         # 1 for both ON blocks
        elif d[i][0] > 1:
            d[i] = [d[i][0],-1]         # -1 for off periods
    vsRpara = []
    for [numimages,contrastval] in d:
        for i in range(numimages):
            vsRpara = vsRpara + [contrastval]

    dhalf = N.array(vsRpara*1)
    dhalf[len(vsRpara)/2+1:] = 0.0
    Rparadigm = d0 +vsRpara*2 +dhalf.tolist() +vsRpara*2 +dhalf.tolist()
    io.put(N.array(Rparadigm)[:,N.NewAxis],outparaprefix+'vsR.p')
    io.put(N.array(correct_for_lag(Rparadigm))[:,N.NewAxis],outparaprefix+'vsRshift'+sh+'.p')

    PRparadigm = d0 +vsRpara*2 +dhalf.tolist() +d0*3
    io.put(N.array(PRparadigm)[:,N.NewAxis],outparaprefix+'PvsR.p')
    io.put(N.array(correct_for_lag(PRparadigm))[:,N.NewAxis],outparaprefix+'PvsRshift'+sh+'.p')

    TRparadigm = d0*4 +vsRpara*2 +dhalf.tolist()
    io.put(N.array(TRparadigm)[:,N.NewAxis],outparaprefix+'TvsR.p')
    io.put(N.array(correct_for_lag(TRparadigm))[:,N.NewAxis],outparaprefix+'TvsRshift'+sh+'.p')

    Ronly = N.where(N.equal(N.array(vsRpara),-1),-1,0)
    Ronlyparadigm = Ronly.tolist()*7
    io.put(N.array(Ronlyparadigm)[:,N.NewAxis],outparaprefix+'Ronly.p')
    io.put(N.array(correct_for_lag(Ronlyparadigm))[:,N.NewAxis],outparaprefix+'Ronlyshift'+sh+'.p')
    return None



#=======================  IMAGE STATISTICS FUNCTIONS  =======================

def finddistances(parray,threshold=0.001,slicethick=7.0,dx=3.25,dy=3.25):
    """
Creates a 1D array of values corresponding to Euclidean distance
between all pairs of significantly activated pixels in a brain map.  Input
is a stack of contiguous slices containing KSLOGP values.  The threshold is the
p-value cutoff for significance, and the slice thickness and x and y values
are used to calculate distance in real space (rather than in pixel-coordinate
space).

Usage:   finddistances(parray,threshold=0.001,slicethick=7.0,dx=3.25,dy=3.25)
"""
    def distance(a,b):
        """Calculates the Euclidean distance bewteen two points a and b."""
        a = N.asarray(a)
        b = N.asarray(b)
        return math.sqrt(N.add.reduce((a-b)**2))

    parray = abs(parray) * -1
    parray = N.exp(parray)
    sshape = parray.shape
    signif = N.less(parray,threshold)
    signif = signif.flat
    print N.add.reduce(signif)
    sigindices = [[0.0,0.0,0.0]]
    for i in range(len(signif)):
        if signif[i] == 1:
            slice = N.divide(i,sshape[1]*sshape[2])
            x = N.divide(N.remainder(i,sshape[1]*sshape[2]),sshape[2])
            y = N.remainder(N.remainder(i,sshape[1]*sshape[2]),sshape[2])
            sigindices.append([slice,x,y])
    sigindices = N.array(sigindices[1:],'f')
    print sigindices[0:10]
    print sigindices.shape, sigindices.typecode()
    a = sigindices[:,0] * slicethick
    b = sigindices[:,1] * dx
    c = sigindices[:,2] * dy
    pstat.pl(pstat.aabut(sigindices, a, b, c))
    sigindices = pstat.aabut(a,b,c)
    distances = []
    for i in range(len(sigindices)):
        for j in range(i+1,len(sigindices)):
            distances.append(distance(sigindices[i],sigindices[j]))
    return N.array(distances)


def do_tstats(pixelarray,paradigm,tdim=0,related=0):
    """
Returns a p-value array from a [time,x,y] array (i.e., as-read) of fMRI
pixel values using a simple t-test.

Usage:   do_tstats(pixelarray,paradigm,tdim=0,related=0)
Returns: t-image, p-image
"""
    if tdim <> 0:  # If time dim not at end, put it there (w/ transpose)
        tdims = range(len(pixelarray.shape))
        tdims.remove(tdim)
        tdims = [tdim] + tdims
        data1 = N.transpose(pixelarray,tdims) # DOESN'T CARRY THRU NEXT LINE@@@
    data1 = N.compress(N.equal(paradigm,1),pixelarray,0)  # 0=Time dimension
    data2 = N.compress(N.equal(paradigm,-1),pixelarray,0) # 0=Time dimension
#    print data1.shape, data2.shape
    if not related:
        t, pimage = stats.attest_ind(data1,data2,0)
    else:
        t, pimage = stats.attest_rel(data1,data2,0)
    return t, pimage


def do_ksstats(pixelarray,paradigm,tdim=0,threshold=100):
    """
Computes a p-value array from a [time,x,y] array (i.e., as-read)
of fMRI pixel values using a KS-test.  Threshold used to skip calculation
of KS values.

Usage:   do_ksstats(pixelarray,paradigm,tdim=0,threshold=100)
Returns: p-value array with shape=(x,y) 
"""
    if tdim <> 0:  # If time dim not at end, put it there (w/ transpose)
        tdims = range(len(pixelarray.shape))
        tdims.remove(tdim)
        tdims = [tdim] + tdims
        pixelarray = N.transpose(pixelarray,tdims)
    data1 = N.compress(N.equal(paradigm,1),pixelarray,0) # 0=Time dimension
    data2 = N.compress(N.equal(paradigm,-1),pixelarray,0)
    print data1.shape, data2.shape
    imgshp = data1.shape[1:]
    data1 = N.reshape(data1,[data1.shape[0],-1,1])
    data2 = N.reshape(data2,[data2.shape[0],-1,1])
    parray = N.zeros(data1.shape[1],N.Float32)
    d = N.zeros(data1.shape[1],N.Float64)
    print data1.shape, data2.shape, parray.shape, d.shape
    for i in range(len(parray)):
        if i%1000==0: print i
        if data1[0,i,0] < threshold:
            d[i] = 0.0
            parray[i] = 1.0
        else:
            d[i], parray[i] = stats.aks_2samp(N.ravel(data1[:,i]),
                                              N.ravel(data2[:,i]))
            if d[i]<0:
                parray[i] = -parray[i]
    return N.reshape(d,imgshp), N.reshape(parray,imgshp)


def pmap(imagestack,paradigm,tdim=0,statsfunc=do_ksstats):
    """
Returns a -log(p) map for overlay on anatomical images.  Assumes
imagestack has dimensions (as-read) of [time,x,y].

Usage:   pmap(imagestack,paradigm,tdim=0)
Returns: p-values, -log(p) values
"""
    if tdim <> 0:
        tdims = range(len(imagestack.shape)) # transpose to put time dim at 0
        tdims.remove(tdim)
        tdims = [tdim] + tdims
        imagestack = N.transpose(imagestack,tdims)
    if len(imagestack) != len(paradigm):
        print "Number of images and paradigm length don't agree."
        return
    coeff = pstat.aunique(paradigm)
    if N.add.reduce(coeff) != 0.0:                 # if sum(coeffieients)!=0
        newcoeff = coeff - stats.amean(coeff)      # then make the sum=0
        newpara = N.zeros(len(paradigm))
        for i in range(len(coeff)):
            newpara = newpara + N.equal(paradigm,coeff[i])*newcoeff[i]

    stat,ps = statsfunc(imagestack,paradigm,tdim) # dimensions = [time,x,y]
    logimage = p2log(ps)
    return ps, logimage


def pcmap(pixelarray,paradigm,threshold=300,tdim=0):
    """
Calcs a percent-change map given a stack of images and a paradigm (1/-1/0).
The returned map is masked, returning percent-change values for pixels in
the input baseline (-1) images whose mean intensity is >'threshold'.

Usage:   pcmap(pixelarray,paradigm,threshold=300,tdim=0)
Returns: pcmap
"""
    if tdim <> 0:  # If time dim not at end, put it there (w/ transpose)
        tdims = range(len(pixelarray.shape))
        tdims.remove(tdim)
        tdims = [tdim] + tdims
        data1 = N.transpose(pixelarray,tdims) # DOESN'T CARRY THRU NEXT LINE@@@
    data1 = N.compress(N.equal(paradigm,1),pixelarray,0)  # 0=Time dimension
    data2 = N.compress(N.equal(paradigm,-1),pixelarray,0) # 0=Time dimension
    ONmean = stats.amean(data1,0)
    BASEmean = stats.amean(data2,0)
    diffs = ONmean - BASEmean
    zerodivproblem = N.equal(BASEmean,0)
    pcmap = N.where(zerodivproblem,0,100*diffs/BASEmean.astype(N.Float))
    mask = N.where(N.greater(BASEmean,threshold),1,0)
    return pcmap*mask


def squash(imagestack,paradigm):
    """
Takes a stack of images [time,x,y], multiplies them pixel by pixel
times the paradigm array, and adds the resulting values, again pixel by
pixel.

Usage:   squash(imagestack,paradigm)
"""
    if len(imagestack) != len(paradigm):
        print "Number of images and paradigm length don't agree."
        return
    newstack = imagestack*paradigm[:,N.NewAxis,N.NewAxis]
    return N.add.reduce(newstack)


def fixmotion(stack,maxchange):
    """
Takes a stack of images [time,x,y], and compares successive intensity value
differences to maxchange (a constant or a matrix of values equal in size to
the original images).  Any pixel intensity changes larger (in abs. value)
than maxchange between time t and t+1 are eliminated (subtracted out) from
that point until the end of the image stack.  This is a BAD approach, but
may be acceptable for small motions (<< smallest voxel dimension) when
there is no other option.

Usage:   fixmotion(stack,maxchange)    stack = array, maxchange = array or val
Returns: fixed version of stack (pixel intensities adjusted at large jumps)
"""
    sdmap = stats.stdev(stack,0)
    diffs = stack[1:] - stack[:-1]
    modlist = []
    newstack = stack*1
    for i in range(1,len(stack)-1):
        test1 = N.greater(abs(diffs[i-1]),maxchange) #sdmap*sd_threshold)
        test2 = N.greater(abs(diffs[i-1]),maxchange) *N.greater(abs(diffs[i-2]),maxchange/2.0)
        test3 = N.greater(abs(diffs[i-1]),maxchange) *N.greater(abs(diffs[i]),maxchange/2.0)
        mods = N.where(test1+test2+test3,1,0) * diffs[i-1]
        anychanges = stats.sum(N.where(N.not_equal(mods,0),1,0))
        if anychanges > 0:
            newstack[i:] = newstack[i:] -mods
            modlist = modlist + [[i,anychanges]]
    return newstack, modlist


def fixmotionattimes(stack,maxchange,timepoints):
    """
Takes a stack of images [time,x,y], looks at the timepoints specified, and
if there is a fMRI signal intensity change greater than maxchange at that
timepoint, it eliminates it in its entirety.

Usage:   fixmotionattimes(stack,maxchange,timepoints)  stack = array
Returns: fixed version of stack, list of pairs (timepoint,number-of-changes)
"""
    modlist = []
    diffs = stack[1:] - stack[:-1]
    newstack = stack*1
    for i in timepoints:
        test = N.greater(abs(diffs[i-1]),maxchange)
        mods = N.where(test,1,0) * diffs[i-1]
        anychanges = stats.sum(N.where(N.not_equal(mods,0),1,0))
        if anychanges > 0:
            newstack[i:] = newstack[i:] -mods
            modlist = modlist + [[i,anychanges]]
    return newstack, modlist


def elimmotionattimes(stack,start,end):
    """
Takes a stack of images [time,x,y], and removes ALL signal changes for all
pixels at the given timepoints.  Following timepoints are also adjusted so
as not to lose the original timeseries shape following the elimination
points.

Usage:   elimmotionattimes(stack,start end)  stack = array [t,x,y]
Returns: fixed version of stack, list of pairs (timepoint,number-of-changes)
"""
    modlist = []
    newstack = stack.astype('f')*1
    minidx = max(0,start-10)
    m = stats.mean(stack[minidx:start],0)
    for t in range(start,end+1):
        mods = newstack[t] - m
        newstack[t:] = newstack[t:] -mods
    return newstack


def correlationmap(a,fcn,threshold=300):
    """
Calculates a Pearson correlation coefficient for each pixel in array a
(with dims [time,x,y]).  Returns a correlation map and probability map.
Threshold determines whether a r/p values are calculated based on mean
pixel intensity in images a.  Use threshold=None for no masking based on
a numerical threshold on the original data.

Usage:   correlationmap(a,fcn,threshold=300)  a,fcn equal-length arrays
Returns: correlation map, probability map
"""
    TINY = 1.0e-20
    a = a.astype('d')
    fcn = N.ravel(fcn).astype('d')
    assert len(a) == len(fcn), "Fcn and array not of same length"
    n = float(len(fcn))
    fmean = stats.mean(fcn)
    imean = stats.mean(a,0)
    r_den = ((n*stats.ass(a,0) - stats.asquare_of_sums(a,0)) *
             (n*stats.ass(fcn)-stats.asquare_of_sums(fcn)))
    r_den = N.sqrt(N.where(N.less(r_den,0),0,r_den))  # kill negs due to truncation
    fcn.shape = fcn.shape + (1,)*(len(a.shape)-1)
    r_num = n*(N.add.reduce(a*fcn,0)) - N.add.reduce(a,0)*N.add.reduce(fcn)
    r = (r_num / r_den)

    r = N.where(N.equal(r_den,0),0.0,r) # zero out cases with 0 in denom
    # Zero out non-brain regions (i.e.find pixels with a minimum value>thresh)
    if threshold <> None:
        r = N.where(N.less(N.minimum.reduce(a,0),threshold),0.0,r)
    df = n-2
    shp = r.shape
    r = N.ravel(r)
    p = N.zeros(len(r),N.Float)
    for i in range(len(r)):
        t = r[i]*math.sqrt(df/((1.0-r[i]+TINY)*(1.0+r[i]+TINY)))
        p[i] = stats.betai(0.5*df,0.5,df/(df+t*t))
    r.shape = shp
    p.shape = shp
    return r,p


def pairedmapcorrelate(a,b,threshold=None):
    """
Calculates a Pearson correlation coefficient for each pixel in array a
(with dims [time,x,y]) with each pixel in array b (dims [time,x,y]).
Returns a Pearson-r map and a probability map.
Threshold determines whether a r/p value is calculated based on mean
pixel intensity in images a.  Use threshold=None for no masking based on
a numerical threshold on the original data.

Usage:   pairedmapcorrelate(a,b,threshold=0)  a,b equal-size arrays, [time,x,y]
Returns: Pearson-r map, probability map
"""
    TINY = 1.0e-20
    a = a.astype('d')
    b = b.astype('d')
    assert len(a) == len(b), "a and b arrays not of same length"
    print max(a.flat), max(b.flat)
    n = float(len(b))
    r_den = ((n*stats.ass(a,0) - stats.asquare_of_sums(a,0)) *
             (n*stats.ass(b,0)-stats.asquare_of_sums(b,0)))
    r_den = N.sqrt(N.where(N.less(r_den,0),0,r_den))  # kill negs due to truncation
    r_den = N.where(N.less(r_den,TINY),TINY,r_den) # kill zero-denominators
    r_num = n*(N.add.reduce(a*b,0)) - N.add.reduce(a,0)*N.add.reduce(b,0)
    r = (r_num / r_den)

    r = N.where(N.equal(r_den,0),0.0,r) # zero out cases with 0 in denom
    # Zero out non-brain regions (i.e.find pixels with a minimum value>thresh)
    if threshold <> None:
        r = N.where(N.less(N.minimum.reduce(a,0),threshold),0.0,r)
    df = n-2
    shp = r.shape
    r = N.ravel(r)
    p = N.zeros(len(r),N.Float)
    for i in range(len(r)):
        tmp = df/((1.0-r[i]+TINY)*(1.0+r[i]+TINY))
        if tmp<0: # must be in round-off-error land
            tmp = 0
        t = r[i]*math.sqrt(tmp)
        p[i] = stats.betai(0.5*df,0.5,df/(df+t*t))
    r.shape = shp
    p.shape = shp
    return r,p


def corr3maps(filepattern,threshold_on=2.5e-5,threshold_off=1e-4):
    """
Calculates 3 correlation maps (4 files per map ... an r-map and a p-map, each
having an associated .bfloat and .hdr) on each data file corresponding to
filepattern:

1)  PvsR ... correlates 1 vs -1 for P vs R
2)  TvsR ... correlates 1 vs -1 for T vs R
3)  PvsT ... finds pixels that are P-active (p<threshold_on) AND that are
                T-inactive (p>threshold_off); each pixel in the resulting
                map is scaled by the signif correlation r-value (that is,
                if r=0.2 then p=1e-2; if r=0.4, p=1e-4)

The fcn requires the xxPvsR.p, xxTvsR.p and xxPvsT.p paradigm files.

Usage:   corr3maps(filepattern, threshold_on=2.5e-5,threshold_off=1e-4)
"""
    fnames = glob.glob(filepattern)
    assert len(fnames) >0, "NO FILES MATCH PATTERN GIVEN IN corr3maps."
    for fname in fnames:
        try:
            d=io.bget(fname)
            print fname
        except:
            print 'Problem with',fname
            continue

        f = N.ravel(io.aget(fname[3:5]+'PvsR.p'))
        if len(d) <> len(f):
            raise ValueError,"Image stack and corr. fcn not of same length."
        ## Calculate correlation map for Practice vs. Rest
        Prmap,Ppmap = correlationmap(d,f)
        idx1 = string.rfind(fname,'_')
        idx2 = string.rfind(fname,'.')
        bput(Prmap,fname[:idx1]+'_cPvsRr'+fname[idx1:idx2]+'.bfloat',1)
        bput(p2log(Ppmap),fname[:idx1]+'_cPvsRp'+fname[idx1:idx2]+'.bfloat',1)

        f = N.ravel(io.aget(fname[3:5]+'TvsR.p'))
        if len(d) <> len(f):
            raise ValueError,"Image stack and corr. fcn not of same length."
        ## Calculate correlation map for Teaching vs. Rest
        Trmap,Tpmap = correlationmap(d,f)
        bput(Trmap,fname[:idx1]+'_cTvsRr'+fname[idx1:idx2]+'.bfloat',1)
        bput(p2log(Tpmap),fname[:idx1]+'_cTvsRp'+fname[idx1:idx2]+'.bfloat',1)

        Pr_scaled_p = N.power(N.ones(Prmap.shape,'f')*10,
                              -1*(Prmap*10))    #.astype('i'))
        Tr_scaled_p = -1*N.power(N.ones(Trmap.shape,'f')*10,
                                 -1*(Trmap*10)) #.astype('i'))
        PTmap1 = N.where(N.less(Ppmap,threshold_on)*N.greater(Tpmap,threshold_off),
                         Pr_scaled_p,0)
        PTmap2 = N.where(N.less(Tpmap,threshold_on)*N.greater(Ppmap,threshold_off),
                         Tr_scaled_p,0)
        PTpmap = PTmap1 + PTmap2
        PTpmap = N.where(N.equal(PTpmap,0),1,PTpmap)
        bput(p2log(PTpmap),fname[:idx1]+'_cPvsTp'+fname[idx1:idx2]+'.bfloat',1)
    return


def log2p(a):
    """
Calculates -exp(a) by removing the neg-signs, performing the exp(a) and then
putting the negative of the signs back on.
    
Usage:   log2p(a)
Returns: -exp(a)
"""
    negs = N.where(N.less(a,0),-1,1)
    newa = N.exp(-1*abs(a))
    return newa*negs


def p2log(a):
    """
Safely calculates -ln(a), where 0-values in the input array are converted
to zeros in the returned array.  +/- signs of original values are inverted
AFTER taking the log of abs(a).

Usage:   p2log(a)
Returns: -ln(a)
"""
    negs = N.where(N.less(a,0),-1,1)  # -1/1s where a<0 / a>0
    newa = N.equal(a,0) +negs*a       # 1s where a is zero, abs(a) elsewhere
    newa = -1*N.log(newa)             # take -log(a)
    return newa*negs                  # put signs back onto a


def safelog(a):
    """
Safely calculates ln(a), where 0-values and negative values in the input array
are converted to zeros in the returned array.

Usage:   safelog(a)
Returns: -ln(a)
"""
    negs = N.where(N.less(a,0),-1,1)  # -1/1s where a<0 / a>0
    newa = N.equal(a,0) +negs*a       # 1s where a is zero, abs(a) elsewhere
    return N.log(newa)*negs


def sn_bypara(stack,para,compareval=-1):
    """
Computes stats.signaltonoise (mean/stdev) on the image-stack, using
images where associated para(digm) value equals 'compareval'.

Usage:   sn_bypara(stack,para)   stack=[time,x,y], para=paradigm (-1/0/1s)
Returns: array of stats.signaltonoise values, using -1s in para(digm)
"""
    para = N.array(para).flat
    newstack = N.compress(N.equal(para,compareval),stack,0)
    return stats.signaltonoise(newstack)


def roi_timecourse(inarray,mask,dims=0):
    """
Usage:   roi_timecourse(inarray,mask,dims=0) ... a = [time,x,y]
Returns: mean of inarray along dims, but only for elements where mask<>0
"""
    mask = N.notequal(mask,0)  # make sure mask is binary 0/1
    a = inarray*mask
    n = float(stats.sum(mask))
    a = stats.sum(a,dims)
    return a/n      # return mean timecourse over 'mask' voxels


def varmap(a,windowsize):
    """
Calculates a variance map for an image array, using a window +/-windowsize.

Usage:   varmap(a,windowsize)
Returns: array the shape of a, filled with variances
"""
    n = N.zeros(a.shape,N.Float)
    if len(n.shape) == 2:
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                xmin = max(0,i-windowsize)
                xmax = min(a.shape[0],i+windowsize)
                ymin = max(0,j-windowsize)
                ymax = min(a.shape[1],j+windowsize)
                n[i,j] = stats.var(a[xmin:xmax,ymin:ymax])
        return n
    elif len(n.shape)==3:
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                for k in range(a.shape[2]):
                    xmin = max(0,i-windowsize)
                    xmax = min(a.shape[0],i+windowsize)
                    ymin = max(0,j-windowsize)
                    ymax = min(a.shape[1],j+windowsize)
                    zmin = max(0,k-windowsize)
                    zmax = min(a.shape[2],k+windowsize)
                    n[i,j,k] = stats.var(a[xmin:xmax,ymin:ymax,zmin:zmax])
        return n
    else:
        raise ValueError, "Only 2D and 3D arrays allowed in varmap()"

def piecewiselineardriftcorrect(d,para):
    """
Drift corrects first dimension of array d given paradigm para (-1s and 1s)
using a piecewise-linear approach between alternating OFF periods.

Usage:   piecewiselineardriftcorrect(d,para)
Returns: drift-corrected version of d
"""
    # look for "OFF" values (-1s)
    OFFindices = N.ravel(support.findval(para,-1))
    print OFFindices.shape

    # list the indices into OFFindices where there's a discontinuity in numbering
    btwOFFs = [0]
    for i in range(1,len(OFFindices)):
        if OFFindices[i] > 1+OFFindices[i-1]:  # a gap in the "off" periods
            btwOFFs.append(i)
    btwOFFs.append(len(OFFindices))

    fixd = d+0.

    # loop through succesive pairs of markers
    for i in range(len(btwOFFs)-2): 
        # get a list of OFF indices (only) for a sequence OFF-ON-OFF
        if i == 0: # this is the first block, use whole preOFF period
            start = btwOFFs[i]
        else:      # not first block, use last half of preOFF period only
            start = int(round((btwOFFs[i]+btwOFFs[i+1])/2.0))
        if i == len(btwOFFs)-3:  # this is the last block, use whole postOFF period
            end = btwOFFs[i+2]
        else:                    # not last block, use first half of postOFF period
            end = int(round((btwOFFs[i+1]+btwOFFs[i+2])/2.0))
        print start, end
        xs = OFFindices[start:end]

        # grab the two off periods of MR data
        ys = N.take(d,xs)

        # calc slopes based on adjacent OFF periods
        slopes = ts.getslopes(ys, xs) 
        print xs
        print slopes.shape

    #    nys = ys - N.multiply.outer(xs,slopes-stats.mean(slopes,0,keepdims=1))

        # interpolate slopes for the OFF-ON-OFF part of this period
    #    print OFFindices[start],OFFindices, start, end, len(OFFindices)
        linestart = OFFindices[start]
        if i == len(btwOFFs)-3:  # this is the last block, use whole postOFF period
            lineend = OFFindices[-1]
        else:                    # not last block, use first half of postOFF period
            lineend = OFFindices[end]
        line = N.arange(linestart,lineend)
        print linestart, lineend, line
        line = line - stats.mean(line)
        adj = N.multiply.outer(line,slopes)
        print adj.shape

        # correct OFF-ON period for OFF-to-OFF slope
        fixd[linestart:lineend] -= adj

        # subtract mean "off" value from OFF-ON part of MR data
        mn = stats.mean(N.take(fixd,xs),0,keepdims=1)
        print mn.shape
        fixd[linestart:lineend] -= mn
        print fixd.shape

    # obliterate bad scans
    BADindices = N.ravel(support.findval(para>=33333,1))
    for i in BADindices:
        fixd[i] = 0
    fixd[-1] = 0

    # add back in mean signal levels for each pixel
    fixd += stats.mean(d,0,keepdims=1)

    return fixd


def pldc(d,para):
    """
Drift corrects first dimension of array d given paradigm para (-1s and 1s)
using a piecewise-linear approach between alternating OFF periods. Use a
para value >=33333 to exclude that timepoint from slope calcs.

Usage:   pldc(d,para)
Returns: drift-corrected version of d
"""
    # trim para
    para = N.ravel(para)[:len(d)]
    
    # look for "OFF" values (-1s) or IGNORE (>=33333) values
    offs = para==-1
    bads = para>=33333
    OFFindices = N.ravel(support.findval(N.ravel(offs+bads),1))

    # list indices into OFFindices where there's a discontinuity in numbering
    for i in range(len(para)): # start with the first non-tossed datapoint
        if para[i] < 33333:
            btwOFFs = [i]
            break
    for i in range(1,len(OFFindices)):
        # a discontinuity in numbering
        if OFFindices[i]>1+OFFindices[i-1]: # and para[OFFindices[i]-1]<33333:
            btwOFFs.append(i)
    btwOFFs.append(len(OFFindices))

    print btwOFFs
    # remove any islands of >=33333 within ON periods
    killist = []
    for i in range(1,len(btwOFFs)-2):
        # see what previous clump and next clump are like
        print OFFindices[btwOFFs[i]]-1, OFFindices[btwOFFs[i+1]]-1
        if para[OFFindices[btwOFFs[i]]-1]==1 and para[OFFindices[btwOFFs[i+1]]-1]==1:
            killist.append(btwOFFs[i]) # if both clumps are 1s, it's an island
    print killist
    for item in killist:
        btwOFFs.remove(item)
    print btwOFFs

    fixd = d+0.

    # loop through succesive pairs of markers
    print 'Lists of indices into paradigm used for correction ...'
    for i in range(len(btwOFFs)-2): 
        # get a list of OFF indices (only) for a sequence OFF-ON-OFF
        if i == 0: # this is the first block, use whole preOFF period
            start = btwOFFs[i]
        else:      # not first block, use last half of preOFF period only
            start = int(round((btwOFFs[i]+btwOFFs[i+1])/2.0))
        if i == len(btwOFFs)-3:  # this is the last block, use whole postOFF period
            end = btwOFFs[i+2]
        else:                    # not last block, use first half of postOFF period
            end = int(round((btwOFFs[i+1]+btwOFFs[i+2])/2.0))
#        print start, end
        xs = OFFindices[start:end]

        # prune out any >=33333 indices
        xs = xs.tolist()
        for j in range(len(xs)-1,-1,-1):
#            print len(para), j, xs[j]
            if para[xs[j]] >= 33333:
                del xs[j]
        xs = N.array(xs)
        print xs

        # grab the two off periods of MR data
        ys = N.take(d,xs)

        # calc slopes based on adjacent OFF periods
        slopes = ts.getslopes(ys, xs) 
#        print xs
#        print slopes.shape

    #    nys = ys - N.multiply.outer(xs,slopes-stats.mean(slopes,0,keepdims=1))

        # interpolate slopes for the OFF-ON-OFF part of this period
    #    print OFFindices[start],OFFindices, start, end, len(OFFindices)
        linestart = OFFindices[start]
        if i == len(btwOFFs)-3:  # this is the last block, use whole postOFF period
            lineend = OFFindices[-1]
        else:                    # not last block, use first half of postOFF period
            lineend = OFFindices[end]
        line = N.arange(linestart,lineend)
#        print linestart, lineend, line
        line = line - stats.mean(line)
        adj = N.multiply.outer(line,slopes)
#        print adj.shape

        # correct OFF-ON period for OFF-to-OFF slope
        fixd[linestart:lineend] -= adj

        # subtract mean "off" value from OFF-ON part of MR data
        mn = stats.mean(N.take(fixd,xs),0,keepdims=1)
#        print mn.shape
        fixd[linestart:lineend] -= mn
#        print fixd.shape

    # obliterate bad scans
    BADindices = N.ravel(support.findval(para>=33333,1))
    for i in BADindices:
        fixd[i] = 0
    fixd[-1] = 0

    # add back in mean signal levels for each pixel
    fixd += stats.mean(d,0,keepdims=1)

    return fixd

def find_onsets(d,thresh,minoffpoints=3):
    """
Usage:   find_onsets(d,thresh,minoffpoints=3)
Returns: list of onset indices (below-to-above thresh indices)
"""
    l = []
    for i in range(len(d)):
        if (d[i]>thresh and N.sum(d[i-minoffpoints:i]>thresh)==0):
            l.append(i)
    return l


def find_offsets(d,thresh,minoffpoints=3):
    """
Usage:   find_offsets(d,thresh,minoffpoints=3)
Returns: list of offset indices (above-to-below thresh transitions)
"""
    l = []
    for i in range(minoffpoints,len(d)):
        if (d[i]<thresh and N.sum(d[i-minoffpoints:i]<thresh)==0):
            l.append(i)
    return l

def lengths2para(lengths, startwith=-1):
    """
Usage:   lengths2para(lengths, startwith=-1) ... lengths=list of block lengths
Returns: paradigm of -1s and 1s of length sum(lengths)
"""
    para = []
    for i in range(len(lengths)):
#        print i, pow(-1,i)
        para = para +[-1*pow(-1,i)]*lengths[i]
    return N.array(para)
