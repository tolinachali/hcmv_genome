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

Here is 

![image](https://github.com/tolinachali/hcmv_genome/assets/130226558/12d00ced-eed1-4961-be52-fb7baf1ce1db)


But at the end to run the willowj I tried  to  arrange the YML file and still unsucceul 

May be how to identify the  sample group file and groupcategory definition needs to be edited

##  group category definitoins 

![image](https://github.com/tolinachali/hcmv_genome/assets/130226558/f59b8427-0400-4b4a-9169-a32d5589e658)

## Sample group file


![image](https://github.com/tolinachali/hcmv_genome/assets/130226558/d72102d7-d601-4e13-8652-c0f5710de860)









































































































