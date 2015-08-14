#Bayer Programming interview question

#Author: Preeti Singh, Carnegie Mellon University
#Date of Submission: June 2nd, 2014


#Check if the variant is in the range 
def searchrange(variant, fileidx): 
    if variant == None:
        return False
    if not variant.strip():
        return False
    s = variant.split()
    for i in range(0, len(chrm_list)):
        if (s[0] == chrm_list[i] and lowthr_list[i] <= int(s[1]) \
        and int(s[1]) <= highthr_list[i]):
            variant_cnt[fileidx] += 1
            return True
    return False

#Check if the variants of all three files overlap 
def overlap(i1,i2,i3):
    if i1 == None or i2 == None or i3 == None:
        return False
    if not (i1.strip() and i2.strip() and i3.strip()):
        return False

    if1 = i1.split() 
    if2 = i2.split()
    if3 = i3.split()
    if(if1[0]==if2[0]==if3[0]):
        if(if1[1] == if2[1] == if3[1]):
            return True
    return False

#Find the minimmum variant position among 3 files
def minfile(i1,i2,i3):
    bestchrom = -1
    bestpos = -1
    bestidx = -1

    if i1 != None and i1.strip():
        s = i1.split()
        chrom = chrmval[s[0]]
        pos = int(s[1])
        if ((bestchrom == -1) or (chrom < bestchrom) or \
        ((chrom == bestchrom) and (pos < bestpos))):
            
            bestchrom = chrom
            bestpos = pos 
            bestidx = 0

    if i2 != None and i2.strip():
        s = i2.split()
        chrom = chrmval[s[0]]
        pos = int(s[1])
        if ((bestchrom == -1) or (chrom < bestchrom) or \
        ((chrom == bestchrom) and (pos < bestpos))):
            
            bestchrom = chrom
            bestpos = pos 
            bestidx = 1

    if i3 != None and i3.strip():
        s = i3.split()
        chrom = chrmval[s[0]]
        pos = int(s[1])
        if ((bestchrom == -1) or (chrom < bestchrom) or \
        ((chrom == bestchrom) and (pos < bestpos))):
            
            bestchrom = chrom
            bestpos = pos 
            bestidx = 2

    return bestidx


#Read the Ranges file
r1 =  open('ranges.txt') 
ifile = []
#Read all the input files having variant position
ifile.append(open('input1.txt'))
ifile.append(open('input2.txt'))
ifile.append(open('input3.txt'))

lowthr_list = []
highthr_list = []
chrm_list = []
f = {}
chrmval = {}
chrmnum = 0
variant_cnt = [0,0,0]
cnt_overlap = 0

for line in r1:
    s = line.split()
    #split each line
    chrm = s[0]
    low_thr = int(s[1])
    high_thr = int(s[2])
    #load these values into memory #using list
    lowthr_list.append(low_thr)
    highthr_list.append(high_thr)
    chrm_list.append(chrm)

    if (not (s[0] in chrmval)):
        chrmval[s[0]] = chrmnum
	chrmnum = chrmnum + 1
   
#process the input files
for i in range(0,3):
    f[i] = ifile[i].readline()
    f[i] = ifile[i].readline()

for i in range(0,2):
    searchrange(f[i], i)

if searchrange(f[2], 2):
    if overlap(f[0], f[1], f[2]):
        cnt_overlap += 1

while(1):
    idx = minfile(f[0], f[1], f[2])
    if idx == -1:
        break

    f[idx] = ifile[idx].readline()

    if f[idx] != None:
        if searchrange(f[idx], idx):
            if overlap(f[0], f[1], f[2]):
                cnt_overlap += 1

for i in range(0,3):
    print "Number of variants in range for file " + str(i+1) + ": " + str(variant_cnt[i])

print "Number of variants in range that overlap over all three files: " + str(cnt_overlap)

