# Build ENV 

## Apptainer (Singularity)
- apptainer.def
- build with `apptainer build alignment.sig apptainer.def`

## docker
- Dockerfile

## Future changes
- bitsandbytes packege: currently it does not support CUDA version > 12, need to build manually (already in config files). Once the issue fixed, we can add bitsandbytes back to requirements.txt