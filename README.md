## GDR_calc for 10 hcmv_samples

To calculate GDR_value I tried to figure out clinical samples and lab_strain samples from the 405 hcmv GenBank data 

After that I selected 5 clinical samples and 5 lab strain samples to save time rather than  all of the samples 

To the next,  extract a fasta file which is important for sequence alignment using  python script and do a multiple sequence alignment. 

I have added a python code used to extract the fasta file

using MAFFT software which have speed than clustalo
The command :

###  mafft 10_sample_hcmv.fasta > aligned_hcmv.fasta

Now possible to find a distance matrix which is very important to for GDR_calculation 

Also  I used a python script to find a didtance matrix for the samples 

Here is the distance matrix of the 10 samples 

![image](https://github.com/tolinachali/hcmv_genome/assets/130226558/048d29c3-b327-4884-86b5-48fcc4174b5c)

I tried to rearrange the yaml file and 

preapare  the  sample group file and groupcategory definition as follows 

##  group category definitoins 

![image](https://github.com/tolinachali/hcmv_genome/assets/130226558/29823567-120b-4d5d-b3c5-83e9688d4d11)


## Sample group file

![image](https://github.com/tolinachali/hcmv_genome/assets/130226558/44a67b46-2a9a-4d31-b043-090c80f695dd)


### The result looks like :


![image](https://github.com/tolinachali/hcmv_genome/assets/130226558/f09d6822-2226-44a3-87bb-fa1ccea56391)


# Even if I get  GDRCalculationResultsJ When I run the willowj still thtough error like below 


![ERRor](https://github.com/tolinachali/hcmv_genome/assets/130226558/154614a0-ad9f-4ba6-a170-8bf7972390be)





































































































