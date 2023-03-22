import os
import sys
import getopt

#input = input()



#os.system('source /home/amax/Desktop/HCM/nnunet_workdir-4CH-cine/nnUNET-README/nnUNet/venv/bin/activate')

def main(argv):
    i = str(argv[1])
    o = str(argv[2])

    idir,ifile=os.path.split(i)
    os.system('mkdir '+i+'dir')
    os.system('unzip '+i+' -d '+i+'dir')
    os.system('mkdir '+o+'dir')
    os.environ["nnUNet_raw_data_base"] = "/home/amax/Desktop/HCM/nnunet_workdir-4CH-cine/nnUNET-README/nnUNet/" \
                                         "nnunet_workdir/nnunet_dataset"
    os.environ["nnUNet_preprocessed"] = "/home/amax/Desktop/HCM/nnunet_workdir-4CH-cine/nnUNET-README/nnUNet/" \
                                        "nnunet_workdir/nnunet_preprocessed"
    os.environ["RESULTS_FOLDER"] = "/home/amax/Desktop/HCM/nnunet_workdir-4CH-cine/nnUNET-README/nnUNet/" \
                                   "nnunet_workdir/nnunet_trained_models"
    os.system('CUDA_VISIBLE_DEVICES=0 nnUNet_predict '
              '-i %s'
              ' -o %s'
              ' -tr nnUNetTrainerV2 -ctr nnUNetTrainerV2CascadeFullRes -m 3d_fullres -p nnUNetPlansv2.1 -t '
              'Task530_4CH_SEG' % (i+'dir',o+'dir')
          )
    os.system('zip -r '+o+' '+o+'dir -j')
'''
    i2 = str(argv[3])
    o2 = str(argv[4])
    os.system('mkdir '+i2+'dir')
    os.system('unzip '+i2+' -d '+i2+'dir')
    os.system('mkdir '+o2+'dir')

    os.system('CUDA_VISIBLE_DEVICES=0 nnUNet_predict '
              '-i %s'
              ' -o %s'
              ' -tr nnUNetTrainerV2 -ctr nnUNetTrainerV2CascadeFullRes -m 3d_fullres -p nnUNetPlansv2.1 -t '
              'Task531_SAX_SEG' % (i2+'dir',o2+'dir')
          )
    os.system('zip -r '+o2+' '+o2+'dir -j')


'''
if __name__ == "__main__":
    main(sys.argv)

