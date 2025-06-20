from SynthSeg.brain_generator import BrainGenerator
import nibabel as nib
labs = ['/Users/vicentcaselles/work/research/project_MARCOS/Multiple-Sclerosis-TIMILS/subj1/flair_bfc_filled_NeuroMorph_Parcellation.nii.gz',
        '/Users/vicentcaselles/work/research/project_MARCOS/Multiple-Sclerosis-TIMILS/subj2/flair_bfc_filled_NeuroMorph_Parcellation.nii.gz',
        '/Users/vicentcaselles/work/research/project_MARCOS/Multiple-Sclerosis-TIMILS/subj3/flair_bfc_filled_NeuroMorph_Parcellation.nii.gz']

ntries = 5
i = 0
for l in labs:
    bg = BrainGenerator(labels_dir=l, normalise='zscore')
    for n in range(ntries):
        im, seg = bg.generate_brain()
        nib.save(
            nib.Nifti1Image(im, bg.aff),
            f'test_{i+1}.nii.gz'
        )
        i += 1
